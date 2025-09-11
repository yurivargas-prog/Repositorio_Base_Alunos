# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


print("produto: FIAT TORO")
preco = int(input("preço: "))
porcentagem = int(input("porcentagem de desconto "))
desconto = preco * (porcentagem / 100 )
total = preco - desconto 
print(f"O FIAT TORO com {porcentagem}% de desconto custara R$ {total} ")