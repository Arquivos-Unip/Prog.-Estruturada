# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima? "
# d. "Devia para a vítima? "
# e. "Já trabalhou com a vítima? "

input("Responda as pergunta com sim ou nao, ok?")
telefonou = input("Telefonou para a vítima? ")
local = input("Esteve no local do crime? ")
morar = input("Mora perto da vítima? ")
divida = input("Devia para a vítima? ")
trabalhou = input("Já trabalhou com a vítima? ")

sim = 0

if(telefonou == 'sim'):
    sim = sim + 1
if(local == 'sim'):
    sim = sim + 1
if(morar == 'sim'):
    sim = sim + 1
if(divida == 'sim'):
    sim = sim + 1
if(trabalhou == 'sim'):
    sim = sim + 1

if(sim < 2):
    print("Inocente")
elif(sim == 2 ):
    print("Suspeita")
elif(sim == 3 or sim == 4):
    print("Cumplice")
elif(sim == 5):
    print("Assassino")
else:
    print("Valor invalido!")