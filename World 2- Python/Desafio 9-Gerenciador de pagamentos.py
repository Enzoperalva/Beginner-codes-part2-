import time

#INTERAÇÃO COM VARIÁVEIS:
valor= float(input('Qual valor do produto:'))
print('\033[36mESCOLHA A CONDIÇÃO DE PAGAMENTO\033[m')
print('[ 1 ] A VISTA, DINHEIRO/CHECK: 10% de desconto!')
time.sleep(0.5)
print('[ 2 ] A VISTA NO CARTÃO: 5% de desconto!')
time.sleep(0.5)
print('[ 3 ] EM ATÉ 2x NO CARTÃO: preço normal!')
time.sleep(0.5)
print('[ 4 ] 3x OU MAIS NO CARTÃO: 20% de juros!')
time.sleep(0.5)
num1= int(input('Opcão:'))

#CONDIÇÕES:
if num1 == 1:
    avista= valor * 0.1
    total1= valor - avista
    print(f'Pagando {valor} a vista você tem 10% de desconto!')
    print(f'O preço com o desconto é de R${total1}')

elif num1 == 2:
    avista1= valor * 0.05
    total2= valor - avista1
    print(f'Pagando {valor} a vista no cartão, você tem 5% de desconto!')
    print(f'O preço com o desconto é de R${total2}')

elif num1 == 3:
    cartao= valor / 2
    print(f'Dividindo no cartão você não tem desconto, agora vai pagar 2 parcelas de R${cartao}')

elif num1 == 4:
    num2= int(input('Em quantas vezes você quer dividir:'))
    juros= valor * 0.2
    juros1= valor + juros
    parcela= juros1 / num2
    print(f'Dividindo por 3 você tem um juros de 20%')
    print(f'Você iria pagar {valor} e agora vai pagar {juros1}')
    print(f'Tudo isso em 3 parcelas de R${parcela}')

else:
    print('\033[31mESCOLHAS AS OPÇÕES CERTAS: 1, 2, 3 OU 4\033[m')