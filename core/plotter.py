import numpy as np
import itertools
from datetime import timedelta
import matplotlib.pyplot as plt
import re




# def plot_medias_por_iteracao(
#     dados, titulo, ylabel, inicio, fim, passo, max_y, extras=None, usar_fitness=False
# ):
#     fig, ax = plt.subplots(figsize=(12, 5))
#     ticks_size = 20
#     label_size=50
#     if extras is not None:
#         iteracoes_desejadas = list(range(inicio, fim, passo)) + extras
#     else:
#         iteracoes_desejadas = list(range(inicio, fim, passo))
#
#     if usar_fitness:
#         # Mapeia avaliação de aptidão (ex: 200) para geração (200 // 100 = 2)
#         valores = [dados.get(i // 100, 0.0) for i in iteracoes_desejadas]
#         categorias = [format(i, '.1e').replace('.', ',').replace('e', 'E') for i in iteracoes_desejadas]
#         ax.set_xticks([])
#
#         bars = ax.bar(range(len(categorias)), valores, width=0.4)
#
#         for i, label in enumerate(categorias):
#             ax.text(
#                 i + 0.3,
#                 -max_y * 0.0,
#                 label,
#                 fontsize=ticks_size,
#                 fontweight='bold',
#                 rotation=45,
#                 ha='right',
#                 va='top',
#                 transform=ax.transData,
#                 clip_on=False
#             )
#
#         plt.subplots_adjust(bottom=0.7)
#         ax.set_xlabel("Avaliação de aptidão", fontsize=label_size, fontweight='bold', labelpad=80)
#     else:
#         valores = [dados.get(i, 0.0) for i in iteracoes_desejadas]
#         categorias = [str(i) for i in iteracoes_desejadas]
#         bars = ax.bar(categorias, valores, width=0.4)
#         ax.set_xticks(range(len(categorias)))
#         ax.set_xticklabels(categorias, fontsize=ticks_size, fontweight='bold')
#         ax.set_xlabel("Geração", fontsize=label_size, fontweight='bold')
#
#     ax.set_title(titulo, fontsize=label_size, fontweight='bold')
#     ax.set_ylabel(ylabel, fontsize=label_size, fontweight='bold')
#     ax.set_ylim(0, max_y)
#     ax.set_yticks(np.arange(0, max_y + 5, 5))
#     ax.tick_params(axis='y', labelsize=ticks_size)
#     [label.set_fontweight('bold') for label in ax.get_yticklabels()]
#
#     ax.grid(axis='y', linestyle='--', linewidth=0.5)
#
#     plt.tight_layout()
#     plt.show()


def plot_medias_por_iteracao(
    dados, titulo, ylabel, inicio, fim, passo, max_y,
    extras=None, usar_fitness=False,
    erase_number_tick_x=False, erase_number_tick_y=False,
    step_tick_x=2, step_tick_y=2
):
    fig, ax = plt.subplots(figsize=(12, 5))
    ticks_size = 28
    label_size = 50

    extras = extras or []
    if extras:
        extras = set(extras)

    iteracoes_desejadas = list(range(inicio, fim, passo)) + list(extras)

    if usar_fitness:
        valores = [dados.get(i // 100, 0.0) for i in iteracoes_desejadas]
        categorias = [format(i, '.1e').replace('.', ',').replace('e', 'E') for i in iteracoes_desejadas]
        ax.set_xticks([])

        bars = ax.bar(range(len(categorias)), valores, width=0.4)

        for i, label in enumerate(categorias):
            marco = iteracoes_desejadas[i]
            mostrar_label = (
                not erase_number_tick_x
                or (marco in extras)
                or (i % step_tick_x == 0)
            )
            if mostrar_label:
                ax.text(
                    i + 0.3,
                    -max_y * 0.0,
                    label,
                    fontsize=ticks_size,
                    fontweight='bold',
                    rotation=45,
                    ha='right',
                    va='top',
                    transform=ax.transData,
                    clip_on=False
                )

        plt.subplots_adjust(bottom=0.7)
        ax.set_xlabel("Avaliação de aptidão", fontsize=label_size, fontweight='bold', labelpad=120)

    else:
        valores = [dados.get(i, 0.0) for i in iteracoes_desejadas]
        categorias = [str(i) for i in iteracoes_desejadas]
        bars = ax.bar(range(len(categorias)), valores, width=0.4)
        ax.set_xticks(range(len(categorias)))

        ax.set_xticklabels([
            categorias[i] if (
                not erase_number_tick_x
                or iteracoes_desejadas[i] in extras
                or i % step_tick_x == 0
            ) else '' for i in range(len(categorias))
        ], fontsize=ticks_size, fontweight='bold')

        ax.set_xlabel("Geração", fontsize=label_size, fontweight='bold')

    ax.set_title(titulo, fontsize=label_size, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=label_size, fontweight='bold')
    ax.set_ylim(0, max_y)
    yticks = np.arange(0, max_y + 5, 5)
    ax.set_yticks(yticks)

    if erase_number_tick_y:
        ax.set_yticklabels([
            f"{int(y)}" if i % step_tick_y == 0 else '' for i, y in enumerate(yticks)
        ], fontsize=ticks_size, fontweight='bold')
    else:
        ax.tick_params(axis='y', labelsize=ticks_size)
        [label.set_fontweight('bold') for label in ax.get_yticklabels()]

    ax.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()






# def plot_histograma(
#     valores: list,
#     titulo: str,
#     ylabel: str,
#     max_y: float = 100,
#     inicio: int = 1,
#     fim: int = None,
#     passo: int = 1,
#     extras: list = None,
#     usar_fitness: bool = False
# ):
#     fig, ax = plt.subplots(figsize=(12, 5))
#     tick_size=20
#     label_size=50
#     if fim is None:
#         fim = len(valores) + 1
#
#     extras = extras or []
#     base_indices = list(range(inicio, fim + 1, passo))
#     all_indices = base_indices + extras
#
#     if usar_fitness:
#         yvalores = []
#         for i in all_indices:
#             if i in base_indices:
#                 idx = (i - inicio) // passo
#                 yvalores.append(valores[idx] if 0 <= idx < len(valores) else 0.0)
#             else:
#                 idx = 38 + ((i // 100) // 40) - 1
#                 yvalores.append(valores[idx] if 0 <= idx < len(valores) else 0.0)
#         categorias = [format(i, '.1e').replace('.', ',').replace('e', 'E') for i in all_indices]
#     else:
#         #aqui tem uma falha se for pegar por geração porque acima da geração 40 é a 80 e não a 41
#         #mas como vou avalizar por marco de fitness não vou tratar
#         yvalores = [valores[i - 1] if 1 <= i <= len(valores) else 0.0 for i in all_indices]
#         categorias = [str(i) for i in all_indices]
#
#     bars = ax.bar(range(len(categorias)), yvalores, width=0.4)
#
#     if usar_fitness:
#         ax.set_xticks([])  # Remove os ticks automáticos
#
#         for i, label in enumerate(categorias):
#             ax.text(
#                 i + 0.3,
#                 -max_y * 0.0,  # levemente acima da base
#                 label,
#                 fontsize=tick_size,
#                 fontweight='bold',
#                 rotation=45,
#                 ha='right',
#                 va='top',
#                 transform=ax.transData,
#                 clip_on=False
#             )
#
#         # Aumenta a margem inferior para caber ticks E legenda
#         plt.subplots_adjust(bottom=0.7)
#
#         # Define a legenda do eixo X ainda mais abaixo
#         eixo_x = "Avaliação de aptidão"
#         ax.set_xlabel(eixo_x, fontsize=label_size, fontweight='bold', labelpad=80)
#     else:
#         ax.set_xticks(range(len(categorias)))
#         ax.set_xticklabels(categorias, fontsize=label_size, fontweight='bold')
#         ax.set_xlabel("Execução", fontsize=label_size, fontweight='bold')
#
#     ax.set_title(titulo, fontsize=label_size, fontweight='bold')
#     ax.set_ylabel(ylabel, fontsize=label_size, fontweight='bold')
#     ax.set_ylim(0, max_y)
#     ax.set_yticks(np.linspace(0, max_y, 6))
#     ax.tick_params(axis='y', labelsize=tick_size)
#     [label.set_fontweight('bold') for label in ax.get_yticklabels()]
#     ax.grid(axis='y', linestyle='--', linewidth=0.5)
#
#     plt.tight_layout()
#     plt.show()

def plot_histograma(
    valores: list,
    titulo: str,
    ylabel: str,
    max_y: float = 100,
    inicio: int = 1,
    fim: int = None,
    passo: int = 1,
    extras: list = None,
    usar_fitness: bool = False,
    erase_number_tick_x: bool = False,
    step_tick_x: int = 2
):
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots(figsize=(12, 5))
    tick_size = 20
    label_size = 50

    if fim is None:
        fim = len(valores) + 1

    extras = extras or []
    extras_set = set(extras)

    base_indices = list(range(inicio, fim + 1, passo))
    all_indices = base_indices + extras

    if usar_fitness:
        yvalores = []
        for i in all_indices:
            if i in base_indices:
                idx = (i - inicio) // passo
                yvalores.append(valores[idx] if 0 <= idx < len(valores) else 0.0)
            else:
                idx = 38 + ((i // 100) // 40) - 1
                yvalores.append(valores[idx] if 0 <= idx < len(valores) else 0.0)
        categorias = [format(i, '.1e').replace('.', ',').replace('e', 'E') for i in all_indices]
    else:
        yvalores = [valores[i - 1] if 1 <= i <= len(valores) else 0.0 for i in all_indices]
        categorias = [str(i) for i in all_indices]

    bars = ax.bar(range(len(categorias)), yvalores, width=0.4)

    if usar_fitness:
        ax.set_xticks([])

        for i, label in enumerate(categorias):
            marco = all_indices[i]
            mostrar_label = (
                not erase_number_tick_x
                or (marco in extras_set)
                or (i % step_tick_x == 0)
            )
            if mostrar_label:
                ax.text(
                    i + 0.3,
                    -max_y * 0.0,
                    label,
                    fontsize=tick_size,
                    fontweight='bold',
                    rotation=45,
                    ha='right',
                    va='top',
                    transform=ax.transData,
                    clip_on=False
                )

        plt.subplots_adjust(bottom=0.7)
        ax.set_xlabel("Avaliação de aptidão", fontsize=label_size, fontweight='bold', labelpad=80)
    else:
        ax.set_xticks(range(len(categorias)))
        ax.set_xticklabels([
            categorias[i] if (
                not erase_number_tick_x
                or i % step_tick_x == 0
            ) else ''
            for i in range(len(categorias))
        ], fontsize=label_size, fontweight='bold')

        ax.set_xlabel("Execução", fontsize=label_size, fontweight='bold')

    ax.set_title(titulo, fontsize=label_size, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=label_size, fontweight='bold')
    ax.set_ylim(0, max_y)
    ax.set_yticks(np.linspace(0, max_y, 6))
    ax.tick_params(axis='y', labelsize=tick_size)
    [label.set_fontweight('bold') for label in ax.get_yticklabels()]
    ax.grid(axis='y', linestyle='--', linewidth=0.5)

    plt.tight_layout()
    plt.show()








def parse_tempo_em_timedelta(tempo_str):
    try:
        partes = tempo_str.split(":")
        if len(partes) == 3:
            horas, minutos, segundos = map(float, partes)
            return timedelta(hours=horas, minutes=minutos, seconds=segundos)
    except Exception as e:
        print(f"Erro ao converter tempo '{tempo_str}': {e}")
    return timedelta()



def parse_tempo_em_timedelta(tempo_str):
    try:
        # Caso com dias, ex: "2 days, 23:44:37.455000"
        if "days" in tempo_str:
            dias_str, tempo_str = tempo_str.split(", ")
            dias = int(dias_str.split()[0])
        else:
            dias = 0

        partes = tempo_str.split(":")
        if len(partes) == 3:
            horas, minutos, segundos = map(float, partes)
            return timedelta(days=dias, hours=horas, minutes=minutos, seconds=segundos)

    except Exception as e:
        print(f"Erro ao converter tempo '{tempo_str}': {e}")

    return timedelta()



def plot_tempo_execucao(dados, titulo, ylabel, inicio, fim, passo, extras=None, media=0.0, desvio=0.0, max_horas=20):
    tick_size = 18
    label_size = 30
    plt.figure(figsize=(12, 5))

    if extras is not None:
        iteracoes_desejadas = list(range(inicio, fim, passo)) + extras
    else:
        iteracoes_desejadas = list(range(inicio, fim, passo))

    # Converte os tempos (em string) para timedelta e depois para segundos
    tempos = [
        parse_tempo_em_timedelta(dados.get(i, "00:00:00")).total_seconds()
        for i in iteracoes_desejadas
    ]
    categorias = [str(i) for i in iteracoes_desejadas]

    # Criação do gráfico de barras
    plt.bar(categorias, tempos, width=0.4)

    # Eixo Y: formatação como [Xd\nhh:mm:ss] ou [hh:mm:ss]
    def formatar_tempo(segundos, _):
        if segundos == 0:
            return "0d"

        dias = int(segundos) // 86400
        resto = int(segundos) % 86400
        horas = resto // 3600
        minutos = (resto % 3600) // 60
        segundos_restantes = resto % 60

        if dias > 0:
            if horas == 0 and minutos == 0 and segundos_restantes == 0:
                return f"{dias}d"
            else:
                return f"{dias}d\n{horas:02}:{minutos:02}:{segundos_restantes:02}"
        else:
            return f"{horas:02}:{minutos:02}:{segundos_restantes:02}"

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(formatar_tempo))

    # Define intervalo dos ticks com base no tempo máximo
    tempo_max = max(tempos)
    if tempo_max >= 86400:  # 1 dia
        passo_ticks = 86400  # 1 dia
    else:
        passo_ticks = 3600   # 1 hora

    plt.yticks(np.arange(0, tempo_max + passo_ticks, passo_ticks))

    plt.title(titulo, fontsize=label_size, fontweight='bold')
    plt.xlabel(f"Execuções: tempo médio = {media}, desvio padrão = {desvio}", fontsize=label_size, fontweight='bold')
    plt.ylabel(ylabel, fontsize=label_size, fontweight='bold')
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    # Controle de formatação dos eixos
    plt.xticks(fontsize=tick_size, fontweight='bold')
    plt.yticks(fontsize=tick_size, fontweight='bold')

    plt.show()




def plot_pareto(pareto_solucoes: dict, pareto_frentes: dict):
    iteracoes = list(pareto_solucoes.keys())
    tick_size = 18
    label_size = 30
    plt.figure(figsize=(12, 5))

    # Linha sólida para o 1º Pareto
    plt.plot(iteracoes, list(pareto_solucoes.values()), label="Soluções no 1º Pareto")

    # ALTERAÇÃO: Linha tracejada para "Número de Frentes"
    plt.plot(iteracoes, list(pareto_frentes.values()), label="Número de Frentes", linestyle='--')

    # Ajuste direto da legenda
    legenda = plt.legend()
    for texto in legenda.get_texts():
        texto.set_fontsize(18)
        texto.set_fontweight('bold')

    plt.title("Evolução do Pareto: media 30 execuções", fontsize=label_size, fontweight='bold')
    plt.xlabel("Geração", fontsize=label_size, fontweight='bold')
    plt.ylabel("Valor", fontsize=label_size, fontweight='bold')
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(fontsize=14, fontweight='bold')
    plt.yticks(fontsize=14, fontweight='bold')
    plt.show()







def extrair_codigo_multiplicado(path: str) -> str:
    match = re.search(r'FUN(\d+)\.CSV$', path, re.IGNORECASE)
    if match:
        numero = int(match.group(1))
        resultado = str(numero * 100)
        return resultado
    else:
        raise ValueError("O caminho não termina com 'FUN<numero>.CSV'")


def extrair_numero_execution(path: str) -> int:
    match = re.search(r'execution(\d+)', path, re.IGNORECASE)
    if match:
        return int(match.group(1))
    else:
        raise ValueError("Não foi possível encontrar o número após 'execution'.")



def plotar_frentes_pareto(frentes: list[list[tuple[float, float]]], path: str):

    aval_aptidao= extrair_codigo_multiplicado(path)
    execucao= extrair_numero_execution(path)

    """
    Plota dois gráficos:
    1. Todas as frentes de Pareto com cores e marcadores diferentes
    2. Apenas a primeira frente (mais convergida), com o mesmo estilo do gráfico anterior
    """
    marcadores = ['o', 's', 'D', '^', 'v', '*', 'P', 'X', 'h', 'H']
    cores = ['blue', 'green', 'red', 'orange', 'purple', 'brown', 'pink', 'olive', 'cyan', 'magenta']
    estilos = itertools.cycle(zip(marcadores, cores))

    # Grava o estilo da primeira frente
    marcador_convergido, cor_convergida = next(estilos)
    fonte_legenda_size=50
    ticks_size=28
    # Gráfico com todas as frentes
    plt.figure(figsize=(10, 6))
    for idx, frente in enumerate(frentes):
        xs, ys = zip(*frente)
        if idx == 0:
            marcador, cor = marcador_convergido, cor_convergida
        else:
            marcador, cor = next(estilos)
        #s=60 define o tamanho dos marcadores (pontos) para todas as frentes.
        plt.scatter(xs, ys, label=f"Frente {idx + 1}", marker=marcador, color=cor, s=60)
    # Ajusta a legenda diretamente
    legenda = plt.legend()
    for texto in legenda.get_texts():
        texto.set_fontsize(120)
        texto.set_fontweight('bold')
    plt.title(f"Todas as Frentes Não Dominadas:\n Execução {execucao} Avaliação de Aptidão {aval_aptidao}", fontsize=fonte_legenda_size, fontweight='bold')
    plt.xlabel("Probabilidade\n de Bloqueio", fontsize=fonte_legenda_size, fontweight='bold')
    plt.ylabel("CAPEX", fontsize=fonte_legenda_size, fontweight='bold')
    plt.rc('legend', fontsize=18)  # Tamanho da fonte da legenda para o modal frente1, frente 2...
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # controle de largura da numeração dos eixos:
    plt.xticks(fontsize=ticks_size, fontweight='bold')
    plt.yticks(fontsize=ticks_size, fontweight='bold')
    plt.show()

    # Gráfico com apenas a primeira frente, com o mesmo estilo usado antes
    if frentes:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(xs, ys, color=cor_convergida, marker=marcador_convergido, s=60)

        ax.set_title(f"Frente Mais Convergida:\n Execução {execucao} Avaliação de Aptidão {aval_aptidao}",
                     fontsize=fonte_legenda_size, fontweight='bold')
        ax.set_xlabel("Probabilidade\n de Bloqueio", fontsize=fonte_legenda_size, fontweight='bold')
        ax.set_ylabel("CAPEX", fontsize=fonte_legenda_size, fontweight='bold')

        # Formatação dos ticks manualmente
        for label in ax.get_xticklabels():
            label.set_fontsize(ticks_size)
            label.set_fontweight('bold')

        for label in ax.get_yticklabels():
            label.set_fontsize(ticks_size)
            label.set_fontweight('bold')

        ax.grid(True)
        fig.tight_layout()
        plt.show()


