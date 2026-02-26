class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, rg, nome, saldo = 0):
        self.id = rg
        self.titular =  nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucessor. Saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta de {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def depositar(self, valor):
        self.saldo+= valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo-=valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")
        else:
            print(f"Tranzação negada, você não pode sacar R${valor:,.2f} com R${self.saldo} na conta {self.id}!")




c1= ContaBancaria(112, "Gustavo", 3000)
c1.depositar(500)
c1.sacar(2_000_000)
print(c1)
print(c1.__doc__)