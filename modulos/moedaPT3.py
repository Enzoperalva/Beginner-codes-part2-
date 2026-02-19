def aumentar(n=0,por=0, formato=False):
    res = n + (n * (por/100))
    return res


def diminuir(n=0, por=0):
    res=n - (n* (por / 100))
    return res


def dobro(n=0):
    res = n * 2
    return res


def metdade(n=0):
    res = n / 2
    return res


def moeda(preco = 0, moeda = 'R$', show= False):
    if show:
        return f'{moeda}{preco:.2f}'.replace('.',',')
    else:
        return f'{moeda}{preco}'