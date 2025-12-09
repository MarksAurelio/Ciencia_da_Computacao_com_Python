# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
def vogal(caractere):
    vogais = 'aeiouAEIOU'
    return caractere in vogais  

def test_vogal():   
    assert vogal('a') == True
    assert vogal('e') == True
    assert vogal('i') == True
    assert vogal('o') == True
    assert vogal('u') == True
    assert vogal('A') == True
    assert vogal('E') == True
    assert vogal('I') == True
    assert vogal('O') == True
    assert vogal('U') == True
    assert vogal('b') == False
    assert vogal('c') == False
    assert vogal('d') == False
    assert vogal('f') == False
    assert vogal('g') == False
    assert vogal('B') == False
    assert vogal('C') == False
    assert vogal('D') == False
    assert vogal('F') == False
    assert vogal('G') == False
