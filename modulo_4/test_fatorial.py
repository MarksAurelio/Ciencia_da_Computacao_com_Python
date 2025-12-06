def fatorial(n):
    if n < 0:
        return 1
    i = fat = 1
    while i <= n:
        fat = fat * i
        i += 1      
    return fat

def test_fatorial():
    assert fatorial(5) == 120
    assert fatorial(4) == 24
    assert fatorial(3) == 6
    assert fatorial(2) == 2
    assert fatorial(1) == 1
    assert fatorial(0) == 1
    assert fatorial(6) == 720
    assert fatorial(7) == 5040
    assert fatorial(8) == 40320
    assert fatorial(9) == 362880
    assert fatorial(10) == 3628800
    assert fatorial(-10) == 1