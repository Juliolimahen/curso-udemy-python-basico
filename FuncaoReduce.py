# funcao reduce
from functools import reduce


def soma(x, y):
    return x+y


lista = [1, 3, 5, 10, 20]
# obter a soma de todos os valores
#chmar funcao e a lista para obter a lista
soma = reduce(soma, lista)
print(soma)
