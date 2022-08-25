hrTrab = float(input('Quantidade de horas trabalhadas? '))
valHr = float(input('Qual o valor da hora trabalhada? '))

def salario(hrTrab, valHr):
    impostoRenda = 11/100
    inss = 8/100
    sindicato = 5/100
    salBruto = hrTrab * valHr
    ir = salBruto * impostoRenda
    valorInss = salBruto * inss
    valorSind = salBruto * sindicato
    salLiquido = salBruto - (ir + valorInss + valorSind)
    print("O salario bruto é: ", salBruto, "\nO valor de imposto de renda pago é: ", ir, "\nO valor de inss pago é: ", valorInss, "\nO valor de sindicato pago é: ", valorSind, "\nO salario liquido é: ", salLiquido)

salario(hrTrab, valHr)

