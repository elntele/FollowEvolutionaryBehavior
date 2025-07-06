from core.file_loader import find_execution_files
from core.analysis import analisar_execucoes
from core.plotter import *

arquivos = find_execution_files(r'C:\Users\elnte\Desktop\result 24.6.25\CN-C+MN-C')
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
    "Média de soluções com restrição de conectividade algébrica por iteração",
    "Número de soluções com nós isolados",
    2, 21, 1, 100, [40, 200, 500, 1000]
)

plot_medias_por_iteracao(
    resumo['medias_qtd_sol_com_restri_equinad'],
    "Média de soluções com inadequação de equipamentos por geração",
    "Quantidade de soluções com restrição 2",
    2, 41, 1, 100, [80, 200, 500, 1000]
)

plot_tempo_execucao(
    resumo['tempos_execucao'],
    "Tempo de execução de cada uma das 30 execuções",
    "Tempo de execução (hh:mm:ss)",
    1, 31, 1,
    media=resumo["media_execucao_hhmmss"],
    desvio=resumo['std_execucao_hhmmss'],
    max_horas=20
)



plot_histograma(
    resumo['medias_de_valores_de_restr_eq_inadeq'],
    "Média da méria dos valores de restrição de inadequação de equipamentos a cada geração",
    "Valor médio de inadequação",
    max_y=0.6,
    inicio=200,
    fim=4000,
    passo=100,
    extras=[8000, 20000, 100000],
    usar_fitness=True
)


plot_histograma(
    resumo['std_da_media_dos_valores_de_restri_de_eq_inadeq'],
    "Média das 30 execuções do desvio padrão dos valores de restrição de inadequação de equipamentos a cada geração",
    "Desvio padrão da inadequação",
    max_y=0.12,
    inicio=2,
    fim=41,
    passo=1,
    extras=[80, 200, 1000]
)

plot_pareto(
    resumo['medias_pareto_solucoes'],
    resumo['pareto_frentes']
)
