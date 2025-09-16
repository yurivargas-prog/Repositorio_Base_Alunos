from colorama import init,Fore 

# Escreva um programa simples que pede a idade do usuário e 
# depois mostre na tela com valor BOOLEANO (True ou False) se o usuário pode tirar a CNH (Carteira Nacional de Habilitação) ou não.
# Para tirar carteira no Brasil, a idade mínima é 18 anos.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite sua idade: 19
# Pode tirar carteira de motorista? True

# Exemplo 2:
# Digite sua idade: 17
# Pode tirar carteira de motorista? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|-------------------------------------------|')
print("|----------------CADASTRO-------------------|")
print("                                             ")
print("CNH (Carteira Nacional de Habilitação") 
print("                                             ")
print(" é necessario ter mais de 18 anos para tirar a CNH ")
print("                                             ")

nome = input("nome de usuario:")
print("                                             ")
idade = int(input("qual é asua idade:"))


cnh = idade >= 18


if cnh:

    print(Fore.GREEN+f" parabéns, vc ja pode tirar a sua CNH!! ")


else:

    print(Fore.RED+f"vc não pode tirar a sua CNH ")
