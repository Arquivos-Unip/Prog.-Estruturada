# Para homens: (72.7*h) - 58
#     Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura em metros: "))
sexo = int(input("Qual o seu sexo? 1-Homem, 2-Mulher"))

def idealPeso(altura, sexo): 
    if(sexo == 1):
        ideal = (72.7* altura) - 58
        print("Seu peso ideal é: ", ideal)
    elif(sexo == 2):
        ideal = (62.1 * altura) - 44.7
        print("Seu peso ideal é: ", ideal)
    else: print("Sexo não existente")

idealPeso(altura, sexo)


