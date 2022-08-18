nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
provaInst = float(input('Nota da prova: '))
boletim = 0

def calcMedia(nota1, nota2, provaInst): 
     boletim = (nota1*0.3 + nota2 * 0.3 + provaInst * 0.4)
     return boletim

print(calcMedia(nota1, nota2, provaInst))


