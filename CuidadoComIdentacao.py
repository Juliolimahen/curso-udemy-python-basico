x = 1 
y = 2

if x == y:
    print("numeros iguais")
elif x < y:
    print("x menor que y")
    if x%2==0:
        print("x é par!")
    else:
        print(" x é impar")
elif y < x:
    print("y maior que x")
    if y%2==0:
        print("y é par!")
    else:
        print(" y é impar")
else: 
    print("numeros diferentes ")