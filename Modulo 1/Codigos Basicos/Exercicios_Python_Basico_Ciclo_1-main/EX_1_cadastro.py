# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|-------------------------------------------|')
print("|----------------CADASTRO-------------------|")
print("|-------------SEJA BEM-VINDO----------------|")

print("prencha o formulario abaixo")
print("                                             ")
nome = input(' qual é seu nome? ')
idade = input("qual sua idade? ")
email = input ("digite seu email: ")
senha = input ("crie uma senha" )
print("                                             ") 
print("                                             ")
print("|-------------------------------------------|")
print("|------------ USUÁRIO CADASTRADO -----------|")
print(f"seja bem-vindo {nome}!")
print(f" email:{email}")
print("|-------------------------------------------|")
print("                                             ")
print("obrigado por prencher o formulario!")