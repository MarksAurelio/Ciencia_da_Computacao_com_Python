from modulo_6.test_jogo_do_NIM import computador_escolhe_jogada

def test_computador_move_to_multiple():
    assert computador_escolhe_jogada(5, 3) == 1   # deixa 4 (m+1)
    assert computador_escolhe_jogada(7, 3) == 3   # deixa 4

def test_computador_uses_max_when_no_escape():
    assert computador_escolhe_jogada(4, 3) == 3   # nenhum j em 1..3 deixa múltiplo, usa max
    assert computador_escolhe_jogada(8, 3) == 3

def test_computador_handles_small_piles():
    assert computador_escolhe_jogada(2, 3) == 2
    assert computador_escolhe_jogada(1, 3) == 1
""" **** Simulação de um campeonato de Jogo do NIM **** """