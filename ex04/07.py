num1 = int(input("Digite um numero: \n"))
num2 = int(input("Digite um numero: \n"))
num3 = int(input("Digite um numero: \n"))
num4 = int(input("Digite um numero: \n"))
num5 = int(input("Digite um numero: \n"))

if(num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5):
    print('O maior numero é o 1')
elif(num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5):
    print('O maior numero é o 2')
elif(num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5):
    print('O maior numero é o 3')
elif(num4 > num1 and num4 > num3 and num4 > num2 and num4 > num5):
    print('O maior numero é o 4')
elif(num5 > num1 and num5 > num3 and num5 > num4 and num5 > num2):
    print('O maior numero é o 5')
