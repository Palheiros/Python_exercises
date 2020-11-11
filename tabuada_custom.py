# Tabuada onde o usuário escolhe o início e fim da mesma

n = int(input("Tabuada de: "))
inicio = int(input("Começo: "))
fim = int(input("Fim: "))
print("")
x = inicio
while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1
