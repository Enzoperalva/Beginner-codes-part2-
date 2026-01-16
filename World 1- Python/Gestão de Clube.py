import time, random

#COLETA DE DADOS DO SÓCIO:
print('-='*14)
print('\033[33mPREENCHA OS DADOS DE SÓCIO:\033[m')
print('-='*14)

#VARIAVEIS:
name= str(input('Qual seu nome:')).strip()
years= int(input('Ano de nascimento:'))
saldo= float(input('Salário atual: R$'))

#ANÁLISE DO NOME:
name_upper= name.upper()
tem= 'SILVA' in name_upper

print('-='*10)
print('\033[36mANALISANDO SEUS DADOS...\033[m')
print('-='*10)
time.sleep(2)

print(f'Seu nome todo maiúsculo: {name_upper}')
time.sleep(1)

print(f'Seu primeiro nome tem {len(name.split()[0])} letras!')
time.sleep(1)

print(f'Seu sobrenome tem silva: {tem}')
time.sleep(1)

#ANÁLISE DE IDADE:
idade= 2026 - years

if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')
time.sleep(1)

print('\033[36mCALCULANDO O VALOR DA MENSALIDADE...\033[m')
time.sleep(2)

carteira= random.randint(1000, 9999)
print(f'O número da sua carteirinha é: {carteira}')

#ANÁLISE FINANCEIRO:

mensalidade= saldo * 0.05
desconto_mensalidade= mensalidade * 0.10
mensalidade_total= mensalidade - desconto_mensalidade

if mensalidade > 500:
    print('\033[34mVocê ganhou um desconto de 10%\033[m')
    print(f'Sua mensalidade é de: {mensalidade_total:.2f}')
else:
    print(f'Sua mensalidae é de: {mensalidade:.2f}')