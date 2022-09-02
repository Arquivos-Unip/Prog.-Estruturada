corte = input("Qual corte de carne voce vai querer(f- File Duplo, a- Alcatra, p- Picanha): ")
kilo = float(input("Qual a quantidade de carne voce vai querer(Em Kg): "))
pagamento = input("O pagamento sera com o cartao tabajara? ( sim ou nao)")
total = 0
corteEscolhido = ''
if(corte == 'f'):
    corteEscolhido = 'File Duplo'
    if(kilo > 5):
        total = (kilo * 4.9)
    else:
        total = (kilo * 5.8)
elif(corte == 'a'):
    corteEscolhido = 'Alcatra'
    if(kilo > 5):
        total = (kilo * 5.9)
    else:
        total = (kilo * 6.8)
elif(corte == 'p'):
    corteEscolhido = 'Picanha'
    if(kilo > 5):
        total = (kilo * 6.9)
    else:
        total = (kilo * 7.8)
else:
    print("Operaçao invalida!")



