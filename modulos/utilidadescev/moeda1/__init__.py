def aumentar(n=0,taxa=0):
    res = n + (n * (taxa/100))
    return res


def diminuir(n=0, taxar=0):
    res=n - (n* (taxar / 100))
    return res


def dobro(n=0):
    res = n * 2
    return res


def metdade(n=0):
    res = n / 2
    return res


def moeda(n = 0, moeda = 'R$', show= False):
    if show:
        return f'{moeda}{n:.2f}'.replace('.',',')
    else:
        return f'{moeda}{n}'


def resumo(n=0, taxa=10, taxar=5):
    print('_'*30)
    print('RESUMO DO VALOR'.center(30))
    print('_' * 30)
    print(f'Preço analisado: \t{moeda(n, show=True)}')
    print(f'Dobro do preço: \t{moeda(dobro(n), show=True)}')
    print(f'Metade do preço: \t{moeda(metdade(n), show=True)}')
    print(f'Com {taxa}% de aumento:\t{moeda(aumentar(n, taxa), show=True)} ')
    print(f'Com {taxar}% de redução: \t{moeda(diminuir(n, taxar), show=True)}')
    print('_' * 30)