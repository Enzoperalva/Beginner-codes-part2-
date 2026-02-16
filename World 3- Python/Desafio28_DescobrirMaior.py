import time

def maior(*num):
    cont=maior1=0

    print('-='*20)
    print('Analisando os valores passados...')
    time.sleep(0.5)
    for c in num:
        print(c, end=' ', flush=True)
        time.sleep(0.5)
        if cont == 0:
            maior1=c
        else:
            if c > maior1:
                maior1=c
        cont+=1
    print(f'Foram passados {len(num)} valores ao todo!')
    print(f'O maior valor é {maior1}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
