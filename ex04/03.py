# Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v', 'd';

nome = input("Insira seu nome:\n")
idade = int(input("Insira sua idade:\n"))
salario = float(input("Insira seu salario:\n"))
sexo = input("Insira seu sexo(f - feminino, m - Masculino:\n")
estadoCivil = input("Insira seu estado civil('s', 'c', 'v', 'd'):\n")

if(len(nome)> 3):
    print("Nome validado")
else: 
    print("Nome invalido!")

if(idade > 0 and idade < 150):
    print("Idade validada")
else:
        print("Idade invalida!")

if(salario > 0):
    print("Salario validado")
else:
    print("Salario invalido!")

if(sexo == 'f' or sexo == 'm'):
    print("sexoe validado")
else:
    print("Sexo invalido")

if(estadoCivil in ("s" or "c"or "v" or "d")):
    print("Estado civil valido!")
else:
    print('Estado civil invalido!')