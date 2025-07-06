import os
import numpy as np
from collections import defaultdict
from core.parser import parse_execution_file
from datetime import timedelta


def analisar_execucoes(lista_arquivos, n_execucoes=30):
    tempos_execucao = []
    restricao_eq_inade_media_do_valor_em_todas_solucoes_por_execucao = defaultdict(list)
    restricao_eq_inade_std_do_valor_em_todas_solucoes_por_execucao = defaultdict(list)
    qtd_solucoes_com_restricao_ca_por_iteracao = defaultdict(list)
    qtd_solucoes_com_restricao_eq_inadequa_por_iteracao = defaultdict(list)
    lista_de_numero_solucoes_primeiro_pareto_a_cada_iteracao = defaultdict(list)
    numero_de_frentes_de_pareto_por_iteracao = defaultdict(list)
    exec = 1
    for path in lista_arquivos[:n_execucoes]:
        if not os.path.isfile(path):
            print(f"[AVISO] Arquivo {path} não encontrado.")
            continue

        dados = parse_execution_file(path)

        if "execution_time_ms" in dados:
            tempos_execucao.append(dados["execution_time_ms"])

        if "iterations" in dados:
            for iteracao in dados["iterations"]:
                i = iteracao["iteration"]
                qtd_solucoes_com_restricao_ca_por_iteracao[i].append(iteracao["ca0Rest1"])
                qtd_solucoes_com_restricao_eq_inadequa_por_iteracao[i].append(iteracao["eqInadRest2"])

        for it in dados.get("iterations", []):
            media = it.get("medianrest2")
            i = it["iteration"]
            if media is not None:
                if np.isnan(media):
                    media = 0.0
                restricao_eq_inade_media_do_valor_em_todas_solucoes_por_execucao[i].append(
                    media)  # agora é uma mastri de valores de restrição

        for it in dados.get("iterations", []):
            std = it.get("stdrest2")
            i = it["iteration"]
            if std is not None:
                if np.isnan(std):
                    std = 0.0
                restricao_eq_inade_std_do_valor_em_todas_solucoes_por_execucao[i].append(
                    std)  # agora é uma mastri de valores de restrição

        if "pareto" in dados:
            for i, p in dados["pareto"].items():
                lista_de_numero_solucoes_primeiro_pareto_a_cada_iteracao[i].append(p[0])  # num_solucoes
                numero_de_frentes_de_pareto_por_iteracao[i].append(p[1])  # num_paretos

    # Estatísticas globais
    media_tempo = np.mean(tempos_execucao)
    std_tempo = np.std(tempos_execucao)

    # print("Tempo médio de execução (ms):", round(media_tempo, 2))
    # print("Desvio padrão do tempo (ms):", round(std_tempo, 2))

    # Iterações selecionadas para gráfico de barras
    iteracoes_destaque = list(range(1, 41)) + [80, 200, 400, 520, 1000]
    medias_qtd_sol_com_restri_ca = {}
    medias_qtd_sol_com_restri_equinad = {}

    for i in iteracoes_destaque:
        # ca_lista e eq_lista pegam as listas de valores na iteração n:
        # ou seja, todos os 30 valores na iteração n
        ca_lista = qtd_solucoes_com_restricao_ca_por_iteracao.get(i)
        eq_lista = qtd_solucoes_com_restricao_eq_inadequa_por_iteracao.get(i)
        # medias_qtd_sol_com_restri_ca e medias_qtd_sol_com_restri_equinad são
        # duas listas das medias de qtd de soluções
        # com restrição por iteração, respectivamente de ca e eq. inadeq.
        medias_qtd_sol_com_restri_ca[i] = float(np.mean(ca_lista)) if ca_lista else 0.0
        medias_qtd_sol_com_restri_equinad[i] = float(np.mean(eq_lista)) if eq_lista else 0.0

    # Histograma de medianrest2 por execução
    medias_de_valores_de_restr_eq_inadeq = [np.mean(v) for _, v in sorted(
        restricao_eq_inade_media_do_valor_em_todas_solucoes_por_execucao.items())]
    std_da_media_dos_valores_de_restri_de_eq_inadeq = [np.mean(v) for _, v in sorted(
        restricao_eq_inade_std_do_valor_em_todas_solucoes_por_execucao.items())]

    # Pareto até iteração 960
    iteracoes_pareto = list(range(40, 1000, 40))
    medias_pareto_solucoes = {}
    medias_qtd_de_frentes_paretos = {}
    for i in iteracoes_pareto:
        lista_sol = lista_de_numero_solucoes_primeiro_pareto_a_cada_iteracao.get(i)
        lista_frentes = numero_de_frentes_de_pareto_por_iteracao.get(i)
        if lista_sol:
            medias_pareto_solucoes[i] = float(np.mean(lista_sol))
        if lista_frentes:
            medias_qtd_de_frentes_paretos[i] = float(np.mean(lista_frentes))

    tempos_execucao_hhmmss = {
        i + 1: str(timedelta(milliseconds=t)) for i, t in enumerate(tempos_execucao)
    }

    media_td = timedelta(milliseconds=media_tempo)
    std_td = timedelta(milliseconds=std_tempo)

    media_execucao_hhmmss = str(timedelta(milliseconds=media_tempo)).split(".")[0]
    std_execucao_hhmmss = str(timedelta(milliseconds=std_tempo)).split(".")[0]

    return {
        "tempos_execucao": tempos_execucao_hhmmss,
        "media_execucao_hhmmss": media_execucao_hhmmss,
        "std_execucao_hhmmss": std_execucao_hhmmss,
        "medias_qtd_sol_com_restri_ca": medias_qtd_sol_com_restri_ca,
        "medias_qtd_sol_com_restri_equinad": medias_qtd_sol_com_restri_equinad,
        "medias_de_valores_de_restr_eq_inadeq": medias_de_valores_de_restr_eq_inadeq,
        "std_da_media_dos_valores_de_restri_de_eq_inadeq": std_da_media_dos_valores_de_restri_de_eq_inadeq,
        "medias_pareto_solucoes": medias_pareto_solucoes,
        "pareto_frentes": medias_qtd_de_frentes_paretos
    }
