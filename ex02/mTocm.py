metros = float(input("Digite a medida em metros: "))
centimetros = 0

def converter(metros, centimetros): 
    centimetros = metros * 1000
    return centimetros

print("A medida em centimetros é: ", converter(metros, centimetros))