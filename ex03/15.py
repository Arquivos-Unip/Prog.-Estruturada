lado1 = float(input("Digite o primeiro lado do tringulo: "))
lado2 = float(input("Digite o segundo lado do triangulo: "))
lado3 = float(input("Digite o terceiro lado de um triangulo: "))

if((lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1):
    if((lado1 == lado2) and (lado1 == lado3)):
        print("Triangulo equilatero")
    elif((lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3)):
        print("Triangulo isoceles")
    elif((lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3)):
        print("Triangulo escaleno")
    else: 
        print("Valor invalido")
else:
    print("Não é um triangulo")