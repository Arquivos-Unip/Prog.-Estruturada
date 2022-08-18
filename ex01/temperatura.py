far = float(input('Digite a temperatura em Fahrenheit: '))
grau = 0

def farToGrau(far, grau):
    grau = (far - 32) * (5/9)
    return grau

print(farToGrau(far, grau))