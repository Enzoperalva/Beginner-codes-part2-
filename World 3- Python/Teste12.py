def teste():
    x=8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}') #x só existe nessa função, ela é uma
                                          #variável local

#Progama pricipal
n=2 #variável global, funciona tanto aqui quanto lá em cima
print(f'No programa principal, n vale {n}')
teste()