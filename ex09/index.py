db = {}

i = 0

while(i != 4): 
    menu = int(input("O que você quer fazer?\n1. Inserir nova conta\n2. Selecionar conta\n3. Listar contas\n4. Sair\n"))
    if(menu == 1): 
        print('Sua opção: 1')
        cpf = int(input('Qual CPF?\n'))
        nome = input('Qual Nome?\n')
        valorInicial = float(input('Qual Valor Inicial?\n'))
        conta = {
            "cpf": cpf,
            "nome": nome,
            "total": valorInicial
        }
        db.update({cpf: conta})
        print("Conta cadastrada!")
    elif(menu == 2): 
        print('Sua opção: 2')
        cpfEscolhido = int(input('Qual CPF da conta?\n'))
        acaoEscolhida = int(input("O que você quer fazer?\n1. Sacar\n2. Depositar\n3. Sair menu conta\n"))
        contaEscolhida = db.get(cpfEscolhido)
        if(acaoEscolhida == 1):
            valorSacar = float(input("Quanto deseja sacar?\n"))
            if(contaEscolhida['total'] < valorSacar):
                print('Saldo insuficiente!')
            else:
                contaEscolhida['total'] = contaEscolhida['total'] - valorSacar
                print("Acão concluida!")
        elif(acaoEscolhida == 2):
            valorDepositar = float(input("Quanto deseja depositar?\n"))
            contaEscolhida['total'] = contaEscolhida['total'] + valorDepositar
            print("Acão concluida!")
    elif(menu == 3):
        print('Sua opção: 3')
        for i in db:
            item = db[i]
            print('CPF:', item['cpf'],'\nNome:', item['nome'],'\nTotal:',item['total'])
            print('--------------------')