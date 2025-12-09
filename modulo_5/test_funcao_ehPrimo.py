# Função que verifica se um número é primo
def EhPrimo (x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x // 2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True

def test_EhPrimo():
    assert EhPrimo(2) == True
    assert EhPrimo(3) == True
    assert EhPrimo(4) == False
    assert EhPrimo(5) == True
    assert EhPrimo(10) == False
    assert EhPrimo(13) == True
    assert EhPrimo(25) == False
    assert EhPrimo(29) == True
    assert EhPrimo(50) == False
    assert EhPrimo(97) == True
