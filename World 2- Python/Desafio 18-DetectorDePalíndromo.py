#MINHA RESOLUÇÃO:
algo= str(input('Digíte uma frase:')).upper().strip()
algo1= algo.replace(' ', '')
embaralhar= algo1[::-1]
print(f'O inverso de {algo1} é {embaralhar}.')
if algo1== embaralhar:
    print('\033[32mELA É UM PALÍNDROMO!\033[m')
else:
    print('\033[31mNÃO É UM PALÍNDROMO!\033[m')

#RESOLUÇÃO GUSTAVO GUANABARA:
algo= str(input('Dígite uma frase:')).strip().upper()
palavras= algo.split()
juntar= ''.join(palavras)
inverso= ''
for letra in range(len(juntar)-1, -1, -1):
    inverso+= juntar[letra]
print(f'O inverso de {juntar} é {inverso}')
if juntar== inverso:
    print('\033[32mELA É UM PALÍNDROMO!\033[m')
else:
    print('\033[31mELA NÃO É UM PALÍNDROMO!\033[m')