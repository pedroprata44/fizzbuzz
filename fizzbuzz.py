'''
Regras do jogo
1 - se a pos for multíplo de 3 fala fizz
2 - se a pos for multíplo de 5 fala buzz
3 - se a pos for multíplo de 3 e de 5 fala fizzbuzz'
4 - se não for multíplo de 3 e/ou 5 fala a posição
'''
from functools import partial

multiple_of = lambda base, num: num % base == 0

multiple_of_3 = partial(multiple_of,3)
multiple_of_5 = partial(multiple_of,5)

def robot(pos):

    if multiple_of_3(pos) and multiple_of_5(pos):
        return 'fizzbuzz'

    if multiple_of_5(pos):
        return 'buzz'

    if multiple_of_3(pos):
        return 'fizz'
    
    return str(pos)

 
if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'