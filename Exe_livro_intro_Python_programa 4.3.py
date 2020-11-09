#Algoritmo que lê três valores, imprimindo o menor e o maior

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

maior = a
if b > a and b > c:
          maior = b
if c > a and c > b:
          maior = c
menor = a
if b < a and b < c:
          menor = b
if c < b and c < a:
          menor = c
print("")
print(f"O menor valor digitado foi {menor}.")
print(f"O maior valor digitado foi {maior}.")
