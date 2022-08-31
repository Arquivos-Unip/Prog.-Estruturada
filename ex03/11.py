from operator import indexOf


salario = float(input("Qual seu salario? "))

if(salario <= 280):
    percentual = 20
    aumento = salario * (percentual / 100)
    newSalario = salario + aumento
    print("O salario antes do reajuste era: ", salario, "\nO percentual do aumento foi de: ", percentual, "%", "\nO valor do aumento foi de: ", aumento, "\nO novo salario é: ", newSalario)
elif(salario > 280 and salario <= 700):
    percentual = 15
    aumento = salario * (percentual / 100)
    newSalario = salario + aumento
    print("O salario antes do reajuste era: ", salario, "\nO percentual do aumento foi de: ", percentual, "%", "\nO valor do aumento foi de: ", aumento, "\nO novo salario é: ", newSalario)
elif(salario > 700 and salario <= 1500):
    percentual = 10
    aumento = salario * (percentual / 100)
    newSalario = salario + aumento
    print("O salario antes do reajuste era: ", salario, "\nO percentual do aumento foi de: ", percentual, "%", "\nO valor do aumento foi de: ", aumento, "\nO novo salario é: ", newSalario)
elif(salario > 1500):
    percentual = 5
    aumento = salario * (percentual / 100)
    newSalario = salario + aumento
    print("O salario antes do reajuste era: ", salario, "\nO percentual do aumento foi de: ", percentual, "%", "\nO valor do aumento foi de: ", aumento, "\nO novo salario é: ", newSalario)
else:
    print("Valor invalido!")