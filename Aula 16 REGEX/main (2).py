import re
codigo = input("Digite um códigão monstruoso ai:")
if re.fullmatch(r"\d{4}", codigo):
    print("Códigão positivo afirmativo tudo correto sem crocodilagem validado")
else:
    print("Códiguinho inválido seu beta ")