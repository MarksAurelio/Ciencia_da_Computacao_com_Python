# Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.
def maximo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def test_maximo():
    assert maximo(3, 5, 2) == 5
    assert maximo(10, 2, 8) == 10
    assert maximo(-1, -5, -3) == -1
    assert maximo(0, 0, 0) == 0
    assert maximo(7, 7, 5) == 7
    assert maximo(4, 9, 9) == 9
    assert maximo(6, 6, 6) == 6
    assert maximo(-2, -1, -3) == -1
