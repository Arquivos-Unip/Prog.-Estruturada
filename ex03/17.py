from traceback import print_tb


ano = int(input("Digite um ano: "))

if (ano % 4 == 0):
    if(ano % 100 == 0):
        if(ano % 400 == 0):
            print("Ano bissexto")
        else:
            ("Nao é ano bissexto")
    else: 
        print("Ano bissexto")
else:
    print("Nao é ano bissexto")