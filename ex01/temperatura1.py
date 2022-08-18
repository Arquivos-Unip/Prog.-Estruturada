grau = float(input('Digite a temperatura em graus: '))
Fahrenheit = 0

def grauToFar(grau, far):
    far = grau * (9/5) + 32 
    return far

print(grauToFar(grau, Fahrenheit))