def TransformarDEC(num): 
    binario = ''
    while(num > 0): 
        binario = str(num % 2) + binario
        num = num // 2
    return binario

print(TransformarDEC(int(input('Digite um número: '))))

def TransformarBIN(num):
    decimal = 0
    expoente = 0
    while(num > 0):
        resto = num % 10
        decimal = decimal + resto * 2 ** expoente
        expoente = expoente + 1
        num = num // 10
    return decimal