import matplotlib.pyplot as plt
import numpy as np


def plot_medias_por_iteracao(dados, titulo, ylabel, inicio, fim, passo, max_y, extras=None):

    plt.figure(figsize=(12, 5))

    # Iterações desejadas no eixo X
    if extras is not None:
        iteracoes_desejadas = list(range(inicio, fim, passo)) + extras
    else:
        iteracoes_desejadas = list(range(inicio, fim, passo))

    valores = [dados.get(i, 0.0) for i in iteracoes_desejadas]
    categorias = [str(i) for i in iteracoes_desejadas]

    # Criação do gráfico de barras com largura ajustada
    plt.bar(categorias, valores, width=0.4)

    # Configurações de título e eixos
    plt.title(titulo, fontsize=18, fontweight='bold')
    plt.xlabel("Geração", fontsize=16, fontweight='bold')
    plt.ylabel(ylabel, fontsize=16, fontweight='bold')

    # Eixo Y: de 0 a max_y, com marcações de 5 em 5
    plt.yticks(np.arange(0, max_y + 5, 5))  # Garante que o max_y apareça

    # Grade e layout
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
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
#     plt.figure(figsize=(12, 5))
#
#     # Define os índices (categorias) para o eixo X
#     if fim is None:
#         fim = len(valores) + 1
#
#     if extras is not None:
#         iteracoes = list(range(inicio, fim, passo)) + extras
#     else:
#         iteracoes = list(range(inicio, fim, passo))
#
#     categorias = [str(i) for i in iteracoes]
#
#     if usar_fitness:
#         # Mostra os valores na ordem em que aparecem (sem indexar pela fitness)
#         yvalores = valores[:len(iteracoes)]
#     else:
#         # Indexa pela iteração normal
#         yvalores = [valores[i - 1] if 1 <= i <= len(valores) else 0.0 for i in iteracoes]
#
#     # Criação do gráfico
#     plt.bar(categorias, yvalores, width=0.4)
#
#     # Títulos e rótulos com estilo
#     plt.title(titulo, fontsize=14, fontweight='bold')
#     eixo_x = "Avaliação de aptidão" if usar_fitness else "Execução"
#     plt.xlabel(eixo_x, fontsize=12, fontweight='bold')
#     plt.ylabel(ylabel, fontsize=12, fontweight='bold')
#
#     # Eixo Y com intervalo adequado
#     plt.ylim(0, max_y)
#     plt.yticks(np.linspace(0, max_y, 6))
#
#     # Grade e layout
#     plt.grid(axis='y', linestyle='--', linewidth=0.5)
#     plt.tight_layout()
#     plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
# def formatar_expoente(valor: int) -> str:
#     if valor == 0:
#         return "0"
#
#     expoente = int(np.floor(np.log10(valor)))
#     base = valor / (10 ** expoente)
#
#     # Converte expoente para sobrescrito
#     expoente_formatado = ''.join({
#         '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
#         '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
#     }.get(c, '') for c in str(expoente))
#
#     # Formata a base com 1 casa decimal (e remove .0 se não for necessário)
#     base_str = f"{base:.1f}".rstrip('0').rstrip('.')
#     return f"{base_str}×10{expoente_formatado}"
#
#
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
#     plt.figure(figsize=(12, 5))
#
#     if fim is None:
#         fim = len(valores) + 1
#
#     extras = extras or []
#
#     # Gera os índices principais e extras
#     base_indices = list(range(inicio, fim + 1, passo))
#     all_indices = base_indices + extras
#
#     # Calcula yvalores corretamente
#     if usar_fitness:
#         yvalores = []
#         for i in all_indices:
#             if i in base_indices:
#                 idx = (i - inicio) // passo
#                 if 0 <= idx < len(valores):
#                     yvalores.append(valores[idx])
#                 else:
#                     yvalores.append(0.0)
#             else:
#                 yvalores.append(0.0)
#         categorias = [formatar_expoente(i) for i in all_indices]
#     else:
#         yvalores = [valores[i - 1] if 1 <= i <= len(valores) else 0.0 for i in all_indices]
#         categorias = [str(i) for i in all_indices]
#
#     # Criação do gráfico
#     plt.bar(categorias, yvalores, width=0.4)
#
#     # Aplica rotação nos rótulos do eixo X apenas para notação científica
#     if usar_fitness:
#         plt.xticks(rotation=45)
#
#     # Títulos e rótulos com estilo
#     plt.title(titulo, fontsize=14, fontweight='bold')
#     eixo_x = "Avaliação de aptidão" if usar_fitness else "Execução"
#     plt.xlabel(eixo_x, fontsize=12, fontweight='bold')
#     plt.ylabel(ylabel, fontsize=12, fontweight='bold')
#
#     plt.ylim(0, max_y)
#     plt.yticks(np.linspace(0, max_y, 6))
#
#     plt.grid(axis='y', linestyle='--', linewidth=0.5)
#     plt.tight_layout()
#     plt.show()

import matplotlib.pyplot as plt
import numpy as np

def plot_histograma(
    valores: list,
    titulo: str,
    ylabel: str,
    max_y: float = 100,
    inicio: int = 1,
    fim: int = None,
    passo: int = 1,
    extras: list = None,
    usar_fitness: bool = False
):
    plt.figure(figsize=(12, 5))

    if fim is None:
        fim = len(valores) + 1

    extras = extras or []
    base_indices = list(range(inicio, fim + 1, passo))
    all_indices = base_indices + extras

    if usar_fitness:
        yvalores = []
        for i in all_indices:
            if i in base_indices:
                idx = (i - inicio) // passo
                yvalores.append(valores[idx] if 0 <= idx < len(valores) else 0.0)
            else:
                yvalores.append(0.0)
        # Notação científica padrão com "e" (ex: 1e3)
        categorias = [format(i, '.1e').replace('.', ',').replace('e', 'E') for i in all_indices]

    else:
        yvalores = [valores[i - 1] if 1 <= i <= len(valores) else 0.0 for i in all_indices]
        categorias = [str(i) for i in all_indices]

    plt.bar(categorias, yvalores, width=0.4)

    # Rotação apenas se for em notação científica
    if usar_fitness:
        plt.xticks(rotation=45)

    plt.title(titulo, fontsize=14, fontweight='bold')
    eixo_x = "Avaliação de aptidão" if usar_fitness else "Execução"
    plt.xlabel(eixo_x, fontsize=12, fontweight='bold')
    plt.ylabel(ylabel, fontsize=12, fontweight='bold')
    plt.ylim(0, max_y)
    plt.yticks(np.linspace(0, max_y, 6))
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
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


from datetime import timedelta

def parse_tempo_em_timedelta(tempo_str):
    try:
        partes = tempo_str.split(":")
        if len(partes) == 3:
            horas, minutos, segundos = map(float, partes)
            return timedelta(hours=horas, minutes=minutos, seconds=segundos)
    except Exception as e:
        print(f"Erro ao converter tempo '{tempo_str}': {e}")
    return timedelta()

def plot_tempo_execucao(dados, titulo, ylabel, inicio, fim, passo, extras=None, media=0.0, desvio=0.0, max_horas=20):
    import matplotlib.pyplot as plt
    import numpy as np

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

    # Eixo Y: formatação como hh:mm:ss
    def format_hms(x, _):
        return str(timedelta(seconds=int(x)))

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_hms))
    plt.yticks(np.arange(0, max_horas * 3600 + 1, 3600))

    plt.title(titulo)
    plt.xlabel(f"Execuções: tempo médio = {media}, desvio padrão = {desvio}")
    plt.ylabel(ylabel)
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()



def plot_pareto(pareto_solucoes: dict, pareto_frentes: dict):
    iteracoes = list(pareto_solucoes.keys())

    plt.figure(figsize=(12, 5))
    plt.plot(iteracoes, list(pareto_solucoes.values()), label="Soluções no 1º Pareto")
    plt.plot(iteracoes, list(pareto_frentes.values()), label="Número de Frentes")

    plt.title("Evolução do Pareto", fontsize=14, fontweight='bold')
    plt.xlabel("Iteração", fontsize=12, fontweight='bold')
    plt.ylabel("Valor", fontsize=12, fontweight='bold')

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
