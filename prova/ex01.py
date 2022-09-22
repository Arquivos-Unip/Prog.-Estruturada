# Crie um programa que receba e verifique se um número inteiro é positivo ou
# negativo. Caso seja positivo, mostrar se está
# entre as possibilidades abaixo:
# a) Menor do que 50.
# b) Entre 50 e 100.
# c) Maior do que 100.
# d) Qual é a média dos valores positivos entre 50 e 100.

total = 0
vezes = 0
i = 0
while(i < 10):
    numero = int(input('Digite um numero:\n'))
    if(numero >= 0): 
        positivoNegativo = 'positivo'
    else:
        positivoNegativo = 'negativo'


    if(positivoNegativo == 'positivo'):
        if(numero < 50):
            print("Numero é menor que 50")
        elif(numero >= 50 and numero <= 100):
            print("Numero entre 50 e 100.")
            total = total + numero
            vezes = vezes + 1

        elif(numero > 100):
            print("Numero é maior que 100")
        else:
            print("Numero inválido!!")

    i=i+1

print("A media é:", (total / vezes))






