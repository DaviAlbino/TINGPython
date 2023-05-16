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
    if instance.queue == []:
        return sys.stdout.write("Não há elementos\n")

    removed_queue = instance.dequeue()
    removed_q_name = removed_queue["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {removed_q_name} removido com sucesso\n")


def file_metadata(instance, position):
    if position >= 0 and position <= len(instance) - 1:
        return sys.stdout.write(str(instance.search(position)))
    else:
        return sys.stderr.write("Posição inválida")
