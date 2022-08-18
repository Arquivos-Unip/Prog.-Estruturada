raio = float(input('Digite o raio: '))
altura = float(input('Digite a altura: '))
volume = 0

def calcVolume(raio, altura):
    volume = 3.14 * (raio **2) * altura
    return volume

print(calcVolume(raio, altura))
