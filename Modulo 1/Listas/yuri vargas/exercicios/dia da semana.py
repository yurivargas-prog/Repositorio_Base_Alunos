from colorama import init, Fore
init(autoreset=True) 
numero = int(input("digite um numero? "))

if numero == 1:
    print('Domingo')

elif numero == 2:
    print("segunda")

elif numero == 3:
    print("terça")

elif numero == 4:
    print("quarta")

elif numero ==5:
    print("quinta")

elif numero == 6:
    print("sexta")

elif numero == 7:
    print("sabado")


else:

    print (Fore.RED+f'numero incorreto')