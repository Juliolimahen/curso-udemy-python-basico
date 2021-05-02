a = "Julio"
b = "Henrique"

#juntar strings 
concatenar = a + " " + b
print(concatenar)
#mastrar tamanho string
tamanho = len (concatenar)
print(tamanho)

#nevegação pelo indice
print (a[0])
print (a[1])
print (a[2])
print (a[3])
print (a[4])

#imprimir parte da string
print(concatenar[0:5])

#aplicando funcao/metodo, deixar minusculo 
print(concatenar.lower())

#aplicando funcao/metodo, deixar maiusculo
print(concatenar.upper())

print(concatenar)

concatenar = concatenar.upper()
print(concatenar)
#remover caracteres indesejados 
print(concatenar.strip())
#converter em lista
minha_string = "O rato roeu a roupa do rei de Roma "

print(minha_string)
minha_lista = minha_string.split()
print(minha_lista)

# busca de substring, rei
busca = minha_string.find("rei")

print(busca)

#substituir partes de uma string 
minha_string = minha_string.replace("o rei", " a rainha")
print(minha_string)