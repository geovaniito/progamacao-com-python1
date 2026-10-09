personagens = []

def criarp():
    nome = input("Digite o nome do seu personagem: ")
    classe = input("Digite sua classe: ")
    nivel = int(input("Digite seu nivel: "))
    
    personagem = {
        "nome": nome, 
        "classe": classe,
        "nivel": nivel,
    }
    personagens.append(personagem)
    
qtd = int(input("Quantas personas almejastes conceber?"))
for i in range(qtd):
    print(f"Sua persona está sendo consubstanciando {i +  1}")
    criarp()

print("---Personas Cridas--")
for personagem in personagens:
    print("Nome: ", personagem["nome"])
    print("Classe: ", personagem["classe"])
    print("Nivel: ", personagem["nivel"])
