import math, time
print('-=-='*7)
print('VAMOS PLANEJAR SUA VIAGEM...')
print('-=-='*7)

distancia= float(input('Me fale a distância da sua viagem em km:'))
print('Qual é o preço da viagem por km?')
valor= float(input('Ex: 0.50 centavos por km:'))
carteira= float(input('Quanto você tem na conta para atualizarmos em dolar:'))
atual= float(input('E qual a cotação do dolar atual:'))

#CALCULOS:
total= distancia * valor
dolar= carteira / atual
dias1= math.floor(dolar / 80)

#CALCULO 2:
n1= carteira - total
n2= n1 / atual
totaldolar= math.floor(n2 / 80)
faltou= 400 - n2

print('\033[36mANALISANDO\033[m...')
time.sleep(3)
#EXIBIR

print(f'Viajando por {distancia} km, você vai pagar um total de {total:.2f}')
print(f'Os seus R${carteira} valem US${dolar:.2f}')
print(f'Você vai conseguir ficar {totaldolar} dias, tendo em vista que o custo diario é US$80.00')
print(f'Você só vai conseguir ficar esses dias por causa do preço da passagem R${total}.')

#INFORMAÇÕES:
print(f'Saldo em real:{carteira}')
print(f'Saldo em dollar descontando o valor da passagem da passagem: {n2:.2f}')

#CONDIÇÕES

if totaldolar >= 5:
    print('\033[32mVIAGEM POSSÍVEL!\033[m')
else:
    print('\033[31mECONOMIZE MAIS!\033[m')
    print(f'Faltou {faltou:.2f} dollares para você conseguir viajar, em reais: {faltou * atual:.2f}!')