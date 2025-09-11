barra = f'|{30*"_"}|'
print(barra)
print("| calculadora")
print(barra)

print("|1- SOMA")
print("|2- subtração")
print("|3- multiplicação ")
print("|4- divisão")
print(barra)
op = int(input("escolha uma das opções: "))
numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o primeiro numero: "))

if op ==1 :
    print(numero1+numero2)

elif op ==2:
    print(numero1-numero2)

elif op ==3:
    print(numero1*numero2)

elif op == 4:
    
    print(numero1/numero2)