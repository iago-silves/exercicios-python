from Saque import Saque
from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, cliente, limite=500, limite_saques=3):
        super().__init__(agencia, numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, agencia=1):
        return cls(agencia, numero, cliente)

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self.limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= self.limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        else:
            return super().sacar(valor)

        return False
