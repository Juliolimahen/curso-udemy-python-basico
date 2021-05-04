# maneira "errada"
lista = ["abacate", "bola", "cachorro"]
# percorrer lista e imprimir valor e indice
for i in range(len(lista)):
    print(i, lista[i])

# Fuçao enumerate
for i, nome in enumerate(lista):
    print(i, nome)
