import math
n1= 1
while n1 != 0:
    n1= int(input('Digite um valor:'))
    n2= math.factorial(n1)
    print(f'O fatorial de {n1} é {n2}')
print('Valor invalido')