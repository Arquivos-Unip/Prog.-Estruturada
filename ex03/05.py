nota1 = float(input("Digita a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
mediaNum = ((nota1 + nota2) / 2 )

def media(media):
    if(media < 10 and media > 7):
        print("Aprovado")
    elif(media < 7):
        print("Reprovado")
    elif(media == 10):
        print("Aprovado com distinçao")
    else:
        print("Nota invalida")

media(mediaNum)