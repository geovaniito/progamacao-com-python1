'''
def cadastrar_usuario(nome, idade, cidade="Não informado"):
    print(f"Cadastro: {nome}, {idade}, {cidade}")

cadastrar_usuario(idade = 30, cidade = "SJS", nome = "Carlos")
'''

def mostrar_nome():
    nome = "Joao"
    print(nome)

# print(nome) nao funciona
print(mostrar_nome())

numero = 10 #Variavel global
def calculo():
    global numero # Indica que quero usar a variável global
    numero = 20 #Cria uma nova variável local
calcul()
print(numero)