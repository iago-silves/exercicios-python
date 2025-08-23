dados_bancarios = {
    "saldo": 0,
    "limite_de_saque": 500,
    "extrato": "",
    "quantidade_saque": 3
}

def menu_opcoes():
    while True:
        print("\n===== MENU =====")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")

        try:
            opcao = int(input("Qual opção deseja selecionar? "))

            if opcao not in [1, 2, 3, 4]:
                print("Opção inválida. Tente novamente.")
            else:
                return opcao
        except ValueError:
            print("Erro: digite apenas números inteiros.")

def conta_deposito(valor_deposito):
    if valor_deposito <= 0:
        print("Erro: Não é possível adicionar valores negativos ou zero.")
    else:
        dados_bancarios["saldo"] += valor_deposito
        dados_bancarios["extrato"] += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")

def regras_saque(valor_saque):
    if valor_saque <= 0:
        print("Erro: O valor do saque deve ser positivo.")
    elif valor_saque > dados_bancarios["saldo"]:
        print("Erro: Saldo insuficiente.")
    elif valor_saque > dados_bancarios["limite_de_saque"]:
        print("Erro: O saque excede o limite de R$ 500 por vez.")
    elif dados_bancarios["quantidade_saque"] <= 0:
        print("Erro: Você atingiu o limite diário de saques.")
    else:
        dados_bancarios["saldo"] -= valor_saque
        dados_bancarios["quantidade_saque"] -= 1
        dados_bancarios["extrato"] += f"Saque: R$ {valor_saque:.2f}\n"
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")

def mostrar_extrato():
    print("\n===== EXTRATO =====")
    if dados_bancarios["extrato"] == "":
        print("Nenhuma movimentação realizada.")
    else:
        print(dados_bancarios["extrato"])
    print(f"Saldo atual: R$ {dados_bancarios['saldo']:.2f}")

# Programa principal
while True:
    opcao = menu_opcoes()

    if opcao == 1:
        valor = float(input("Digite o valor para depósito: "))
        conta_deposito(valor)
    elif opcao == 2:
        valor = float(input("Digite o valor para saque: "))
        regras_saque(valor)
    elif opcao == 3:
        mostrar_extrato()
    elif opcao == 4:
        print("Encerrando o programa. Até mais!")
        break
