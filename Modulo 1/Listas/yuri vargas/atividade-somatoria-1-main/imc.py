from colorama import init, Fore
init(autoreset=True) 



print("|-------------SEJA BEM-VINDO----------------|")
print("                                             ")

nome = input("Qual é seu nome? ")


print("                                             ")

peso = float(input(" informe o seu peso: "))
print("                                             ")
altura = float(input("qual é sua altura:"))

imc = peso / (altura ** 2)                                             

print("| Faixa de IMC        | Classificação                  |")
print("|---------------------|--------------------------------|")
print("| < 18.5              | Abaixo do peso                 |")
print("| 18.5 – 24.9         | Peso normal                    |")
print("| 25.0 – 29.9         | Sobrepeso                      |")
print("| 30.0 – 34.9         | Obesidade Grau I               |")
print("| 35.0 – 39.9         | Obesidade Grau II              |")
print("| ≥ 40.0              | Obesidade Grau III (mórbida)   |")

print("                                             ")

print(f"Hola {nome}")
print(f"Sua altura é {altura:.2f}")

print("                                             ")


if imc <= 18.5:

    print("Você esta a baixo do Peso ")
    print(Fore.YELLOW+"Se Alinmente Corretamente!")

elif imc <= 24.9:

    print("Você esta Com peso Normal ")
    print(Fore.GREEN+"Parabéns, Você Esta se alimentando corretamente!")
elif imc <=29.9:

    print("Você esta Com sobre peso Obeso ")
    print(Fore.YELLOW+"Come-se a se cuidar seu Nivel de Obesidade esta Grau I ")
elif imc <= 39.9:

    print("Você esta com  grau Obesidade II ")
    print(Fore.YELLOW+"Procure Fazer Dieta")
else:

    print("Você esta com garu  Obesidade III ")
    print(Fore.RED+"Você esta obeso(a) Prucure fazer Dieta ")
    print("                                             ")
    print(Fore.MAGENTA+"Preserve a Sua Saude, pois ela é muito inportante patra Você")

