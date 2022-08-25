numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))
numeroReal = float(input("Digite um numero real: "))

def operaçoes(num1, num2, num3): 
    primeiraOpt = (num1 * 2) * (num2 / 2)
    secondOpt = (num1 * 3) + num3
    thirdOpt = (num3 ** 3)
    print(" A primeira operaçao resulta em: ", primeiraOpt)
    print(" A segunda operaçao resulta em: ", secondOpt)
    print(" A terceira operaçao resulta em: ", thirdOpt)

operaçoes(numero1, numero2, numeroReal)