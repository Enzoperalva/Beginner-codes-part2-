termo= int(input('Primeiro termo:'))
razao= int(input('Razão:'))
primeiro=termo
contador=1

while contador<=10:
    print(f'{primeiro} ⮕ ', end='')
    primeiro+=razao
    contador+=1
print('FIM')
