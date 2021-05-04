# zip
lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$2,00", "R$1,00", "Não tem preço",
          "Não tem preço", "Não tem preço"]

# concatenar lista1 com a lista2
for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)
