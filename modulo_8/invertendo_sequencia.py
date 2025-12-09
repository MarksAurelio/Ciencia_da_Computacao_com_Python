""" Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência. """
numeros = []
numero = int(input("Digite um número inteiro (0 para terminar): ")) 
while numero != 0:
    numeros.append(numero)
    numero = int(input("Digite um número inteiro (0 para terminar): "))     
    numeros_invertidos = numeros[::-1]
for num in numeros_invertidos:
    print(num)
