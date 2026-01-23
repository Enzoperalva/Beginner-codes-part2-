from datetime import date

maior=0
menor=0
atual= date.today().year
for pess in range(0, 7):
    nasc= int(input(f'Em qual a ano a pessoa {pess+1} nasceu:'))
    idade= atual-nasc
    if idade >= 21:
        maior+=1
    else:
        menor+=1
print(f'Ao todo tivemos {maior} pessoas maiores de idade!!')
print(f'E tivemos {menor} pessoas menores de idade!!')