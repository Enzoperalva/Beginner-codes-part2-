# Declaração de classe
class Gafanhoto:
    """
    Essa classe crua um Garfanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use
    variavel = Garfanhoto(nome, idade)
    """
    def __init__(self, nome = "Vazio", idade = 0):
        # Atributos de instancia
        self.nome = nome
        self.idade = idade

    # Métodos de instâcia
    def aniversario(self):
        self.idade +=1

    def __str__(self):
        return f"{self.nome} é Garfanhoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de objetos
g1= Gafanhoto("Maria", 17) #Momento de instânciação
g1.aniversario() # Tem parenteses é um metodo
print(g1)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__doc__)
print(g1.__class__)

g2= Gafanhoto("Mauro", 53)
g2.aniversario()
print(g2)
print(g2.__getstate__()) 