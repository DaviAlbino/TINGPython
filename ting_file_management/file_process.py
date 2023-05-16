from ting_file_management.file_management import txt_importer
# from queue import Queue
import sys


def process(path_file, instance):
    my_txts = txt_importer(path_file)
    outcome = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(my_txts),
        "linhas_do_arquivo": my_txts,
    }
    for que_index in range(len(instance)):
        if instance.search(que_index)["nome_do_arquivo"] == path_file:
            return None

    outcome_str = str(outcome)

    instance.enqueue(outcome)
    return sys.stdout.write(outcome_str)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
