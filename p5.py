def HistoricoNumero(numeros):
	if not numeros:
		print("Nenhum número foi adicionado ainda.")
		
	for i, (num, tipo) in enumerate(numeros, start=1):
		print(f'{i}. O número {num} é: {tipo}.')
		
def Salvar(numeros, numero, tipo):	
	numeros.append((numero, tipo))

def DigiteNumero( ):
	while True:
		try:
			numero = float(input('Digite um número qualquer: '))
			return numero
			
		except ValueError:
			print('Erro: Digite apenas números.')

def AnaliseDigito(numero):
	if numero < 0:
		return 'Número negativo'
	
	elif numero == 0:
		return 'Número zero'
	
	else:
		return 'Número positivo'

def main( ):
	numeros = [ ]
	
	while True:
		try:
			print('Menu:\n [1] Adicionar número\n [2] Mostrar números\n [3] Sair')
			
			opcao = int(input('Escolha uma opção: '))
			
			if opcao == 1:
				numero = DigiteNumero( )
				tipo = AnaliseDigito(numero)
				dado = Salvar(numeros, numero, tipo)
				print(f"Número {numero} classificado como '{tipo}' foi salvo.")
			
			elif opcao == 2:
				HistoricoNumero(numeros)
			
			elif opcao == 3:
				print('Fechando programa')
			
			else:
				print('Escolha uma opção valida.')
		
		except ValueError:
			print('Erro: Digite opções válidas.')

if __name__ == '__main__':
	main()
	