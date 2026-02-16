def linha(msg):
    print('-='*10)
    print(msg)
    print('-='*10)


linha('Controle de terrenos')
def area(a,b):
    print(f'A área do terreno {a}x{b} é de {a * b}m².')


area(a= float(input('LARGURA (m): ')), b= float(input('COMPRIMENTO (m): ')))