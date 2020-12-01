# Programa que soma números digitados pelo usuário até que se digite '0'.
# Ao final deve mostrar a soma e quantos números foram inseridos

soma = 0
contador = -1

while True:
    v = int(input("Digite um número para somar ou '0' para interromper: "))
    contador += 1
    if v == 0:
        break
    soma += v

print (f"\nForam digitados {contador} números. A soma dos números = {soma}")
