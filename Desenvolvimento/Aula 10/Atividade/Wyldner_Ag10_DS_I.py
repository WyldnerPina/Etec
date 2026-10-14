def calcularMedia(nota1, nota2):
    return (nota1 + nota2) / 2

def verificarAprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

def gerarRelatorio(nome, nota1, nota2, media, situacao):
    print("\n===== RELATÓRIO DE DESEMPENHO =====")
    print(f"Aluno: {nome}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("==================================")

def main():
    controle = True

    while controle:
        print("\n===== MENU =====")
        print("1 - Calcular média e verificar aprovação")
        print("2 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")

            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))

            media = calcularMedia(nota1, nota2)
            situacao = verificarAprovacao(media)

            gerarRelatorio(nome, nota1, nota2, media, situacao)

        elif opcao == "2":
            controle = False
            print("Programa encerrado.")

        else:
            print("Opção inválida. Tente novamente.")

main()
