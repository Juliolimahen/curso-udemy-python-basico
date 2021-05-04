# maneira errada
def dobro(x):
    return x*2


valor = [1, 2, 3, 4, 5]

print(dobro(valor))

# map
valor_dobrado = map(dobro, valor)
# percorrer lista e pegar dobrado
for v in valor_dobrado:
    print(v)


valor_dobrado = map(dobro, valor)
# conveter em lista
valor_dobrado = list(valor_dobrado)

print(valor_dobrado)
