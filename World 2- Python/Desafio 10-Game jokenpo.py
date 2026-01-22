import random, time

#VARIÁVEIS:
lista= ['pedra', 'papel', 'tesoura']
bot= (random.choice(lista)).lower()

#INTERAÇÃO:
print('-='*12)
print('VAMOS BRINCAR DE JOKENPO!')
print('-='*12)
time.sleep(1)

print('Eu ja escolhi o meu, agora é sua vez:')
time.sleep(0.5)
print('PEDRA')
time.sleep(0.7)
print('PAPEL')
time.sleep(0.7)
print('TESOURA')
time.sleep(0.7)

#VARIÁVEIS:
opcao= str(input('Opção:')).lower()

#CONDIÇÕES DE DEORRTA E EMPATE:
if bot == 'pedra' and opcao== 'tesoura':
    print(f'Você perdeu, eu escolhi {bot} e você {opcao}!')

elif bot == 'pedra' and opcao== 'pedra':
    print('Empatamos, ambos de nós escolhemos pedra')

elif bot== 'papel' and opcao== 'tesoura':
    print(f'Eu perdi, você escolheu {opcao} e eu {bot}')