from entrevistado import Entrevistado
from enum_op import EnumOp


TOTAL_ENTREVISTADOS = 50

entrevistados = set()

loop = 0

print("\n==============================================")
print("Pesquisa de satisfação - TudoWeb")
print("==============================================")

while loop < TOTAL_ENTREVISTADOS:   

    print("Olá! Bem-vindo à pesquisa de satisfação da TudoWeb.")

    while True:
        nome = input("Digite seu nome: ").strip()		# explica strip

        try:
            idade = int(input("Digite sua idade: "))
        except ValueError:
            print("A idade deve ser um número inteiro.")
            continue

        if nome == "":
            print("O nome não pode ficar vazio.")

        elif idade <= 0:
            print("A idade não pode ser negativa.")

        else:            
            break						                    # Os dados são válidos.


   #========================================================= questionário de opinião
    while True:
        try:
            op = int(
                input(
                    "\nQual a sua opinião sobre o atendimento prestado?\n"
                    "1 - EXCELENTE\n"
                    "2 - BOM\n"
                    "3 - RUIM\n"
                    "Digite sua opção: "
                )
            )
        except ValueError:
            print("Digite somente 1, 2 ou 3.")
            continue
        
        if 1 <= op <= 3:					                # Apenas 1, 2 e 3 são valores válidos.
            break

        print("Opção inválida. Digite 1, 2 ou 3.")

    enum_opiniao = EnumOp(op)

    id_entrevistado = loop + 1

    entrevistado = Entrevistado(				            # objeto Entrevistado
        id=id_entrevistado,
        nome=nome,
        idade=idade,
        opiniao=enum_opiniao
    )

    entrevistados.add(entrevistado)				            # add à lista
   
    loop += 1

    faltam = TOTAL_ENTREVISTADOS - loop
    print(f"\nEntrevista cadastrada com sucesso!")

    print("==============================================")
    print(f"Faltam {faltam} entrevistas.\n\n")
    print("==============================================")


# ============================================================ contando resultados
qnt_excelente = 0
qnt_ruim = 0

for entrevistado in entrevistados:
    if entrevistado.opiniao == EnumOp.EXCELENTE:
        qnt_excelente += 1

    if entrevistado.opiniao == EnumOp.RUIM:
        qnt_ruim += 1

print("\n==============================================")
print("RESULTADO FINAL")
print("==============================================")

print(f"Quantidade de respostas EXCELENTE: {qnt_excelente}")
print(f"Quantidade de respostas RUIM: {qnt_ruim}")


# ============================================================ apenas conferindo
print("\nEntrevistados cadastrados:")

for entrevistado in entrevistados:
    print(entrevistado)