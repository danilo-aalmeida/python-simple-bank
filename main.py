from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main():
    menu()


def menu() -> None:
    print('')
    print(''.center(50, '='))
    print(' Caixa 24h '.center(50, '='))
    print(' Geek Bank '.center(50, '='))
    print(''.center(50, '='))

    print('Selecione uma opcao abaixo: ')
    print('1  - Criar conta')
    print('2  - Efetuar saque')
    print('3  - Efetuar deposito')
    print('4  - Efetuar transferencia')
    print('5  - Listar contas')
    print('6  - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opcao invalida')
        sleep(1)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)

    print(f'Conta criada com sucesso.')
    print('')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o numero da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Nao foi encontrada a conta com numero {numero}')

    else:
        print('Ainda nao existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o numero da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input('Informe o valor do deposito: '))
            conta.depositar(valor)
        else:
            print(f'Nao foi encontrada a conta com numero {numero}')

    else:
        print('Ainda nao existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_origem: int = int(input('Informe o numero da sua conta: '))
        conta_origem: Conta = buscar_conta_por_numero(numero_origem)
        if conta_origem:
            numero_destino: int = int(input('Informe o numero da conta destino: '))
            conta_destino: Conta = buscar_conta_por_numero(numero_destino)
            if conta_destino:
                valor: float = float(input('Informe o valor da transferencia: '))
                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'A conta destino com numero {numero_destino} nao foi encontrada')
        else:
            print(f'Sua conta com numero {numero_origem} nao foi encontrada')

    else:
        print('Ainda nao existem contas cadastradas.')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print(' Listagem de contas '.center(50, '='))
        for conta in contas:
            print(conta)
            print(''.center(50, '-'))
            sleep(1)
    else:
        print('Ainda nao existem contas cadastradas.')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    conta_pesquisada: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                conta_pesquisada = conta
    return conta_pesquisada


if __name__ == '__main__':
    main()
