nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if(media >=9 and media <=10):
    conceito = 'A'
    print("A media do aluno foi: ", media, "\nO conceito foi: ", conceito, "\nO aluno foi aprovado")
elif(media >= 7.5 and media < 9):
    conceito = 'B'
    print("A media do aluno foi: ", media, "\nO conceito foi: ", conceito, "\nO aluno foi aprovado")
elif(media >= 6 and media < 7.5):
    conceito = 'C'
    print("A media do aluno foi: ", media, "\nO conceito foi: ", conceito, "\nO aluno foi aprovado")
elif(media >= 4 and media < 6):
    conceito = 'D'
    print("A media do aluno foi: ", media, "\nO conceito foi: ", conceito, "\nO aluno foi reprovado")
elif(media < 4):
    conceito = 'E'
    print("A media do aluno foi: ", media, "\nO conceito foi: ", conceito, "\nO aluno foi reprovado")
else:
    print("Valor invalido!")