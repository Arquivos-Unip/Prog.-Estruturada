metrosQuadrados2= int(input("Qual a medida da area a ser pintada em m2: "))
metrosQuadrados2Str = str(metrosQuadrados2)
newMetrosQuadrados2 = metrosQuadrados2 * 1.1
preço18 = 80
preço36 = 25
coberturaLata18 = 108
coberturaLata36 = 21.6

156

if(newMetrosQuadrados2 <= coberturaLata36): print("É necessario apenas uma lata pequena\nO preço total é: ", preço36)
else:
    latasNecessarias36 = 0
    latasNecessarias18 = 0
    latasNecessarias18 = newMetrosQuadrados2 // 108
    latasNecessarias36 = (newMetrosQuadrados2 - (latasNecessarias18 * 108)) / 21.6
    if(latasNecessarias36 % 1 == 0):
        latasNecessarias36 = latasNecessarias36
    else:
        latasNecessarias36 = (latasNecessarias36 // 1) +1

total18 = latasNecessarias18 * preço18
total36 = latasNecessarias36 * preço36
total = total18 + total36
print("Serao necessarias:", latasNecessarias18,"lata(s) de 18L e", latasNecessarias36,"galão(s) de 3,6L","\nTotal a ser pago:",total )