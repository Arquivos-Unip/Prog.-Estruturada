import math

a = float(input("Digita o 'a' da equaçao: "))

if(a != 0):
    b = float(input("Digita o 'b' da equaçao: "))
    c = float(input("Digita o 'c' da equaçao: "))
    delta = (b ** 2) - (4 * a * c)
    if(delta < 0):
        print("Equaçao nao possui raizes reais")
    else:
        if(delta == 0):
            x1 = (-b / (2 * a))
            print("A equaçao possui apenas uma raiz por razao do delta ser igual a 0", "\nRaiz igual a: ", x1)
        else:
            x1 = ((-b + math.sqrt(delta)) / (2 *a))
            x2 = ((-b - math.sqrt(delta)) / (2 *a))
            print("As raizes da equaçao são: ", x1, "e", x2)
else:
    print("Valor invalido")