
class Conta:

    def __init__(self, titular, numero, saldo=0):
        self._saldo = 0
        self._numero = numero
        self._titular = titular

    
    def get_saldo(self):
        return self._saldo
    
    
    def set_saldo(self, saldo):
        if (saldo < 0):
            print('O saldo não pode ser negativo.')
        else:
            self._saldo = saldo


    def saque(self, valor):
        if (self._saldo >= valor):
            self._saldo -= valor
            print('Saque realizado com sucesso.')
        else:
            print('Saldo insuficiente.')


    def deposita(self, valor):
        self._saldo += valor


    def extrato(self):
        print(f'Cliente: {self._titular} Saldo Atual: {self._saldo}')