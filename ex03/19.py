numero = int(input("Digite um numero menor q 1000: "))

numeroStr =str(numero)
if (numero > 1000):
    print("Numero invalido!")
else:
    centenas = (numero) // (10 ** (len(numeroStr)- 1))
    dezenas = ((numero - (centenas * 100)) // 10)
    unidade = ((numero - (centenas * 100)) - (dezenas * 10))
    print(numero, "= ", centenas, ' centenas, ', dezenas, " dezenas e", unidade, " unidades." )
