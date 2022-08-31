produto1 = float(input("Digite o primeiro preço: "))
produto2 = float(input("Digite o segundo preço: "))
produto3 = float(input("Digite o terceiro preço: "))

if(produto1 < produto2 and produto1 < produto3):
    print("O produto mais barato é o ", produto1)
elif(produto2 < produto1 and produto2 < produto3):
    print("O produto mais barato é o ", produto2)
else:
    print("O produto mais barato é o de valor: ", produto3)