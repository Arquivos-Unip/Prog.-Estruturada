hrAula = float(input('Qual o valor da hora aula? '))
nmrAulas = float(input('Quantas aulas dadas no mes? '))
inss = float(input('Qual o desconto do INSS? '))

def calcSalario(hrAula, nmrAulas, inss): 
    salarioBruto = hrAula * nmrAulas
    salarioLiquido = salarioBruto * (1 + (inss / 100))
    return salarioLiquido

print(calcSalario(hrAula, nmrAulas, inss))