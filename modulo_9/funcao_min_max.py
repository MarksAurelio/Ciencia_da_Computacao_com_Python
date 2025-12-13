# Função min e max de números
def min_max_print(temperaturas):
    print("A menor temperatura é:", minimo(temperaturas),"C.")
    print("A maior temperatura é:", maxima(temperaturas),"C.")

def maxima(temperaturas):
    max = temperaturas[0]
    i = 1
    while i < len(temperaturas):
        if temperaturas[i] > max:
            max = temperaturas[i]
        i += 1
    return max

def minimo(temperaturas):
    min = temperaturas[0]
    i = 1
    while i < len(temperaturas):
        if temperaturas[i] < min:
            min = temperaturas[i]
        i += 1
    return min

def teste_pontual_maxima(temperaturas, valor_esperado):
    valor_calculado = maxima(temperaturas)
    if valor_calculado != valor_esperado:
        print("Teste falhou! Para o valor esperado", valor_esperado,"o valor calculado foi", valor_calculado)

def teste_pontual_minimo(temperaturas, valor_esperado):
    valor_calculado = minimo(temperaturas)
    if valor_calculado != valor_esperado:
        print("Teste falhou! Para o valor esperado", valor_esperado, "o valor calculado foi", valor_calculado)

def teste_minimo():
    print("Iniciando os testes de minimo...")
    teste_pontual_minimo([3, 5, 1, 4, 2], 1)
    teste_pontual_minimo([-10, -5, -1, -4, -2], -10)
    teste_pontual_minimo([0, 0, 0, 0], 0)
    print("Testes de minimo finalizados.")

def teste_maximo():
    print("Iniciando os testes de maximo...")
    teste_pontual_maxima([3, 5, 1, 4, 2], 5)
    teste_pontual_maxima([-10, -5, -1, -4, -2], -1)
    teste_pontual_maxima([0, 0, 0, 0], 0)
    print("Testes de maximo finalizados.")

if __name__ == "__main__":
    temperaturas = [23, 45, 12, 67, 34, 89, 2]
    min_max_print(temperaturas)
    teste_minimo()
    teste_maximo()
# Fim do programa