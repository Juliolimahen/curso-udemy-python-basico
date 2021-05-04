import random
#forçar a escolher sempre o mesmo numero
#random.seed(1)
#escoler um numero aleatório de 0 a 10
lista=[4,9,69]
#metodo choice escolher numero aleatorio de uma lista
numero = random.choice(lista)
print(numero)
numero = random.randint(0,10)
print(numero)