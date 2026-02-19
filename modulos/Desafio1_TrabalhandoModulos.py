from modulos import moeda

p = float(input('Digíte o preço: R$'))
print(f'A metade de {p} é {moeda.metdade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p,13)}')