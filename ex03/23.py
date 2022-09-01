numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um numero: "))
operacao = int(input("Qual operaçao deseja fazer? (1- Soma, 2- Subtraçao, 3- Multiplicaçao, 4- Divisao"))
res = 0
parImpar = ''
positivoNegativo = ''
intDecimal = ''

def calcular(numero1, numero2, operaçao, res):
    if(operaçao == 1):
        res = numero1 + numero2
    elif(operaçao == 2):
        res = numero1 - numero2
    elif(operaçao == 3):
        res = numero1 * numero2
    elif(operaçao == 4):
        res = numero1 / numero2
    else:
        input("Valor invalido!")
    return res

valor = calcular(numero1,numero2, operacao, res)

if(valor % 2 == 0):
        parImpar = 'Par'
else:
        parImpar = 'Impar'

if(valor >= 0):
        positivoNegativo = 'Positivo'
else:
        positivoNegativo = 'Negativo'

if(valor % 1 ==0):
        intDecimal = 'Inteiro'
else:
        intDecimal = 'Decimal'


print("Resultado: ", valor, "\nEste Valor é:", parImpar, intDecimal,"e",positivoNegativo)