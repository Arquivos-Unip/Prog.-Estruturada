i = 0
def calcularConsumo(largura, comprimento, potencia):
    area = largura * comprimento 
    consumo = area * potencia
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
    if(inf.get('tipoQuarto') == 0 ): 
        consumo = calcularConsumo(inf.get('largura'), inf.get('comprimento'), 12)
    elif(inf.get('tipoQuarto') == 1 ): 
        consumo = calcularConsumo(inf.get('largura'), inf.get('comprimento'), 15)
    elif(inf.get('tipoQuarto') == 2 ): 
        consumo = calcularConsumo(inf.get('largura'), inf.get('comprimento'), 18)
    elif(inf.get('tipoQuarto') == 3 ): 
        consumo = calcularConsumo(inf.get('largura'), inf.get('comprimento'), 20)
    elif(inf.get('tipoQuarto') == 4 ): 
        consumo = calcularConsumo(inf.get('largura'), inf.get('comprimento'), 22)
    else:
        print('Numero Invalido')
    quantidadeLamp = consumo / 60
    if(quantidadeLamp % 1 == 0):
        total = quantidadeLamp
    else:
        total = (quantidadeLamp // 1) + 1
    print('A quantidade de lampada necessaria é:', total)
    i = int(input('Caso deseje parar, digite "-1", para continuar digite outro numero.'))
