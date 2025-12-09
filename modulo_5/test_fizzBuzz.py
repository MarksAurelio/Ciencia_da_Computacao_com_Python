# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve
""" 'Fizz' se o número for divisível por 3 e não for divisível por 5;

'Buzz' se o número for divisível por 5 e não for divisível por 3;

'FizzBuzz' se o número for divisível por 3 e por 5;

Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro. """
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n
    
def test_fizzbuzz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(7) == 7
    assert fizzbuzz(9) == 'Fizz'
    assert fizzbuzz(10) == 'Buzz'
    assert fizzbuzz(30) == 'FizzBuzz'
    assert fizzbuzz(22) == 22
    assert fizzbuzz(33) == 'Fizz'
