from colorama import init,Fore 
init(autoreset=True)
# Escreva um programa que pede que o usuário informe uma senha.
# O código deve comparar a senha informada pelo usuário com uma senha pré-definida no código armazenada em uma variável 
# Depois o código deve informar se a senha é correta ou incorreta.

# OUTPUT ESPERADO
# Exemplo 1:

# Digite a senha: 123123
# Senha incorreta

# Exemplo 2:

# Digite a senha: AC12
# Senha correta

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|-------------------------------------------|')
print("|-------------SEJA BEM-VINDO----------------|")
print("                                             ") 
senha = input("digite a senha:")
print("                                             ") 

if senha == "AC12":

    print(Fore.GREEN+"SENHA CORRETA!")

else:

     
        print(Fore.RED+"SENHA INCORRETA, por favor tente novamente")



