altura = float(input("Digite a altura do quadrado: "))
largura = float(input("Digite a largura do quadrado: "))

def calcArea(altura, largura):
    area = altura * largura;
    areaDobro = area * 2
    return areaDobro

print("O dobro da area é: ", calcArea(altura, largura))