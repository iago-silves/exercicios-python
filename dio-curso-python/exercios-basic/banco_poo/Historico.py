from datetime import datetime

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def exibir(self): 
        print("\n=== Histórico de Transações ===")
        for transacao in self.transacoes:
            print(f"{transacao['data']} - {transacao['tipo']}: R${transacao['valor']:.2f}")
