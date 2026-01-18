name= str(input('Qual seu nome? '))

if name.lower() == 'gustavo':
    print('Que nome bonito<3')
elif name.lower() == 'maria' or name.lower() ==  'pedro' or name.lower() == 'paulo':
    print('Seu nome é bem popular no Brasil.')
elif name in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome feminino!')
else:
    print('Que nome normal..')

print(f'Tenha um bom dia, {name.capitalize()}!')