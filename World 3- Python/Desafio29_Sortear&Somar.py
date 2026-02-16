import random, time
def sorteio(lista):
    print('Sorteando cinco valores da lista: ',end='')
    for cont in range(0,5):
        n= random.randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        time.sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma=0
    for valor in lista:
        if valor % 2 == 0:
            soma+=valor
    print(f'Números pares somados: {soma}')


numeros = list()
sorteio(numeros)
somaPar(numeros)