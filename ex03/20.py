total = int(input("Qual o valor a ser sacado? "))

def saque(total):
    nota100 = (total // 100)
    total = total - (nota100 * 100)
    nota50 = (total // 50)
    total = total - (nota50 * 50)
    nota10 = (total // 10)
    total = total - (nota10 * 10)
    nota5 = (total // 5)
    total = total - (nota5 * 5)
    nota1 = (total // 1)
    total = total - (nota1 * 1)
    print(nota100, "Nota(s) de 100,", nota50, "Nota(s) de 50,", nota10, "Nota(s) de 10,", nota5, "Nota(s) de 5 e", nota1, "Nota(s) de 1")
    
saque(total)