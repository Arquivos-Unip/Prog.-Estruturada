numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))

def trocarValor(numero1, numero2):
    newNumero1 = numero2
    newNumero2 = numero1
    print('O valor do numero 1 era: ', numero1, " e virou: ", newNumero1)
    print('O valor do numero 2 era: ', numero2, " e virou: ", newNumero2)

trocarValor(numero1, numero2)