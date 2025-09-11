# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


print('|-------------------------------------------|')
print("|-------------SEJA BEM-VINDO----------------|")
print("                                             ")

print("escolha se quer converter  de Reais para Dollar ou Dollar para reais")
print("                                             ")


print("|___________________________________________|")
  
print("escolha uma opção:" )
print("                               ")

print("1- Dollar para Real: ")
print("2- Real para dollar: ")
opcao = input("digite uma opção:")


if opcao == "1":

    dollar = float(input("informe a cotação atual do Dollar:"))


if opcao == "1":
    qt = float(input("enfome a quantidade de dollar"))
    mutiplicacao = qt * dollar


    print(f"o valor em Reais é: R${mutiplicacao}")
elif opcao == "2":


    dollar = float(input("informe a cotação atual do Dollar:"))
    real = float(input("informe a quantidade fe reais:"))
    mutiplicacao =float(f'{real / dollar: .2f}')

    print(f"o valor em dollar é: ${mutiplicacao}")

else:

    print(" numero incorreto, tente novamente")



