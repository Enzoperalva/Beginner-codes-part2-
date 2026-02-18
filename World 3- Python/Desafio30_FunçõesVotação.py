#Minha resolução:
from datetime import date
def voto():
    nasc=int(input('Ano de nascimento: '))
    idade= date.today().year - nasc
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO!')
    if 16 <= idade <18 or idade > 70:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    elif 18 <= idade <=70:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')


voto()

#Resolução guanabara:
def voto(ano):
    from datetime import date
    atual= date.today().year
    idade= atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade >70:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


print(voto(ano = int(input('Ano de nascimento:'))))