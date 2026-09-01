jogos = [
    ['CS2',"ROBLOX","RDR2"], #Jogos de PC
    ["AstroBot", "God Of War", "The Last OF Us"], #Jogos de PS4
    ["Halo", "Forza Horizon", "Gears of War"] #Jogos de Xbox
]
print(len(jogos)) # Quantidade de listas dentro da lista

print("Jogos por plataforma:\n")
print("Jogos de PC: ")
for i in jogos[0]:
    print(i)

print("\nJogos de PS4: ")
for jogo in jogos[1]:
    print(jogo)
    
print("\nJogos de XBOX: ")
for jogo in jogos[2]:
    print(jogo)