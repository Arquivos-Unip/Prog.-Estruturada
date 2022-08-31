numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))

def calcular(numero1, numero2): 
    if(numero1 / numero2 > 1):
        print("O maior numeor é o: ", numero1)
    elif(numero1 / numero2 < 1):
        print("O maior numero é o: ", numero2)
    else:
        print("Os numeros sao iguais!")

calcular(numero1, numero2)

