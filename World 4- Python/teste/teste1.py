#DESAFIO 1
'''from rich import print
from rich.table import Table

nome= input('Nome do item: ')
quant= int(input(f'Quantidade de {nome}: '))
pack= quant // 64
sobrando= quant % 64

tabela = Table(title='Tabela de itens')

tabela.add_column('Nome', justify="left", style='black')
tabela.add_column('Quantidade', justify='center', style='white')
tabela.add_column('Packs', justify='center', style='green')
tabela.add_column('Unidade', justify='center', style='red')

tabela.add_row(f'{nome}', f'{quant}', f'{pack}', f'{sobrando}')

print(tabela)'''

#DESAFIO 2
'''from rich import print
x= float(input('Cordenada atual (X): '))
base= float(input('Cordenada da base (X): '))
blocos= x-base
print(f'Você esta à uma distância de {abs(blocos)} da sua base!')'''

#DESAFIO 3
'''from rich import print
diamantes= int(input('Diamantes: '))
stick= int(input('Gravetos: '))

diamantes//=3
stick//=2

print(f'Você consegue fazer {min(stick, diamantes)} picaretas.')'''

#DESAFIO 4
'''name= input('Nome: ').strip()
print(name.upper())
print(name.lower())
print(len(name))
print(name.capitalize())'''

#DESAFIO 5
'''frase= input('Digite uma frase: ').strip()
n= frase.startswith('/')

print(f'A frase possui / no começo: {n}')'''

#DESAFIO 6
'''from rich import print

distancia= float(input('Qual distância você está do mob: '))
if distancia <= 3:
    print('Situação: [red]PERIGO EXTREMO[/]')
elif 3.1 <= distancia < 10:
    print('Situação: [yellow]MOB ESTÁ SE APROXIMANDO[/]')
else:
    print('[green]ZONA SEGURA[/]')'''

#DESAFIO 7
'''from rich import print
fome= int(input('Fome: '))
if  6 < fome < 20:
    print('[yellow]CORRIDA[/]')
elif fome <= 6:
    print('[red]FOME CRÍTICA[/]')
elif fome == 20:
    print('[green]REGENERANDO[/]')
else:
    print('[black]VALOR INVALÍDO[/]')'''

#DESAFIO 8
'''from rich import print
temperatura= int(input('Temperatura [C°]: '))
umidade= int(input('Umidade: '))
if temperatura > 30 and umidade < 20:
    print('Você está no [yellow]DESERTO[/]')
elif temperatura < 0:
    print('Você está na [blue]NEVE[/]')
elif 10 < temperatura < 25 and umidade > 50:
    print('Você está na [green]FLORESTA[/]')
else:
    print('[black]LOCAL DESCONHECIDO![/]')'''

#DESAFIO 9
'''from rich import print
dano= int(input('Ataque da espada: '))
defesa= int(input('Defesa do inimigo: '))
total= max(0, dano-defesa)
if total > 0:
    print(f'Voce causou {total} de dano!')
else:
    print('Você não causou dano')'''

#DESAFIO 10
from rich import print
peixe= 0
while peixe < 3:
    resp= input('Pescou algum peixe? [S/N]').upper().strip()[0]
    while resp not in 'SN':
        print('[red]RESPOSTA INVÁLIDA[/]')
        resp = input('Pescou algum peixe? [S/N]').upper().strip()[0]
    if resp == 'S':
        print('[yellow]BOAAAA![/]')
        peixe+=1
    else:
        pass
print('[green]PARÁBENS, VOCÊ PESCOU 3 PEIXES[/]')