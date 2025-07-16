controle_estoque_produtos = [ ]

def obtecao_produtos( ):
	try:
		nome = input('Qual o nome do produto? ').strip().title()
		
		if not nome:
			print('Erro: Insira o nome do produto corretamente.')
			return None
		else:	
			quantidade = int(input('Qual é a quantidade do produto? '))
			preco = float(input('Informe o preço unitário do produto: '))			
		return nome, quantidade, preco
	
	except ValueError:
		print('Erro: Certifique-se de que inseriu números válidos.')
		return None	

def cadastrar_produtos(nome, quantidade, preco):
	produto = {
			'nome': nome, 
			'quantidade': quantidade,
			'preco': preco
	}
	controle_estoque_produtos.append((produto))
	return f'Produto {nome} cadastrado com sucesso.'

def menu_cadastro():
    while True:
        print('1. Adicionar produtos\n'
              '2. Mostrar produtos\n'
              '3. Remover produtos\n'
              '4. Sair')
        try:
            opcoes = int(input('Digite a opção: '))
            if opcoes in [1, 2, 3, 4]:
                return opcoes
            else:
                print('Erro: Escolha uma opção válida.')
        except ValueError:
            print('Erro: Digite valores válidos.')

def exibicao_produtos():
    if not controle_estoque_produtos:
        print('Estoque vazio.')
    else:
        for i, produto in enumerate(controle_estoque_produtos, start=1):
            print(f'{i}. nome: {produto["nome"]}, quantidade: {produto["quantidade"]} — preço: {produto["preco"]}')

def remover_produto( ):
	try:
		print('== Remoção de produtos ==')
		produtos = controle_estoque_produtos
		index = int(input('Qual o index do produto? ')) - 1
		if index < 0 or index >= len(produtos):
			print('Erro: indice não vinculado a produto.')
		else:
			controle_estoque_produtos.pop(index)
			print('Produto removido com sucesso.')
	except ValueError:
		print('Erro: Digite index válidos.')	

def opcoes_do_programa(opcao):
    if opcao == 1:
        retorno = obtecao_produtos()
        if retorno:
            nome, quantidade, preco = retorno
            print(cadastrar_produtos(nome, quantidade, preco))
    elif opcao == 2:
        exibicao_produtos()
    elif opcao == 3:
        remover_produto()

def main( ):
	while True:
		opcao = menu_cadastro( )
		opcoes_do_programa(opcao)
		if opcao == 4:
			print('finalizando programa.')
			break			

if __name__=='__main__':
	main( )