try:
	idade_cliente = int(input('Qual é a idade do cliente? '))
	valor_produto = float(input('Qual é o valor do produto? '))

	if idade_cliente >= 60:
		desconto_aplicado_valor = valor_produto * 0.2
		valor_pago_cliente = valor_produto - desconto_aplicado_valor  
		
	else:
		desconto_aplicado_valor = valor_produto * 0.05
		valor_pago_cliente = valor_produto - desconto_aplicado_valor  
	
	print(f'O cliente com a idade {idade_cliente} irá pagar com o desconto de R$ {desconto_aplicado_valor}: R$ {valor_pago_cliente}')
	
except ValueError:
	print('Erro: Digite valores válidos')
		