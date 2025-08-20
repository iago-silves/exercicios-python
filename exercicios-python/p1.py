# Exercicio número 1

usuario = [ ]

while True:
	try:		
		nome = input('Qual é o seu nome? ').strip().title()
		idade = int(input('Qual é a sua idade? '))
		altura = float(input('Qual é a sua altura? '))
		
		if idade < 0 or altura < 0:
			print('Digite números inteiros ou flutuantes positivos.')
		else:
			usuario.append([nome, idade, altura])
		
		continuar = input('Para continuar digite: (S)im (N)ão ').strip().title()
		
		if continuar not in ['S', 'N']:
			print('Digite "N" ou "S".')
			continue
		
		elif continuar != 'S':
			break
	
	except ValueError:
		print('digite apenas valores válidos.')

for i, pessoa in enumerate(usuario):
	nome = usuario[i][0]
	idade = usuario[i][1]
	altura = usuario[i][2]
	
	print(f'Olá, {nome}! Você tem {idade} anos e {altura} metros de altura.')
	