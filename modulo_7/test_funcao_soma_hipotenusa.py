""" Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número. Em outras palavras, 
h
hh é uma hipotenusa se existem números inteiros 
i
ii e 
j
jj tais que:

h
2
=
i
2
+
j
2
h 
2
 =i 
2
 +j 
2
 h, squared, equals, i, squared, plus, j, squared

Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo 
n
nn e devolva a soma de todos os inteiros entre 1 e 
n
nn que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

DIca1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 1 até 
n
nn testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não. """
def eh_hipotenusa(h):
    for i in range(1, h):
        for j in range(i, h):  # Começa de i para evitar repetições
            if i * i + j * j == h * h:
                return True
    return False        

def soma_hipotenusas(n):
    soma = 0
    for h in range(1, n + 1):
        if eh_hipotenusa(h):
            soma += h
    return soma 

def test_soma_hipotenusas():
    assert soma_hipotenusas(5) == 5  # 5 é hipotenusa (3,4,5)
    assert soma_hipotenusas(10) == 15  # 5 e 10 são hipotenusas (6,8,10)
    assert soma_hipotenusas(13) == 28  # 5,10,13 são hipotenusas (5,12,13)
    assert soma_hipotenusas(1) == 0  # Nenhuma hipotenusa
    assert soma_hipotenusas(4) == 0  # Nenhuma hipotenusa
