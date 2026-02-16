def linha():
    print('-='*30)


def soma(a,b):
    s= a+b
    print(s)


soma(5,7)
linha()
#Empacotar parametros
def contador (*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    tam=len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

linha()
def dobra(lst):
    pos=0
    while pos< len(lst):
        lst[pos]*=2
        pos+=1


valores= [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
linha()
def soma(* valores):
    s=0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 7, 8)
soma(2, 5, 6, 7)