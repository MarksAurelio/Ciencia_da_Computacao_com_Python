""" Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços. """
def desenhar_retangulo_vazio(largura, altura):
    for i in range(altura):
        for j in range(largura):
            if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
                print('#', end='')
            else:
                print(' ', end='')
        print()  # Muda para a próxima linha após imprimir uma linha completa do retângulo                

def test_desenhar_retangulo_vazio(capsys):
    desenhar_retangulo_vazio(4, 3)
    captured = capsys.readouterr()
    assert captured.out == "####\n#  #\n####\n"

    desenhar_retangulo_vazio(5, 4)
    captured = capsys.readouterr()
    assert captured.out == "#####\n#   #\n#   #\n#####\n"

    desenhar_retangulo_vazio(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "##\n##\n"
