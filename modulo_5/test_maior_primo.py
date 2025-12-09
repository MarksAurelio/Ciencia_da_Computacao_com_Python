# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
def maior_primo(n):
    def eh_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(n, 1, -1):
        if eh_primo(i):
            return i

def test_maior_primo():
    assert maior_primo(10) == 7
    assert maior_primo(15) == 13
    assert maior_primo(2) == 2
    assert maior_primo(3) == 3
    assert maior_primo(20) == 19
    assert maior_primo(25) == 23
    assert maior_primo(30) == 29
    assert maior_primo(1_000) == 997
    assert maior_primo(1_001) == 997
    assert maior_primo(1_002) == 997
