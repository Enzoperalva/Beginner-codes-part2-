import time

n1= 0
n2= 0
menu= 1 and 2 and 3 and 4

while menu == 1 or menu == 2 or menu == 3 or menu == 4:
    n1= float(input('Digite um valor:'))
    n2= float(input('Digite outro valor:'))

    print('\033[36mMENU\033[m')
    print('\033[35m[1]\033[m SOMAR')
    print('\033[35m[2]\033[m MULTIPLICAR')
    print('\033[35m[3]\033[m MAIOR')
    print('\033[35m[4]\033[m NOVOS NÚMEROS')
    print('\033[35m[5]\033[m SAIR DO PROGRAMA')
    menu= int(input('Qual opção você vai escolher:'))
    if menu== 1:
        print(f'A soma entre {n1} mais {n2} é {n1+n2}')
    elif menu == 2:
        print(f'A multiplicação de {n1} com {n2} é {n1*n2}')
    elif menu == 3:
        if n1> n2:
            print(f'O {n1:.1f} é maior que {n2:.1f}')
        elif n2>n1:
            print(f'O {n2:.1f} é maior que {n1:.1f}')
        else:
            print(f'{n1:.1f} e {n2:.1f} tem o mesmo valor!')
    elif menu == 4:
        print('\033[33mVoltando...\033[m')
        time.sleep(2)
    elif menu == 5:
        print('\033[36mFINALIZANDO...\033[m')
        time.sleep(1.3)
    else:
        print('\033[31mOpção invalida!\033[m')
