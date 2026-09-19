################################################################################################################## 
############################################## conversando com a IA ##############################################
##################################################################################################################
from decimal import Decimal

print("=== Calculadora para aplicação de desconto ===")


def calcular_desconto(valor):						# sobre chamar função, def (what?!). precisa criar antes = C
    if valor < 0:
        raise ValueError("O valor da compra não pode ser negativo.")	# sobre throw simples, aqui chama raise (what?!)

    if valor < 200:
        percentual_desconto = Decimal("0.05")				# sobre o erro de Float com decimais, Aqui só Decimal (java → BigDecimal)
    elif valor < 300:
        percentual_desconto = Decimal("0.10")
    else:
        percentual_desconto = Decimal("0.15")

    valor_desconto = valor * percentual_desconto
    valor_total = valor - valor_desconto

    return valor_desconto, valor_total


valor_conta_brl = Decimal(input("Digite o valor total da compra: "))

try:
    valor_desconto_brl, valor_total_brl = calcular_desconto(valor_conta_brl)

    print(f"Valor do desconto: R$ {valor_desconto_brl:.2f}")
    print(f"Valor total a ser pago: R$ {valor_total_brl:.2f}")

except ValueError as erro:						# ok, não tem catch, é except (os diferentões né)
    print(f"Erro: {erro}")

