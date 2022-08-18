kmPorL = 12 
tempo = float(input('Qual o tempo da viagem: '))
speed = float(input('Qual a velocidade media do veiculo: '))

def calcCombustivel(kmPorL, tempo, speed): 
    distancia = tempo * speed
    litros = distancia / kmPorL
    print('Velocidade media: ', speed,'Tempo de viagem: ', tempo, 'Distancia total: ', distancia, 'Litros gastos: ', litros )

calcCombustivel(kmPorL, tempo, speed)
