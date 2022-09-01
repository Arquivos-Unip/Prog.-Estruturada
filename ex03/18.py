from datetime import datetime
 
data = input("Digite uma data(dd/mm/aaaa): ")
 
formato = "%d/%m/%Y"

res = False
try:
    res = bool(datetime.strptime(data, formato)) #compara a variavel data com o formato passado, se for verdadeiro, printa
    print('Formato valido!')
except:
    print("Formato invalido!")