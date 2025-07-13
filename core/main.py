from core.file_loader import find_execution_files, ler_paretos
from core.analysis import analisar_execucoes, separa_frentes
from core.plotter import *

#arquivos = find_execution_files(r'C:\Users\elnte\Desktop\result 24.6.25\CN-C+MN-C')
arquivos = find_execution_files(r'C:\Users\elnte\Desktop\result 24.6.25\SBX_CROS+INTE_POL_MUT')
resumo = analisar_execucoes(arquivos)

print("Tempo médio de execução por abordagem (hh:mm:ss):", resumo['media_execucao_hhmmss'])
print("Desvio padrão do tempo de execução (hh:mm:ss):", resumo['std_execucao_hhmmss'])

print("Média de soluções com restrição de conectividade algébrica por iteração:")
print(resumo['medias_qtd_sol_com_restri_ca'])

print("Média de soluções com inadequação de equipamentos por iteração:")
print(resumo['medias_qtd_sol_com_restri_equinad'])

print("Média dos valores de inadequação de equipamentos por execução:")
print(resumo['medias_de_valores_de_restr_eq_inadeq'])

print("Desvio padrão dos valores de inadequação de equipamentos por execução:")
print(resumo['std_da_media_dos_valores_de_restri_de_eq_inadeq'])

print("Média de soluções presentes no primeiro conjunto de Pareto por iteração:")
print(resumo['medias_pareto_solucoes'])

print("Média de frentes de Pareto encontradas por iteração:")
print(resumo['pareto_frentes'])

plot_medias_por_iteracao(
    resumo['medias_qtd_sol_com_restri_ca'],
    "Média da quantidade de soluções com restrição de \n conectividade algébrica por marco de avaliação de aptidão",
    "Número de soluções\n com nós isolados",
    200, 2001, 100, 100,  extras=[8000, 20000, 100000],
    usar_fitness=True
)

plot_medias_por_iteracao(
    resumo['medias_qtd_sol_com_restri_equinad'],
    "Média de soluções com inadequação de equipamentos\n por marco de avaliação de aptidão",
    "Quantidade de soluções\n com restrição 2",
    200, 4001, 100, 100, [8000, 20000, 52000, 100000], True
)

plot_tempo_execucao(
    resumo['tempos_execucao'],
    "Tempo de execução de cada uma das 30 execuções",
    "Tempo de execução (dd:hh:mm:ss)",
    1, 31, 1,
    media=resumo["media_execucao_hhmmss"],
    desvio=resumo['std_execucao_hhmmss'],
    max_horas=20
)

plot_histograma(
    resumo['medias_de_valores_de_restr_eq_inadeq'],
    "Valor médio das 30 execuções da média dos valores restrição\n de inadequação de equipamentos das 100 soluções\n a cada marco de avaliação de aptidão",
    "Valor médio da média\n de inadequação\n nas 30 execuções",
    max_y=0.6,
    inicio=200,
    fim=4001,
    passo=100,
    extras=[8000, 20000, 100000],
    usar_fitness=True
)

plot_histograma(
    resumo['std_da_media_dos_valores_de_restri_de_eq_inadeq'],
    "Valor médio das 30 execuções do desvio\n padrão dos valores de restrição de inadequação\n de equipamentos a cada marco de avaliação de aptidão",
    "Valor médio do desvio\n padrão da inadequação\n de eqquipamentos\n nas 30 execuções",
    max_y=0.12,
    inicio=200,
    fim=4001,
    passo=100,
    extras=[8000, 20000, 100000],
    usar_fitness=True
)

plot_pareto(
    resumo['medias_pareto_solucoes'],
    resumo['pareto_frentes']
)

pathParetos = "C:/Users/elnte/Desktop/result 24.6.25/SBX_CROS+INTE_POL_MUT/VARSandFUNS/execution14/FUN1000.CSV"

try:
    # Etapa 1: Leitura do arquivo
    linhas = ler_paretos(pathParetos)

    # Etapa 2: Separação em frentes de Pareto
    frentes = separa_frentes(linhas)

    # Etapa 3: Plotagem dos gráficos
    plotar_frentes_pareto(frentes, pathParetos)

except FileNotFoundError:
    print(f"Arquivo {pathParetos} não encontrado. Pulando visualização de frentes.")
