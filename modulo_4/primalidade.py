# Escreva um programa que receba um número inteiro positivo na entrada
# e verifique se é primo. Se o número for primo, imprima "primo".
# Caso contrário, imprima "não primo"

def numeroPrimo(numero):
    if numero == 0:
        return False
    elif numero <= 1:
        return False
    else:
        if numero % 2 == 0:
            return False
    return True

numero = int(input("Digite um número inteiro: "))

print("primo" if numeroPrimo(numero) else "não primo")
