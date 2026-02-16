import time

def contador(a,b,c):
    if c < 0:
        c*= -1
    if c == 0:
        c=1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    time.sleep(1)
    if a < b:
        cont=a
        while cont <=b:
            print(cont, end=' ', flush= True)
            cont+=c
            time.sleep(0.4)
        print('FIM!')
        print('-='*20)
    else:
        cont=a
        while cont>=b:
            print(cont, end=' ', flush= True)
            cont-=c
            time.sleep(0.4)
        print('FIM!')
        print('-='*20)


contador(a=1, b=10, c=1)
contador(a=10,b=0,c=2)
print('Agora é sua vez de personalizar a contagem!')
contador(a= int(input('Início: ')), b= int(input('Fim: ')), c= int(input('Passo: ')))