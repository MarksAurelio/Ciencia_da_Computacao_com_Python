""" Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida. """
def maior_elemento(lista):
    if not lista:
        raise ValueError("A lista não pode ser vazia.")
    
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

def test_maior_elemento():
    assert maior_elemento([1, 2, 3, 4, 5]) == 5
    assert maior_elemento([-10, -20, -3, -4]) == -3
    assert maior_elemento([0, 0, 0, 0]) == 0
    assert maior_elemento([100]) == 100
    assert maior_elemento([3, 1, 4, 1, 5, 9, 2, 6, 5]) == 9
    