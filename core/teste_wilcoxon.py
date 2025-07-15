import pandas as pd
from scipy.stats import wilcoxon
from io import StringIO

# Cole os dados diretamente aqui (com tabulação entre colunas)
dados = """
4000	0,7829	0,2881
8000	0,9405	0,2993
12000	0,9659	0,3031
16000	0,9837	0,3056
20000	0,9901	0,3077
24000	0,9918	0,3092
28000	0,9928	0,3103
32000	0,9936	0,3114
36000	0,9944	0,3124
40000	0,9948	0,3132
44000	0,9952	0,3138
48000	0,9956	0,3145
52000	0,9958	0,315
56000	0,996	0,3156
60000	0,9962	0,3161
64000	0,9964	0,3165
68000	0,9965	0,3169
72000	0,9967	0,3173
76000	0,9968	0,3177
80000	0,9968	0,318
84000	0,9969	0,3183
88000	0,9969	0,3186
92000	0,9969	0,3188
96000	0,997	0,319
100000	0,997	0,3193
"""

# Substitui vírgulas por pontos para conversão correta
dados = dados.replace(',', '.')

# Lê os dados como se fossem um arquivo .csv separado por tabulação
df = pd.read_csv(StringIO(dados), sep='\t', header=None)
df.columns = ['Indice', 'Abordagem1', 'Abordagem2']

# Aplica o teste de Wilcoxon
estatistica, pvalor = wilcoxon(df['Abordagem1'], df['Abordagem2'])

# Imprime o resultado
print(f"Estatística de Wilcoxon: {estatistica}")
print(f"P-valor: {pvalor}")
