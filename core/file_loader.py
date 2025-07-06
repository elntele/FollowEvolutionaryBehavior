import os
import re

def find_execution_files(base_path):
    """
    Percorre as subpastas da pasta base e localiza arquivos printExecution*.txt em execution*.
    Retorna lista de caminhos completos.
    """
    execution_files = []

    # Verifica se o caminho existe
    if not os.path.isdir(base_path):
        raise FileNotFoundError(f"Caminho inválido: {base_path}")

    # Itera sobre pastas como execution1, execution2, etc.
    for folder in sorted(os.listdir(base_path)):
        full_folder_path = os.path.join(base_path, folder)
        if os.path.isdir(full_folder_path) and re.match(r'^execution\d+$', folder):
            for filename in os.listdir(full_folder_path):
                if re.match(r'^printExecution\d+\.txt$', filename):
                    execution_files.append(os.path.join(full_folder_path, filename))

    if not execution_files:
        raise FileNotFoundError("Nenhum arquivo printExecution*.txt encontrado nas subpastas.")

    return execution_files
