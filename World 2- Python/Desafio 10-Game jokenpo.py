import random, time

#VARIÁVEIS:
lista= ('pedra', 'papel', 'tesoura')
bot= (random.choice(lista)).lower()

#INTERAÇÃO:
print('-='*12)
print('VAMOS BRINCAR DE JOKENPO!')
print('-='*12)
time.sleep(1)

print('Eu ja escolhi o meu, agora é sua vez!')
time.sleep(1)
print('PEDRA')
print('PAPEL')
print('TESOURA')
time.sleep(0.7)

#VARIÁVEIS:
opcao= str(input('Opção:')).lower()
if opcao not in lista:
    print('\033[31mJOGADA INVALIDA\033[m')
    print('Escolha pedra, papel ou tesoura!')
    exit()

print('JO')
time.sleep(0.4)
print('KEN')
time.sleep(0.4)
print('PO')
time.sleep(0.5)

print('--='*10)
#CONDIÇÕES DE DEORRTA E EMPATE:
        #PEDRA:
if opcao == bot:
    print('\033[36mEMPATAMOS\033[m')
    print(f'Ambos de nós escolhemos {bot}')
elif(opcao == 'pedra' and bot == 'tesoura') or \
    (opcao == 'tesoura' and bot == 'papel') or \
    (opcao == 'papel' and bot == 'pedra'):
    print(f'\033[32mGANHADOR\033[m')
    print(f'Eu escolhi {bot}')
else:
    print('\033[31mVOCÊ PERDEU!\033[m')
print('--='*10)