""" Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista).  """
def remove_repetidos(lista):
    lista_sem_repetidos = []
    for numero in lista:
        if numero not in lista_sem_repetidos:
            lista_sem_repetidos.append(numero)
    lista_sem_repetidos.sort()
    return lista_sem_repetidos

def test_remove_repetidos():
    assert remove_repetidos([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_repetidos([5, 5, 5, 5, 5]) == [5]
    assert remove_repetidos([3, 1, 2, 3, 1]) == [1, 2, 3]
    assert remove_repetidos([]) == []
    assert remove_repetidos([10, -1, 0, -1, 10]) == [-1, 0, 10]
    