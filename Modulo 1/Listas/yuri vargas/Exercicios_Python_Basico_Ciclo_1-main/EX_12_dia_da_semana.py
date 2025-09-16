from colorama import init,Fore 
init(autoreset=True)
# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado
# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

numero = int(input("digite um nomero"))

if numero == 1:
    print(Fore.BLACK+'Domingo')

elif numero == 2:
    print(Fore.BLACK+"segunda")

elif numero == 3:
    print(Fore.BLACK+"terça ")

elif numero == 4:
    print(Fore.BLACK+"quarta")

elif numero == 5:
    print(Fore.BLACK+"quinta")

elif numero == 6:
    print(Fore.BLACK+"sexta")

elif numero == 7:
    print(Fore.BLACK+"sabado")


else:

    print(Fore.RED+"numero incorreto")

