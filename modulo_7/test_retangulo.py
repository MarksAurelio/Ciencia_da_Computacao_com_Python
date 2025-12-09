""" Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída."""
def desenhar_retangulo(largura, altura):
    for i in range(altura):
        for j in range(largura):
            print('#', end='')
        print()  # Muda para a próxima linha após imprimir uma linha completa do retângulo      

if __name__ == "__main__":
    largura = int(input("Digite a largura do retângulo: "))
    altura = int(input("Digite a altura do retângulo: "))
    desenhar_retangulo(largura, altura) 

def test_desenhar_retangulo(capsys):
    desenhar_retangulo(4, 3)
    captured = capsys.readouterr()
    assert captured.out == "####\n####\n####\n"

    desenhar_retangulo(2, 5)
    captured = capsys.readouterr()
    assert captured.out == "##\n##\n##\n##\n##\n"

    desenhar_retangulo(1, 1)
    captured = capsys.readouterr()
    assert captured.out == "#\n"
