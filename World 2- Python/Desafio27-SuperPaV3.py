termo= int(input('Primeiro termo:'))
razao= int(input('Razão:'))
primeiro=termo
contador=1
total=0
mais=10
while mais != 0:
    total+=mais
    while contador<=total:
        print(f'{primeiro} ⮕ ', end='')
        primeiro+=razao
        contador+=1

    mais= int(input('Você deseja mostrar mais quantos termos:'))
print(f'Total de termos {total}')
