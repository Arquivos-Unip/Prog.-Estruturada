def compras():
    i = 0
    db = []
    total = 0
    print("Cadastre os produtos!")
    while (len(db) < 5):
        codigo = int(input("Qual o codigo do produto:\n"))
        nome = input("Qual o nome do produto:\n")
        preco = float(input("Qual o preço do produto:\n"))
        estoque = int(input('Qual a quantidade de produtos:\n'))
        produto = [codigo, nome, preco, estoque]
        db.append(produto)

    print("Produto 1:", 'Codigo:', db[0][0], '| Nome:', db[0][1], '| Preço:', db[0][2], '| Estoque:', db[0][3])
    print("\nProduto 2:", 'Codigo:', db[1][0], '| Nome:', db[1][1], '| Preço:', db[1][2], '| Estoque:', db[1][3])
    print("\nProduto 3:", 'Codigo:', db[2][0], '| Nome:', db[2][1], '| Preço:', db[2][2], '| Estoque:', db[2][3])
    print("\nProduto 4:", 'Codigo:', db[3][0], '| Nome:', db[3][1], '| Preço:', db[3][2], '| Estoque:', db[3][3])
    print("\nProduto 5:", 'Codigo:', db[4][0], '| Nome:', db[4][1], '| Preço:', db[4][2], '| Estoque:', db[4][3])

    while(i != -1):
        codigoProduto = float(input("Qual o codigo do produto que deseja comprar:\n"))
        produtoAtual = db[int(codigoProduto) - 1]
        if(codigoProduto != -1):
            quantidade = int(input("Qual a quantidade:\n"))
            if(produtoAtual[3] < quantidade):
                print('Quantidade indisponivel!\nTente Quantidades menores!')
            else:
                total += produtoAtual[2] * quantidade
                produtoAtual[3] = produtoAtual[3] - quantidade
                print("Produto comprado com sucesso")
        else:
            i = -1
            
    print("O total em reais da compra é:", total)

        
compras()