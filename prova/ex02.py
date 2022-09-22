# Crie um programa que calcule o rendimento do dia de um hotel.
# Primeiramente, o programa deve solicitar ao usuário, a quantidade de quartos
# ocupados, o valor da diária para quartos simples e para quartos duplo e o valor do
# serviço de alarme.
# Para cada quarto ocupado, o programa deverá solicitar:
# • qual é o tipo de quarto ocupado (sugestão: valor 1 para Simples, valor 2 para
# duplo)
# • qual foi a quantidade de serviços de alarme solicitada.
# • qual foi o valor consumido no quarto. Se o valor de consumo for acima de 50%
# do valor pago por hospedagem, o programa deve dar um desconto de 10% no
# total do quarto, se for acima de 75% o desconto é de 20% e, por fim, se for
# acima de 90% o desconto deve ser de 25%.
# No fim da execução, o programa deve apresentar qual é o total de rendimento do
# hotel, o total bruto de cada quarto (sem desconto), o desconto dado para o quarto e o
# valor líquido do quarto (com desconto).

quartoOcupado = int(input('Digite a quantidade de quartos ocupados:\n'))
quartoSimples = float(input('Digite o valor da diária do quarto simples:\n'))
quartoDuplo = float(input('Digite o valor da diária do quarto duplo:\n'))
alarme = float(input('Digite o valor do serviço de alarme:\n'))
totalHotel = 0

for i in range(quartoOcupado):
    tipoQuarto = int(input('Digite o tipo do quarto(1 - simples, 2 - duplo):\n'))
    alarmeQuarto = int(input('Digite a quantidade de serviços de alarme solicitada:\n'))
    valorConsumo = float(input('Digite o valor consumido no quarto:\n'))
    if(tipoQuarto == 1):
        valorQuarto = quartoSimples
    else:
        valorQuarto = quartoDuplo

    if(valorConsumo > (valorQuarto * 0.50) and valorConsumo <= (valorQuarto * 0.75)):
        desconto = 0.10
    elif(valorConsumo > (valorQuarto * 0.75) and valorConsumo <= (valorQuarto * 0.90)):
        desconto = 0.20
    elif(valorConsumo > (valorQuarto * 0.90)):
        desconto = 0.25
    else:
        desconto = 0



    valorTotal = (valorQuarto + (alarmeQuarto * alarme) + valorConsumo) - ((valorQuarto + (alarmeQuarto * alarme) + valorConsumo) * desconto)
    totalHotel = totalHotel + valorTotal
    print("Valor total do quarto: ", valorTotal)
    print("Valor bruto do quarto: ", valorQuarto + (alarmeQuarto * alarme) + valorConsumo)
    print("Desconto do quarto: ", ((valorQuarto + (alarmeQuarto * alarme) + valorConsumo) * desconto))

print("\n\n\nTotal de rendimento do hotel: ", totalHotel)
