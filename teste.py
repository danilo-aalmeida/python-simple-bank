from models.cliente import Cliente
from models.conta import Conta


cliente1: Cliente = Cliente('Fulano da Silva', 'fulano@email.com', '123.456.789-01', '01/01/2000')
cliente2: Cliente = Cliente('Ciclano dos Santos', 'ciclano@email.com', '101.112.131-41', '01/02/2010')

conta1: Conta = Conta(cliente1)
conta2: Conta = Conta(cliente2)

