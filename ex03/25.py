litros = float(input("Qual a quantidade de litros: "))
combustivel = input("Qual combustivel foi utilizado(a- Alcool, g- Gazolina): ")
preco = 0
if(combustivel == 'a'):
    if(litros <= 20):
        preco = (litros * 1.9) - ((litros * 0.03) * 1.9)
        print("O valor total:", preco)
    elif(litros > 20):
        preco = (litros * 1.9) - ((litros * 0.05) * 1.9)
        print("O valor total:", preco)
    else:
        print("Valor invalido")
elif(combustivel == 'g'):
    if(litros <= 20):
        preco = (litros * 2.5) - ((litros * 0.04) * 2.5)
        print("O valor total:", preco)
    elif(litros > 20):
        preco = (litros * 2.5) - ((litros * 0.06) * 2.5)
        print("O valor total:", preco)
    else: 
        print("Valor invalido!")
else:
    print('valor invalido')