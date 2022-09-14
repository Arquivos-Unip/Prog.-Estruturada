# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento
# iniciais. Valide a entrada e permita repetir a operação.

populacaoA = float(input("Qual a populaçao do pais de menos população:\n"))
taxaA = float(input("Qual a taxa de crescimento do pais A:\n"))
populacaoB = float(input("Qual a populaçao do pais de maior população:\n"))
taxaB = float(input("Qual a taxa de crescimento do pais B:\n"))

i = 0

while(populacaoA < populacaoB):
    populacaoA = populacaoA * (taxaA / 100)
    populacaoB = populacaoB * (taxaB / 100)
    i += 1

print("Serao necessarios", i, "anos para a populaçao A ser maior ou igual a populaçao de B")