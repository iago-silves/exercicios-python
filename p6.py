def pegar_numero( ):
    while True:
        try:
            entrada = input('Digite dois números, separados por virgula: ').split(',')
            
            # Converte cada item da lista para float
            numeros = [float(num) for num in entrada]
            
            if 2 != len(entrada):
             	print('Erro: Digite apenas dois números.')            
            else:
             	return numeros
             
        except ValueError:
            print('Erro: Digite apenas números válidos.')

def operacoes_basicas(opcao, numeros):
	if opcao == '+':
		calculo = numeros[0] + numeros[1]
	
	elif opcao == '-':
		calculo = numeros[0] - numeros[1]
	
	elif opcao == '*':
		calculo = numeros[0] * numeros[1]
	
	elif opcao == '/':
		if numeros[1] != 0:
			calculo = numeros[0] / numeros[1]	
		else:			
			return 'É impossivel dividir qualquer número por zero.'
	
	return f'O càlculo entre {numeros[0]} e {numeros[1]} resulta em: {calculo:.2f}.'

def menu_opcao( ):
	while True:
		print('Que operação você deseja fazer? (+), (-), (*), (/)')
		opcao = input('Qual operação será efetuada? ').strip()
		if opcao in ['+','-', '*', '/']:
			return opcao 
		print('Erro: Digite uma opcão válida.')

def continuar_sim_nao( ):
	while True:
		continuar = input('Continuar? [S/N]').strip().upper()
		if continuar not in ['N', 'S']:
			print('Erro: Digite uma opção vàlida.')
		else:
			return continuar
		
# Função Principal			
def main( ):
	while True:
		print('== CALCULADORA SILVESTRE ==')
		print('-*' * 30)
		numeros = pegar_numero( )
		opcao = menu_opcao( )		
		resultado = operacoes_basicas(opcao, numeros)
		print(resultado)
		continuar = continuar_sim_nao( )
		if continuar == 'N':
			print('Fechando execução do programa... ')
			break	
		print('-*' * 30)

if __name__ == '__main__':
	main( )