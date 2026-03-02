from rich import print
from rich import inspect

class Funcionario:
    #ATRIBUTOS DE CLASSE
    empresa = 'Curso em Vídeo'
    def __init__(self, nome, setor, cargo):
        #ATRIBUTOS DE INSTÂNCIA
        self.nome= nome
        self.setor= setor
        self.cargo= cargo

    def apresetacao(self) -> str:
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}.'


c1= Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresetacao())
#inspect(c1, methods=True)

c2= Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresetacao())
#inspect(Funcionario)