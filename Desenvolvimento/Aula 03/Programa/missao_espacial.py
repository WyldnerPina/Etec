nome_astro = input("Digite seu nome completo: ")
dist_da_viagem_km = int(input("Digite a distância da viagem (km): ")) # tbm poderia ser float, apenas optei por int
velo_media_kmh = float(input("Digite a velociadade média da nave (km/h): "))

tempo_em_horas = dist_da_viagem_km/velo_media_kmh
tempo_em_dias = tempo_em_horas/24

print(f"\nAstronauta {nome_astro}, bem-vindo à simulação!\n"
f"A viagem terá uma distância de {dist_da_viagem_km} km.\n"
f"Com velocidade média de {velo_media_kmh:.0f} km/h, o tempo estimado é {tempo_em_horas:.2f} horas ({tempo_em_dias:.2f} dias).\n"
"Boa sorte na missão!\n")  #:.0f p/ ficar similar ao exemplo