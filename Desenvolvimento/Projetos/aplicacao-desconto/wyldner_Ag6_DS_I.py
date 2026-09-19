print("=== Calculadora para aplicação de desconto ===")

valor_conta_brl = float(input("Digite o valor total da compra: ")) 

if valor_conta_brl < 200:	
	valor_desconto_brl = valor_conta_brl * 0.05			# desconto de 5%
elif valor_conta_brl < 300:									
	valor_desconto_brl = valor_conta_brl * 0.1			# desconto de 10%	
else:
	valor_desconto_brl = valor_conta_brl * 0.15			# desconto de 15%
	
print(f"Valor do desconto: R${valor_desconto_brl:.2f}")
valor_total_brl = valor_conta_brl - valor_desconto_brl
print(f"Valor total a ser pago: R${valor_total_brl:.2f}")
# OBS.: não há tratamento para valores q excedam valor máx do float e nem valores negativos