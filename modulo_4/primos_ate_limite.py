def primo (n):
    fator = 2
    if n == 2:
        return True
    
    while n % fator != 0 and fator <= n // 2:
        fator += 1
    if n % fator == 0:
        return False
    else:
        return True
    
limite = int(input("Digite o limite superior: "))

n = 2
while n <= limite:
    if primo(n):
        print(n, end= ', ')
    n += 1
