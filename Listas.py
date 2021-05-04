""" Listas: Representam um conjunto de dados
Pode ser: 
- Numérica: [1,2,3,4,5]
- Strings: ["bola", "sapato", "chuva"]
"""
minha_lista = ["abacaxi","melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.82, True]
#imprimindo indice da lista 
print(minha_lista[1])
#imprimindo lista completa 
print(minha_lista)
#imprimindo navegando por lista imprimindo intem por item 
for item in minha_lista:
    print(item)
#função len, para imprimir o tamanho da lista
tamanho = len(minha_lista)
print(tamanho)

#Adicicionando elementos a lista, metodo append
minha_lista.append("limao")
print(minha_lista)
if 7 in minha_lista2:
    print("7 esta na lista!")
else:
    print("não esta!")