numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um numero: "))
numero3 = float(input("Digite um numero: "))

if(numero1 > numero2 and numero1 > numero3):
    print("O maior numero é: ", numero1)
    if(numero2 > numero3): 
        print("O menor numero e: ", numero3)
    else:
        print("O menor numero é: ", numero2)
elif(numero2 > numero1 and numero2 > numero3):
    print("O maior numero é: ", numero2)
    if(numero1 > numero3): 
        print("O menor numero e: ", numero3)
    else:
        print("O menor numero é: ", numero1)
elif(numero3 > numero1 and numero3 > numero2):
    print("O maior numero é: ", numero3)
    if(numero1 > numero2): 
        print("O menor numero e: ", numero2)
    else:
        print("O menor numero é: ", numero1)
else:
    print("Operaçao invalida!")
