numero = int(input('Digite um numero:\n'))

def fatorial(numero):
    i = numero
    total = 1

    while(i > 0):
        total = total * i
        i = i - 1
    return total

print('O fatorial de', numero, 'é:', fatorial(numero))
