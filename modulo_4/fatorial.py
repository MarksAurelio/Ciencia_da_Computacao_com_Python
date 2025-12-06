# Escreva um programa que receba um número natural n na entrada
# e imprima n! (fatorial) na saída.

# Calcula o fatorial de um número natural
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Ler o número do usuário
numero = int(input("Digite o valor de n: "))

# Calcula e imprime o fatorial
resultado = fatorial(numero)
print(resultado)

# Outro exemplo usando while
numero = int(input("Digite o valor de n: "))
while numero >= 0:
    fatorial = 1
    while numero > 1:
        fatorial *= numero
        numero -= 1
    print(fatorial)   
