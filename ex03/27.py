corte = input("Qual corte de carne voce vai querer(f- File Duplo, a- Alcatra, p- Picanha): ")
kilo = float(input("Qual a quantidade de carne voce vai querer(Em Kg): "))
pagamento = input("O pagamento sera com o cartao tabajara? ( sim ou nao)")
pagamentoEscolhido = 'dinheiro'
total = 0
corteEscolhido = ''
desconto = 0
newTotal = 0
if(corte == 'f'):
    corteEscolhido = 'File Duplo'
    if(kilo < 5):
        total = (kilo * 4.9)
    else:
        total = (kilo * 5.8)
elif(corte == 'a'):
    corteEscolhido = 'Alcatra'
    if(kilo < 5):
        total = (kilo * 5.9)
    else:
        total = (kilo * 6.8)
elif(corte == 'p'):
    corteEscolhido = 'Picanha'
    if(kilo < 5):
        total = (kilo * 6.9)
    else:
        total = (kilo * 7.8)
else:
    print("Operaçao invalida!")


if(pagamento == 'sim'):
    desconto = total * 0.05
    newTotal = total - desconto
    pagamentoEscolhido = 'Cartao tabajara'

print("Corte da carne comprada:", corteEscolhido, "\nQuantidade de carne comprada:", kilo, "\nPreço total:", total,"\nTipo de pagamento:", pagamentoEscolhido, "\nValor do desconto:", desconto, "\nValor a pagar:", newTotal)

