print("=== Bem vindo ao classificador de consumo ===")

tipo_valido = False

while not tipo_valido:                                           					# só aceita as opções esperadas
    tipo_imovel = input("Digite o tipo de imóvel:\n(comercial, casa ou apartamento) ").casefold()

    if tipo_imovel == "comercial" or tipo_imovel == "casa" or tipo_imovel == "apartamento":
        tipo_valido = True
    else:
        print("\033[31mPor favor, digite uma das opções apresentadas\033[0m")


consumo_valido = False

while not consumo_valido:                                      						# somente consumo positivo
    consumo_mensal_agua_m3 = float(input("Digite seu consumo de água mensal (m³): "))

    if consumo_mensal_agua_m3 > 0:
        if tipo_imovel == "comercial":                           					# comercial
            print("Tarifa comercial aplicada – consulte o plano corporativo.")

        elif tipo_imovel == "apartamento" and consumo_mensal_agua_m3 < 10:				# apto e consumo < 10
            print("Consumo econômico – excelente controle de água!")

        elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo_mensal_agua_m3 <= 25:	# apto || casa && consumo <= 25
            print("Consumo moderado – dentro do padrão residencial.")

        else:
            print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

        consumo_valido = True
    else:
        print("\033[31mApenas valores positivos, por favor!\033[0m")


