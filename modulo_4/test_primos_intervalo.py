""" Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n). """
def primo(n):
    if n < 2:
        return False
    fator = 2
    while fator <= n // 2:
        if n % fator == 0:
            return False
        fator += 1
    return True 

def n_primos(n):
    count = 0
    for num in range(2, n + 1):
        if primo(num):
            count += 1
    return count

def test_n_primos():
    assert n_primos(2) == 1
    assert n_primos(3) == 2
    assert n_primos(10) == 4
    assert n_primos(20) == 8
    assert n_primos(1) == 0
    assert n_primos(30) == 10
