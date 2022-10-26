db = {}
total = 0

def calcTotal():
    global total
    for key in db:
        item = db[key]
        quantidade = item['quantidade']
        valor = item['valor']
        totalProduto = quantidade * valor
        total = total + totalProduto
        
for i in range (2):
    print("Cadastre o produto", (i + 1))
    registro = int(input("Digite o registro do produto:\n "))
    autor = input("Digite o autor do produto:\n")
    titulo = input("Digite o titulo do produto:\n")
    editora = input("Digite a editora do produto:\n")
    ano = int(input("Digite o ano do produto:\n "))
    quantidade = int(input("Digite a quantidade do produto:\n "))
    valor = float(input("Digite o valor do produto:\n "))
    item = {
        'registro': registro,
        'autor': autor,
        'titulo': titulo,
        'editora': editora,
        'ano': ano,
        'quantidade': quantidade,
        'valor': valor
    }
    db.update({registro: item})


menu = int(input("Qual opção desejada(1- Consutar item, 2- inventario, 3 - sair)?"))



while(menu != 3): 
    if(menu == 1):
        itemEscolhido = int(input("Digite o registro do produto desejado:\n "))
        if(db.__contains__(itemEscolhido)):
            print(db.get(itemEscolhido))
            menu = int(input("Qual opção desejada(1- Consutar item, 2- inventario, 3 - sair)?"))
        else:
            print("Produto não encontrado!")
            menu = int(input("Qual opção desejada(1- Consutar item, 2- inventario, 3 - sair)?"))

    elif(menu == 2):
        calcTotal()
        print(total)
        total = 0
        menu = int(input("Qual opção desejada(1- Consutar item, 2- inventario, 3 - sair)?"))
