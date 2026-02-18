lista= []
maior=menor=0
alunos= dict()
def notas(*notas, sit=False):
    lista.append(notas)
    alunos['total'] = (len(notas))
    alunos['maior'] = max(max(lista))
    alunos['menor'] = min(min(lista))
    alunos['média'] = (sum(max(lista))) / len(notas)
    print(alunos['maior'])
    print(alunos['menor'])
    print(f'{alunos["média"]:.1f}')

notas(5,5,6)
