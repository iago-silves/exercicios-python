# Armazenamento de dados

def armazenamento_dados():
    try:
        with open('armazenamento.txt', 'r') as arquivo:
            dados = []            
            contato_atual = {}
            for linha in arquivo:
                linha = linha.strip()
                if linha == '-' * 20:  # Delimitador de contatos
                    if contato_atual:
                        dados.append(contato_atual)
                        contato_atual = {}
                elif linha:
                    chave, valor = linha.split(': ')
                    contato_atual[chave] = valor
            return dados
                       
    except FileNotFoundError:
        return []

def salvar_dados(dados):
    with open('armazenamento.txt', 'a') as arquivo:
        for i in dados:
            linhas = [f"{chave}: {valor}\n" for chave, valor in i.items()]
            linhas.append("-" * 20 + "\n")  # Delimitador para separar registros
            arquivo.writelines(linhas)

def mostrar_contatos():
    with open('armazenamento.txt', 'r') as arquivo:
        conteudo = arquivo.read()
    print(conteudo)

def buscar_contato(nome):
    try:
        with open('armazenamento.txt', 'r') as arquivo:
            contato_encontrado = False
            contato_atual = {}

            for linha in arquivo:
                linha = linha.strip()
                if linha == '-' * 20:  # Delimitador de contatos
                    if contato_atual.get('nome') == nome:
                        contato_encontrado = True
                        break
                    contato_atual = {}
                elif linha:
                    chave, valor = linha.split(': ')
                    contato_atual[chave] = valor

            if contato_encontrado:
                return contato_atual
            else:
                return f"Contato com o nome '{nome}' não encontrado."
    except FileNotFoundError:
        return "Arquivo não encontrado."

def dados_contatos():
	nome = input('Qual é nome? ').strip().title()
	telefone = int(input('Qual é o telefone? '))
	email = input('Qual é o email? ').strip().title()
	
	return nome, telefone, email

def adicionar_contato(nome, telefone, email):
	dados = [
			{
				'nome': nome,
				'telefone': telefone,
				'email': email
			}
	]
	salvar_dados(dados)
	return 'Contato salvo com sucesso.'

def controle_resposta():	
	while True:
		opcao = input('Opção:')
		if opcao in ['a', 'e', 'p', 's']:
			return opcao
		
		print('Digite opções válidas...')

def menu_opcoes_iniciais():
		while True:
			print('\nMenu:\n (A)dicionar contato\n (E)xibir contatos\n (P)esquisar contato\n (S)air')
			
			opcoes = controle_resposta()
			
			if opcoes == 'a':
				nome, telefone, senha = dados_contatos()
				adicionar_contato(nome, telefone, senha)
			
			elif opcoes == 'e':
				mostrar = mostrar_contatos()
				
			elif opcoes == 'p':
				nome = input('Quem você procura? ').strip().title()
				busca = buscar_contato(nome)
				print(busca)
				
			else:
				break

# Função principal
def main():
	# Armazenamento de dados
	dados_usuarios = armazenamento_dados()
	# Interface com as funcionalidades do codigo
	menu_opcoes_iniciais()

if __name__ == "__main__":
	main()