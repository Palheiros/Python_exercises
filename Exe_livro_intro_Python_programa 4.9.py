# Simulador de empréstimo imobiliário

valorCasa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o seu salário: R$"))
anosPagar = int(input("Em quantos anos deseja pagar?: "))

meses = anosPagar * 12

if meses <= 72:
    juros = 0.02
elif meses > 72 and meses < 120:
    juros = 0.04
elif meses >= 120 and meses < 240:
    juros = 0.06
else:
    juros = 0.08

prestação = valorCasa / meses
prestaçãoJuros = prestação * juros
prestaçãoFinal = prestação + prestaçãoJuros
valorFinal = valorCasa + (prestaçãoJuros * meses)

print()
print(f"A prestação mensal do imóvel será de R${prestaçãoFinal:.2f} em {meses} meses.")
print(f"Será cobrado {juros}% de juros mensais, no total de R${prestaçãoJuros * meses:.2f}.")
print(f"O valor final do imóvel será de {valorFinal:.2f}.")
print()
if prestaçãoFinal > (salario * 0.30):
    print("Empréstimo não concedido. Parcela maior que 30% do salário.")
else:
    print("Empréstimo aprovado!")
