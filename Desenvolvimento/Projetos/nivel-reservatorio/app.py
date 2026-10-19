from colorama import Fore, Style, init

init(autoreset=False)

# mensagens dos níveis ---------------------------------------------------------------------
niveis = [ 
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)",
]

# chama cor do nível -----------------------------------------------------------------------
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# situação do reservatório -----------------------------------------------------------------
def exibir_situacao(nivel):    
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]
    print(f"{cor}Situação do reservatório: {mensagem}{Style.RESET_ALL}")


# monitoramento ----------------------------------------------------------------------------
print("=== Monitoramento do Reservatório de Água ===\n")

# valores para simulalção
leituras = [3, 2, 1, 2, 3, 4, 5]

for leitura in leituras:
    exibir_situacao(leitura)

print(Style.RESET_ALL + "\nMonitoramento finalizado.")