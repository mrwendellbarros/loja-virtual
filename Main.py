from Cliente import Cliente
from Conta import Conta

class Main:

    pass

c1 = Cliente("joão", "114444-2222")
conta = Conta(c1.nome, 6565, 0)

print(f'{conta.titular} Numero: {conta.numero} Seu saldo: {conta.saldo}')
