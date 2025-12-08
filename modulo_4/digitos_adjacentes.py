""" Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não". """
def adjacentes(numero):
    numero = str(numero)
    for i in range(len(numero)-1):
        if numero[i] == numero[i+1]:
            return True
    return False

numero = int(input('Digite um número inteiro: '))

print('sim' if adjacentes(numero) else 'não')
