import re
import numpy as np

def parse_execution_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = {
        'execution_time_ms': None,
        'iterations': [],        # Lista de métricas por iteração
        'pareto': {},            # {interação: (n_soluções, n_frentes)}
        'restricoes_por_no': {} # {interação: [valores por nó]}
    }

    for line in lines:
        line = line.strip()

        # Tempo total de execução
        if line.startswith("Total execution time:"):
            match = re.search(r"(\d+)ms", line)
            if match:
                data['execution_time_ms'] = int(match.group(1))

        # Métricas por iteração
        elif line.startswith("iteration:"):
            match = re.search(
                r"iteration:\s*(\d+);\s*ca0Rest1:\s*(\d+);\s*eqInadRest2:\s*(\d+);\s*medianrest2:\s*([\d,NaN]+);\s*StdRest2:\s*([\d,NaN]+)",
                line
            )
            if match:
                iteration = int(match.group(1))
                ca0 = int(match.group(2))
                eq2 = int(match.group(3))

                median_raw = match.group(4).replace(',', '.')
                std_raw = match.group(5).replace(',', '.')

                try:
                    median = float(median_raw)
                except ValueError:
                    median = 0.0

                try:
                    std = float(std_raw)
                    if np.isnan(std):
                        std = 0.0
                except ValueError:
                    std = 0.0

                data['iterations'].append({
                    'iteration': iteration,
                    'ca0Rest1': ca0,
                    'eqInadRest2': eq2,
                    'medianrest2': median,
                    'stdrest2': std
                })

        # Informações de Pareto
        elif "numero de soluções no primeiro pareto" in line:
            match = re.search(r"interação:\s*(\d+);\s*numero de soluções no primeiro pareto:\s*(\d+);\s*numero de paretos:\s*(\d+)", line)
            if match:
                data['pareto'][int(match.group(1))] = (
                    int(match.group(2)),  # soluções no primeiro pareto
                    int(match.group(3))   # número de frentes
                )

        # Restrições por nó
        elif "Nós versus qtd de soluções com restrição" in line:
            match = re.search(r"interação:\s*(\d+);\s*Nós versus qtd de soluções com restrição:\s*\[([^\]]+)\]", line)
            if match:
                iteration = int(match.group(1))
                restricoes = list(map(int, match.group(2).split(',')))
                data['restricoes_por_no'][iteration] = restricoes

    return data
