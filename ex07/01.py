i = 0
potenciaLista = [12, 15, 18, 20, 22]
def calcularConsumo(largura, comprimento, potencia):
    area = largura * comprimento 
    consumo = area * potenciaLista[potencia]
    return consumo

while(i != -1):
    largura = float(input('Qual a largura do quarto?\n'))
    comprimento = float(input('Qual o comprimento do quarto?\n'))
    tipoQuarto = int(input("Qual o tipo do quarto(0, 1, 2, 3, 4)?\n"))
    inf = {
        'largura': largura,
        'comprimento': comprimento,
        'tipoQuarto': tipoQuarto
    }
    consumo = calcularConsumo(largura, comprimento, (tipoQuarto))
    
    quantidadeLamp = consumo / 60
    if(quantidadeLamp % 1 == 0):
        total = quantidadeLamp
    else:
        total = (quantidadeLamp // 1) + 1
    print('A quantidade de lampada necessaria é:', total)
    i = int(input('Caso deseje parar, digite "-1", para continuar digite outro numero.'))