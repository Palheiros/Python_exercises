#Programa que pede um número para contagem e se será uma contagem normal, de números ímpares ou pares

n = float(input("Deseja múltiplos para qual número?: "))
escolha = int(input("Quantos múltiplos?: "))
print("")

x = 1

while x <= escolha:
    total = n * x
    print(f"{n} * {x} = {total:.2f}")
    x = x + 1
