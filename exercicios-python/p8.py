while True:
	try:
		print('== GERADOR DE TABUADA ==')
		tabuada = float(input('Digite o número: '))
		
		for i in range(1, 11):
			calculo = i * tabuada
			print(f'{i} x {tabuada} = {calculo:.2f}')
		
		continuar = input('Continuar? [S/N]').strip().upper()
		if continuar not in ['N', 'S']:
			print('Erro: Digite uma opção vàlida.')
			continue			
		elif continuar != 'S':
			print('Fechando programa...')
			break
	
	except ValueError:
		print('Erro: Certifique-se de que inseriu números válidos.')
	