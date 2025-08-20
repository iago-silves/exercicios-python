while True:
	try:
		num = float(input('Digite um número: '))
		
		if num < 0:
			print('Digite números inteiros ou flutuantes positivos.')
			continue
		
		else:	    
			if num > 10:
				print('O numero digitado é maior que dez, True.')
			
			else:
				print('O numero digitado é menor que dez, False')
		
		dobro = num * 2
		quadrado = num **2
		
		print(f'O dobro de {num} = {dobro}\n'
				 f'O quadrado de {num} = {quadrado}')
		
		continuar = input('Para continuar digite: (S)im (N)ão ').strip().upper()
		
		if continuar == 'N':
			break
		
		elif continuar != 'S':
			print('Digite "S" para continuar ou "N" para sair.')
			
	except ValueError:
		print('Insira números positivos válidos.')