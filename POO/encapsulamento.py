class Conta:
    def __init__(self,nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def Depositar(self, valor):
        self._saldo += valor

    def Sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo



conta = Conta("0001",100)
conta.Depositar(100)
print(conta.mostrar_saldo())

