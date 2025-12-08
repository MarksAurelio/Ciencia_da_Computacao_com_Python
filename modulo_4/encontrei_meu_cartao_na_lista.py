""" Escreva um programa que receba o número do seu cartão de crédito na entrada e, em seguida, uma sequência de números de cartões de crédito (um por vez) até que o número 0 seja lido. O programa deve verificar se o número do seu cartão de crédito está entre os números lidos. Se estiver, imprima "Eba!!! Meu cartão está lá!". Caso contrário, imprima "Xi, meu cartão não está lá...". """
meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaoLido = None
encontreiMeuCartaoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartaoNaLista:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
    print("Eba!!! Meu cartão está lá!")
else:
    print("Xi, meu cartão não está lá...")
