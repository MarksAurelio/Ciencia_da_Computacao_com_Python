# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.
def maximo(a, b):
    if a > b:
        return a
    else:
        return b    

def test_maximo():
    assert maximo(3, 5) == 5
    assert maximo(10, 2) == 10
    assert maximo(-1, -5) == -1
    assert maximo(0, 0) == 0
    assert maximo(7, 7) == 7        
