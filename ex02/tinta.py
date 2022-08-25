metrosQuadrados = float(input("Qual a medida da area a ser pintada em m2: "))

def latasTinta(metrosQuadrados): 
    preço = 80
    coberturaLata = 54
    if(metrosQuadrados > coberturaLata):
        latasNecessarias = (metrosQuadrados // coberturaLata) + 1
        print("Serao necessarias ", latasNecessarias, "latas", "\nO preço total é: ", (latasNecessarias * preço))
    else: print("Sera necessario apenas 1 lata \nO preço total é: 80")
    
latasTinta(metrosQuadrados)
