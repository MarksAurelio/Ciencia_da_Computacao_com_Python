# Escreva um programa que receba um número inteiro na entrada,
# calcule e imprima a soma dos dígitos deste número na saída.

# função que calcula a soma dos dígitos de um número inteiro
def soma_digitos_numero(numero):
    soma = 0 # o 0 é número de inicializacão
    while numero > 0: # enquanto o número maior que 0
        digito = numero % 10 # pega último dígito (1, 2, 3, 4, ...9, 10)
        soma += digito
        numero //= 10 # apaga o último dígito (1, 2, 3, 4, ...9, 10)
    return soma # retorna a soma dos dígitos do número

numero = int(input("Digite um número inteiro: "))

resultado = soma_digitos_numero(numero)
print(resultado)
