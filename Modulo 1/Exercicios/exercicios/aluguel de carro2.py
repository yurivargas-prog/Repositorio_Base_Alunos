barra = f'|{30*"_"}|'
print(barra)
print("| 1- audi" )
print("| 2- mercedes ")
print("| 3- bmw " )
print("| 4- buggat ")
print("| 5- ferrari")
print("| 6- lamborghini" )
'   '
carro = int(input("qual carro foi alugado? "))
km = float(input("qunatos km foram percorridos? "))
dias = int(input("quantos dias o carro foi alugado? "))



if carro == 1:
    diaria = 250 


elif carro == 2:
    diaria = 350

elif carro == 3:
    diaria = 450

elif carro == 4:
    diaria = 550

elif carro == 5:
    diaria = 650

elif carro == 6:
    diaria = 750

total_dias = (dias * diaria)
total_km = (km * 0.15)
valor_total = (total_dias + total_km)

print(f"vc andou {km}km porn {dias} dias o valor total a pagar é {valor_total} ")
