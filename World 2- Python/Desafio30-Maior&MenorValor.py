n='S'
n1=0
soma=0
contagem= 0
maior=menor= 0
while n != 'N':
    n1= int(input('Digite um valor:'))
    n= str(input('Você deseja continuar? [S/N]')).upper().strip()[0]
    soma+=n1
    contagem+=1
    if contagem ==1:
        maior=menor=n1
    else:
        if n1> maior:
            maior=n1
        if n1<maior:
            menor=n1

media= soma / contagem
print(f'A soma de todos os número é {soma} e a média é {media:.1f}')
print(f'O maior número é {maior} e o menor numero é {menor}!')