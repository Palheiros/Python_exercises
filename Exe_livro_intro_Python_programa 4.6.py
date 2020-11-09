

km = int(input("A sua viagem será de quantos Km?: "))

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45

print(f"Preço da passagem: R${preco:.2f}")
