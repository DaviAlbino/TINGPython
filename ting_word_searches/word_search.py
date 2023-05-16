def exists_word(word, instance):
    found_words = list()

    for index in range(len(instance)):
        all_files = instance.search(index)
        lines_with_word = list()

# ref enumerate: https://www.datacamp.com/tutorial/python-enumerate-tutorial

        for line_number, line in enumerate(all_files["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                lines_with_word.append({"linha": line_number + 1})

        if lines_with_word:
            result = {
                "palavra": word,
                "arquivo": all_files["nome_do_arquivo"],
                "ocorrencias": lines_with_word
            }
            found_words.append(result)

    return found_words


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
