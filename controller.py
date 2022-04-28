import models.LinkedList as LinkedList


lista = LinkedList()


def abrir_lista():
    return lista.__init__()


def registar_ao_inicio(data):
    return lista.insert_at_start(data)


def registar_no_final(data):
    return lista.insert_at_end(data)


def registar_pais_antes_de_outro(data, x):
    return lista.insert_after_item(data, x)


def registar_pais_depois_de_outro(data, x):
    return lista.insert_before_item(data, x)


def registar_pais_no_indice(data, index):
    return lista.insert_at_index(data, index)


def verificar_numero_de_elementos_na_lista():
    return lista.get_count()


def remover_primeiro_elemento():
    x = lista.start_node
    lista.delete_at_start()
    return x


def remover_ultimo_elemento():
    x = lista.get_last_node()
    lista.delete_at_end()
    return x


def verificar_pais(x):
    return lista.search_item(x)


def print_paises():
    lista.traverse_list()




