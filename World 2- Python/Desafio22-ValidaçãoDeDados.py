sexo = str(input('Qual seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo= str(input('Dados invalidoss. Digite [M/F]')).strip().upper()[0]
print(f'Registrado, seu sexo é {sexo}')