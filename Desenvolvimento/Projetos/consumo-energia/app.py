print("=== Calculadora de Consumo Elétrico ===")

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

consumo_mensal = (potencia * horas_dia * 30) / 1000

print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")

# Cálculo do custo estimado
valor_kwh = 0.75
custo_mensal = consumo_mensal * valor_kwh

print(f"Custo estimado: R$ {custo_mensal:.2f}/mês")