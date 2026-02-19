from moedaPT2 import aumentar,metdade, dobro, diminuir, moeda

p = float(input('Digíte o preço: R$'))
print(f'A metade de {moeda(p)} é {moeda(metdade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10%, temos {moeda(aumentar(p,10))}')
print(f'Diminuindo 13%, temos {moeda(diminuir(p,13))}')