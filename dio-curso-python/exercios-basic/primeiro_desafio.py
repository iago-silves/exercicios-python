dados_bancarios = []

def cadastro_usuario(cpf, senha, tipo_conta, endereco=""):
    usuario = {
        "CPF": cpf,
        "senha": senha,
        "Endereco": endereco,
        "tipo_de_conta": tipo_conta,
        "saldo": 0,
        "limite_de_saque": 500,
        "extrato": [],
        "quantidade_saque": 3
    }
    dados_bancarios.append(usuario)
    print(f"Usuário com CPF {cpf} cadastrado com sucesso!")

def acessar_conta(cpf, senha):
    for usuario in dados_bancarios:
        if usuario["CPF"] == cpf and usuario["senha"] == senha:
            print("Login realizado com sucesso!")
            return usuario
    print("CPF ou senha incorretos!")
    return None

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

def conta_deposito(conta, valor_deposito):
    if valor_deposito <= 0:
        print("Erro: Não é possível adicionar valores negativos ou zero.")
    else:
        conta["saldo"] += valor_deposito
        conta["extrato"].append(f"Depósito: R$ {valor_deposito:.2f}")
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")

def regras_saque(conta, valor_saque):
    if valor_saque <= 0:
        print("Erro: O valor do saque deve ser positivo.")
    elif valor_saque > conta["saldo"]:
        print("Erro: Saldo insuficiente.")
    elif valor_saque > conta["limite_de_saque"]:
        print("Erro: O saque excede o limite de R$ 500 por vez.")
    elif conta["quantidade_saque"] <= 0:
        print("Erro: Você atingiu o limite diário de saques.")
    else:
        conta["saldo"] -= valor_saque
        conta["quantidade_saque"] -= 1
        conta["extrato"].append(f"Saque: R$ {valor_saque:.2f}")
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")

def mostrar_extrato(conta):
    print("\n===== EXTRATO =====")
    if not conta["extrato"]:
        print("Nenhuma movimentação realizada.")
    else:
        for mov in conta["extrato"]:
            print(mov)
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")

def main():
    while True:  
        conta_logada = None

        while not conta_logada:
            print("\n=== MENU INICIAL ===")
            print("1. Fazer login")
            print("2. Cadastrar novo usuário")
            print("3. Encerrar programa")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                cpf = input("Digite o CPF: ")
                senha = input("Digite a senha: ")
                conta_logada = acessar_conta(cpf, senha)
            elif escolha == "2":
                cpf = input("Digite o CPF: ")
                senha = input("Digite a senha: ")
                tipo = input("Digite o tipo de conta (corrente/poupança): ")
                endereco = input("Digite o endereço (opcional): ")
                cadastro_usuario(cpf, senha, tipo, endereco)
            elif escolha == "3":
                print("Encerrando o programa. Até mais!")
                return
            else:
                print("Opção inválida!")

        while True:
            opcao = menu_opcoes()

            if opcao == 1:
                valor = float(input("Digite o valor para depósito: "))
                conta_deposito(conta_logada, valor)
            elif opcao == 2:
                valor = float(input("Digite o valor para saque: "))
                regras_saque(conta_logada, valor)
            elif opcao == 3:
                mostrar_extrato(conta_logada)
            elif opcao == 4:
                cpf = input("Digite o CPF: ")
                senha = input("Digite a senha: ")
                tipo = input("Digite o tipo de conta (corrente/poupança): ")
                endereco = input("Digite o endereço (opcional): ")
                cadastro_usuario(cpf, senha, tipo, endereco)
            elif opcao == 5:
                print("Saindo da conta...")
                break  
            
if __name__ == "__main__":
    main()
