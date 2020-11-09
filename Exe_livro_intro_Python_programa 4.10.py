#Programa que calcula o preço a pagar pela energia de acordo com a quantidade de kWh consumida
# e tipo de instalação: residência, comércio ou industrial.

quant = int(input("Quantidade de kWh consumida: "))
tipo = input("Informe o tipo de instalação: (r)esidencial, (c)omercial ou (i)ndustrial: ")

if tipo == "r" and quant <= 500:
    preço = quant * 0.40
else:
    preço = quant * 0.65

if tipo == "c" and quant <= 1000:
    preço = quant * 0.55
else:
    preço = quant * 0.60

if tipo == "i" and quant <= 5000:
    preço = quant * 0.55
else:
    preço = quant * 0.60

print("")
print(f"A sua conta será de R${preço}")
