hrTrab = float(input('Quantidade de horas trabalhadas? '))
valHr = float(input('Qual o valor da hora trabalhada? '))


def calcSalario(hrTrab, valHr): 
    salario = hrTrab * valHr
    return salario

print("O seu salario é: ", calcSalario(hrTrab, valHr))