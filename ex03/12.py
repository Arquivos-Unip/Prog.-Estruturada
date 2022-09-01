valHr = float(input("Qual o valor da hora trabalhada? "))
quantHr = float(input("Qual a quantidade de horas trabalhadas? "))
ir = 0
inss = 0.03
fgts = 0.11
salarioBruto = valHr * quantHr
def calcular(irCalculado):
    ir = irCalculado
    valorIr = salarioBruto * ir
    valorInss = salarioBruto * inss
    valorFgts = salarioBruto * fgts
    descontos = (valorIr + valorInss)
    salarioLiquido = salarioBruto - descontos
    print("Salario bruto(", valHr, '*', quantHr, "): ", "R$", salarioBruto,
        "\n(-) IR(", ir, "%): ", "R$", valorIr,
        "\n(-) INSS(", (inss * 100), "%): ", "R$", valorInss,
        "\nFGTS(11%): ", "R$", valorFgts,
        "\nTotal de descontos: ", "R$", descontos,
        "\nSalario liquido: ", salarioLiquido
    )
if(salarioBruto <= 900):
    calcular(0)
elif(salarioBruto > 900 and salarioBruto <=1500):
     calcular(0.05)
elif(salarioBruto > 1500 and salarioBruto <=2500):
     calcular(0.10)
elif(salarioBruto > 2500 ):
     calcular(0.20)