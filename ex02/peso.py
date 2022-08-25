altura = float(input("Digite sua altura em metros: "))

def idealPeso(altura): 
    ideal = (72.7* altura) - 58
    return ideal

print("Seu peso ideal é: ", idealPeso(altura))