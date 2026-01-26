import time, random

print('Vamos jogar um jogo da adivinhação!')
time.sleep(1)
print('-='*20)
print('\033[36mESTOU PENSANDO EM UM NÚMERO DE 0 A 10\033[m')
print('-='*20)
time.sleep(1.5)

numero= random.randint(0, 10)
jogador= 0
jogadas=0
while jogador != numero:
    jogador= int(input('Em qual número eu pensei:'))
    if jogador != numero and numero>jogador:
        print('\033[31mERROU, O NÚMERO É MAIOR!\033[m')
        time.sleep(1)
    elif jogador != numero and numero<jogador:
        print('\033[31mERROU, O NÚMERO É MENOR!\033[m')
    jogadas+=1
print('\033[32mAcertou\033[m')
print(f'Você precisou de {jogadas} jogadas para me ganhar!')