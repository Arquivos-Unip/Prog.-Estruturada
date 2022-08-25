# 12) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivoMb = float(input("Qual o tamanho do arquivo em mb: "))
velocidade = float(input("Qual a velocidade em mbps: "))

def tempo(arquivoMb, velocidade): 
    tempoSeg = arquivoMb / velocidade
    tempoMin = tempoSeg / 60
    return tempoMin

print("O tempo de download em minutos é: ", tempo(arquivoMb, velocidade))

