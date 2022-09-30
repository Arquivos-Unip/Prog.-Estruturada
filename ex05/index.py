def calcularNumeroCaixa():
    lado1 = float(input('Qual a altura do retangulo(em metros):\n'))
    lado2 = float(input('Qual a largura do retangulo(em metros):\n'))

    quantidadeCaixa = float(input('Qual a quantidade (em m2) contida em uma caixa do material cerâmico escolhido:\n'))
    formaDeAplicacao = int(input('Qual a forma de aplicaçao(0 - paralela, ou 1 - diagonal aos lados do retângulo):\n'))

    custo = float(input("Qual o valor do material por m2:\n"))
    area = lado1 * lado2
    if(formaDeAplicacao == 0 ):
        acrescimo = 1.1
    else:
        acrescimo = 1.15
    
    numeroCaixa = (area / quantidadeCaixa) * acrescimo
    
    if((numeroCaixa // 1) == 0 ):
        numeroCaixa
    else:
        numeroCaixa = (numeroCaixa // 1) + 1

    preço = numeroCaixa * quantidadeCaixa *  custo

    print(numeroCaixa, preço)

calcularNumeroCaixa()