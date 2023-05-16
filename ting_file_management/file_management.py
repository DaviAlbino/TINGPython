import sys


def txt_importer(path_file: str):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido")

    try:
        with open(path_file) as pf:
            rows = pf.read().split("\n")
            return rows
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
