metrosQuadrados2= float(input("Qual a medida da area a ser pintada em m2: "))

def latasTinta2(metrosQuadrados2): 
    preço18 = 80
    preço36 = 25
    coberturaLata18 = 108
    coberturaLata36 = 21.6
    if(metrosQuadrados2 <= coberturaLata36): print("É necessario apenas uma lata pequena\nO preço total é: ", preço36)
    else:
        latasNecessarias36 = (metrosQuadrados2 // coberturaLata36) + 1
        latasNecessarias18 = (metrosQuadrados2 // coberturaLata18) + 1
        print("Serao necessarias ", latasNecessarias36, " latas de 3,6L", "\nO preço total é: ", (latasNecessarias36 * preço36))
        print("\nSerao necessarias: ", latasNecessarias18, "\nO preço total é: ", preço18)


latasTinta2(metrosQuadrados2)