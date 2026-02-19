from moeda import aumentar,metdade, dobro, diminuir

p = float(input('Digíte o preço: R$'))
print(f'A metade de {p} é {metdade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p,10)}')
print(f'Diminuindo 13%, temos {diminuir(p,13)}')