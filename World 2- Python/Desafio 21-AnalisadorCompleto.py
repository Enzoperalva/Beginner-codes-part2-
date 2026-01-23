from time import sleep
somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=0
mulher20=0
for c in range(1,5):
    print(f'{c}° Pessoa!')
    n1= str(input('NOME:')).strip()
    n2= int(input('IDADE:'))
    n3= str(input('SEXO M/F:')).strip()
    somaidade+=n2
    if c ==1 and n3 in'Mm':
        maioridadehomem = n2
        nomevelho = n1
    if n3 in 'Mm' and mediaidade > maioridadehomem:
        maioridadehomem=n2
        nomevelho=n1
    if n3 in 'Ff' and n2<20:
        mulher20+=1

    sleep(0.5)
mediaidade= somaidade / 4
print(f'A media de idade do grupo é {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} anos e o nome é {nomevelho}')
print(f'Ao todo são {mulher20} com menos de 20 anos!')