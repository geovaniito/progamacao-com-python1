import re
codigo = input("Digite sua senhona monstruosa ai(contendo 5 letras ou numeros):")
while not re.fullmatch(r"[a-z0-9]{5}", codigo):
    codigo = input("Digite denovo sua senha monstruosa ai:")


print("Senha aceitada")


