from PessoaFisica import PessoaFisica
from ContaCorrente import ContaCorrente
from Deposito import Deposito
from Saque import Saque

def menu_opcoes():
    while True:
        print("\n===== MENU =====")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Cadastrar Usuário")
        print("5. Sair")

        try:
            opcao = int(input("Qual opção deseja selecionar? "))
            if opcao in [1, 2, 3, 4, 5]:
                return opcao
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: digite apenas números inteiros.")

def menu_login():
    while True:
        print("\n=== MENU INICIAL ===")
        print("1. Fazer login")
        print("2. Cadastrar novo usuário")
        print("3. Encerrar programa")

        try:
            opcao = int(input("Qual opção deseja selecionar? "))
            if opcao in [1, 2, 3]:
                return opcao
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: digite apenas números inteiros.")

def main():
    usuarios = []
    contas = []

    while True:
        opcao_login = menu_login()

        if opcao_login == 1:  # Fazer login
            cpf = input("Informe seu CPF: ")
            usuario = buscar_usuario(cpf, usuarios)
            if usuario:
                print(f"\nBem-vindo, {usuario.nome}!")
                conta = usuario.contas[0] if usuario.contas else None
                if not conta:
                    print("Usuário sem conta bancária. Cadastre uma.")
                    continue

                while True:
                    opcao = menu_opcoes()

                    if opcao == 1:  # Depósito
                        valor = float(input("Informe o valor do depósito: "))
                        transacao = Deposito(valor)
                        usuario.realizar_transacao(conta, transacao)

                    elif opcao == 2:  # Saque
                        valor = float(input("Informe o valor do saque: "))
                        transacao = Saque(valor)
                        usuario.realizar_transacao(conta, transacao)

                    elif opcao == 3:  # Extrato
                        print("\n=== Extrato ===")
                        for transacao in conta.historico.transacoes:
                            print(f"{transacao['data']} - {transacao['tipo']} - R${transacao['valor']:.2f}")
                        print(f"\nSaldo atual: R${conta.saldo:.2f}")

                    elif opcao == 4:  # Cadastrar nova conta para usuário existente
                        numero_conta = len(contas) + 1
                        nova = ContaCorrente.nova_conta(usuario, numero_conta)
                        contas.append(nova)
                        usuario.adicionar_conta(nova)
                        print("Conta adicionada com sucesso!")

                    elif opcao == 5:
                        print("Saindo do menu de operações.")
                        break

            else:
                print("Usuário não encontrado. Cadastre-se primeiro.")

        elif opcao_login == 2:  # Cadastrar novo usuário
            nome = input("Nome completo: ")
            data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
            cpf = input("CPF: ")
            endereco = input("Endereço (logradouro, número - bairro - cidade/estado): ")

            if buscar_usuario(cpf, usuarios):
                print("Já existe um usuário com esse CPF.")
                continue

            novo_usuario = PessoaFisica(nome, data_nasc, cpf, endereco)
            usuarios.append(novo_usuario)

            numero_conta = len(contas) + 1
            conta = ContaCorrente.nova_conta(novo_usuario, numero_conta)
            contas.append(conta)
            novo_usuario.adicionar_conta(conta)

            print("Usuário e conta criados com sucesso!")

        elif opcao_login == 3:
            print("Programa encerrado.")
            break


def buscar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None


if __name__ == "__main__":
    main()
