
# if (numero > 1000):
#     print("Numero invalido!")
# else:
#     centenas = (numero) // (10 ** (len(numeroStr)- 1))
#     dezenas = ((numero - (centenas * 100)) // 10)
#     unidade = ((numero - (centenas * 100)) - (dezenas * 10))
#     print(numero, "= ", centenas, ' centenas, ', dezenas, " dezenas e", unidade, " unidades." )

numero = int(input("Digite um numero inteiro: "))
numeroInicial = numero
numeroStr = str(numero)
casas = len(numeroStr)
fragmentado = []

while(casas > 0):
    numeroFrag = (numero) // (10 ** (len(numeroStr)- 1))
    fragmentado.append(numeroFrag)
    numero = numero - (numeroFrag * (10 ** (len(numeroStr)- 1)))
    casas = casas - 1
    numeroStr = str(numero)

print("Numero digitado: ",numeroInicial,"\nNumero dividido em casas decimais: ",fragmentado)


