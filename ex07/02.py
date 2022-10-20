# 2) Faça um programa que controle os estoque de 5 produtos em 5 armazéns de um
# supermercado, conforme figura abaixo:

# O programa deverá ler o número da linha e da coluna, correspondente ao produto no armazém, e
# a quantidade a ser retirada do estoque. Caso a quantidade solicitada for menor ou igual a
# quantidade em estoque, o programa deverá emitir uma mensagem de atendimento e dar baixa no
# estoque. Do contrário, emitir mensagem, "Estoque com quantidade insuficiente para atender ao
# pedido". O programa termina quando o número da linha for igual a -1. Utilize a declaração de
# matriz abaixo para resolver o exercício:



estoque = [[150,0,100,150,200], [200,300,230,100,90], [250,300,0,200,150], [300,100,90,450,0],
[350,300,400,250,200]]

i = 0
while(i != -1):
    print("Armazem 1:", estoque[0], "Armazem 2:", estoque[1],"Armazem 3:", estoque[2],"Armazem 4:", estoque[3],"Armazem 5:", estoque[4],)
    armazemEscolhido = int(input("Qual armazem gostaria de retirar o produto(1, 2, 3, 4, 5)?\n")) - 1
    produtoEscolhido = int(input("Qual produto gostaria de retirar do estoque(1, 2, 3, 4, 5)?\n")) - 1
    quantProduto = int(input("Qual a quantidade deseja?\n"))
    produto =  estoque[armazemEscolhido][produtoEscolhido]
    if(quantProduto > produto):
        print("ERROR: Quantidade indisponivel")
    else: 
        print("Produto comprado com sucesso!")
        estoque[armazemEscolhido][produtoEscolhido] = estoque[armazemEscolhido][produtoEscolhido] - quantProduto
    i = int(input('Caso deseje parar, digite "-1", para continuar digite outro numero.'))

