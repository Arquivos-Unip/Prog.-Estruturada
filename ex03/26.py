maca = float(input("Qual a quantidade de maças compradas(em Kg): "))
morango = float(input("Qual a quantidade de morangos comprados(em Kg): "))


def valorMaça(maca):
    totalMaca = 0
    if(maca <= 5 or maca > 8):
        totalMaca = maca * 1.8
    elif(maca > 5 and maca <= 8):
        totalMaca = maca * 1.5
    return totalMaca

def valorMorango(morango):
    totalMorango = 0
    if(morango <= 5 or morango > 8):
        totalMorango = morango * 2.5
    elif(morango > 5 and morango <= 8):
        totalMorango = morango * 2.2
    return totalMorango

def valorTotal(macaPreço, morangoPreco, maca, morango):
    total = 0
    if(maca + morango > 8 or macaPreço + morangoPreco >= 25):
        total = (macaPreço + morangoPreco) - ((macaPreço + morangoPreco) * 0.1)
    else:
        total = macaPreço + morangoPreco
    return total

print("O valor total a ser pago é: ", valorTotal(valorMaça(maca), valorMorango(morango), maca, morango))

