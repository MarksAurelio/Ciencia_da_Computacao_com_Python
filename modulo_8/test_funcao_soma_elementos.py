""" Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida. """
def soma_elementos(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

def test_soma_elementos():
    assert soma_elementos([1, 2, 3, 4, 5]) == 15
    assert soma_elementos([-1, -2, -3, -4, -5]) == -15
    assert soma_elementos([0, 0, 0, 0]) == 0
    assert soma_elementos([]) == 0
    assert soma_elementos([10, 20, 30]) == 60
    