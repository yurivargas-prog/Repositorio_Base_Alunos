# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|-------------------------------------------|')
print("|-------------SEJA BEM-VINDO----------------|")
print("                                             ") 
print("aluguel de carros:" )
dias = int(input("quantos km o carro percorreu"))
km = float(input("quantos dias o carro foi alugado? "))
print("                                             ") 
total_dias = (dias * 60)
total_km = (km * 500 )
valor_total = (total_dias + total_km)

print(f"vc andou {km}km por {dias}dias, então o preço a pagar é R${valor_total:.2f}")