""" Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. """

# Imprime os n (número inteiro positivo) primeiros números ímpares
def numeros_impares(n):
    for i in range(1, n*2, 2): 
        print(i)

n = int(input('Digite o valor de n: '))

numeros_impares(n)
