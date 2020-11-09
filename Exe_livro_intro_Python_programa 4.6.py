#Pergunta a distância da viagem e retorna o preço da passagem
#Viagens de até 200Km preço de 0,50 por km e acima 0,45.

km = int(input("A sua viagem será de quantos Km?: "))

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45

print(f"Preço da passagem: R${preco:.2f}")
