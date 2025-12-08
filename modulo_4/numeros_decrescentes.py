""" Escreva um programa que receba uma sequência de números inteiros na entrada, um por vez, até que o número 0 seja lido. O programa deve verificar se os números lidos estão em ordem decrescente. Se estiverem, imprima "A sequência de números está em ordem decrescente!". Caso contrário, imprima "A sequência de números não está em ordem decrescente!". """
decrescente = True
numero = int(input("Digite o primeiro número da sequência: "))
proximoNumero = int(input("Digite o próximo número da sequência: "))

while proximoNumero != 0 and decrescente:
    if proximoNumero > numero:
        decrescente = False
        numero = proximoNumero

if decrescente:
    print("A sequência de números está em ordem decrescente!")
else:
    print("A sequência de números não está em ordem decrescente!")
