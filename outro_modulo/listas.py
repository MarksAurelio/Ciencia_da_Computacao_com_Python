n1 = [1, 2, 3, 4]
n2 = [1, 6, 6, 4]

valores = n1 + n2
print(valores)
print(type(valores))
valores[0] = 9
print(len(valores))
print(sorted(valores))
print(sorted(valores, reverse=True))
print(sum(valores))
print(min(valores))
print(max(valores))


valores.append(13) # acrescenta um elemento a lista
print(valores) 
valores.pop() # exclui um elemento da lista
print(valores)
valores.insert(3, 21)
print(valores)
print(17 in valores)

planetas = ['Mercúrio', 'Vėnus', 'Marte', 'Saturno', 'Urano', 'Netuno'] # [] ou list() para criar um lista vazia
for planeta in planetas:
    print(planeta)

# Crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas dele, 
# armazenando esses valores em uma lista. Na sequėncia, exiba na tela os elementos da lista em ordem 
# alfabética, um por linha, usando um laço de repetição for.

bebidas = []
for i in range(5):
    bebida = input('Digite uma bebida: ')
    bebidas.append(bebida)

bebidas.sort()

print('Bebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)
