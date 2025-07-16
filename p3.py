contador_pontos = 0
acertos = 0

def linha(char='-*', quant=30):
	print(char * quant)

def verificar_resposta():
	while True:
		resposta = input('Resposta: ').strip().lower()
	
		if resposta in ['a', 'b', 'c', 'd']:
			return resposta		
		print('Insira apenas opções válidas.')
		
		
	
print('=== QUIZ DO GPT - TESTE O CONHECIMENTO ===')
linha()
print( '''Qual é o resultado de 2 * 3 + 5 em Python?
a) 16
b) 11
c) 10
d) 13 ''')
questao1 = verificar_resposta()
linha()
print('''Qual destas estruturas é usada para repetir um bloco de código até que uma condição seja falsa?
a) if
b) while
c) for
d) def ''')
questao2 = verificar_resposta()
linha()
print('''O que é um dicionário em Python?
a) Uma estrutura que armazena dados em pares chave-valor.
b) Um tipo de lista que aceita valores duplicados.
c) Uma função usada para criar listas.
d) Um tipo de variável que contém apenas números inteiros. ''')
questao3  = verificar_resposta()
linha()
	
if questao1 == 'b':
	contador_pontos += 10
	acertos += 1
	
if questao2 == 'a':
	contador_pontos += 10
	acertos += 1
	
if questao3 == 'a':
	contador_pontos += 10
	acertos += 1

print(f'Os seus acertos foram {acertos} e a sua quantidade: {contador_pontos}.')
	