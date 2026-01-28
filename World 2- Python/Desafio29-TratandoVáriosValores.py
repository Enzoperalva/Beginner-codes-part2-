
cont=0
soma=0
n1= int(input('DIgite um número inteiro [999 para parar]:'))
while n1 !=999:
    soma+=n1
    cont+=1
    n1 = int(input('DIgite um número inteiro [999 para parar]:'))
print(f'Você digitou {cont} números e a soma entre eles é {soma}')