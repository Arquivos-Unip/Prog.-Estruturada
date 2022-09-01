maca = float(input("Qual a quantidade de maças compradas(em Kg): "))
morango = float(input("Qual a quantidade de morangos comprados(em Kg): "))


def valorMaça(maca):
    totalMaca = 0
    if(maca >= 5):
        totalMaca = maca * 1.8
    elif(maca > 5 and maca <= 8):
        totalMaca = maca * 1.5
    else:
        print("Valor invalido") 
    return totalMaca

def valorMorango(morango):
    totalMorango = 0
    if(morango >= 5):
        totalMorango = morango * 2.2
    elif(morango > 5 and morango <= 8):
        totalMorango = morango * 1.5
    else:
        print("Valor invalido")
    return totalMorango

def valorTotal(maca, morango):
    total = 0
    if(maca + morango > 8 or maca + morango >= 12):
        total = (maca + morango) - ((maca + morango) * 0.1)
    else:
        total = maca + morango
    return total

print("O valor total a ser pago é: ", valorTotal(valorMaça(maca), valorMorango(morango)))