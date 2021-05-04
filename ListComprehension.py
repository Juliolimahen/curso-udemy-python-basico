#list comprehesion 
#maneira tradicinal
x = [1,2,3,4,5]
y = []

for i in x:
    y.append(i**2)
print(x)
print(y)

#list comprehesion 
x=[1,2,3,4,5]
#sintaxe
#y=[valor_a_adicionar laço condição]
y = [i**2 for i in x]
#numeros impares
z =[i for i in x if i%2==0]

print(x)
print(y)
print(z)
