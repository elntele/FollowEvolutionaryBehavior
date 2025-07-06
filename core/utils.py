import os

def coletar_arquivos_de_execucao():
    base_dir = input("Digite o caminho da pasta base (com execuções): ").strip()
    arquivos = []
    for i in range(1, 31):
        path = os.path.join(base_dir, f"execution{i}", f"printExecution{i}.txt")
        arquivos.append(path)
    return arquivos
