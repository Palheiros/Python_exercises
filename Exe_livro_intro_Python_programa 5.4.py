#Programa que pede um número para contagem e se será uma contagem normal, de números ímpares ou pares

n = int(input("A contagem deverá ir até qual número?: "))
escolha = input("Contagem (n)ormal, números (p)ares ou (i)mpares?: ")

x = 0
if escolha == "n": #Eu poderia ter escolhido a estrutura switch, porém não era a proposta do livro
    while x <= n: #enquanto x for menor ou igual ao número escolhido (n) irá acontecer a repetição
        print(x)
        x = x + 1
elif escolha == "p":
    while x <= n:
        if x %2 == 0: #Aqui a condicional if testa se o número é par com o resto da divisão por 2. O resultado "0" indica o número par.
            print(x)
        x = x + 1
elif escolha == "i":
    while x <= n:
        if x %2 != 0:
            print(x)
        x = x + 1
else:
    print("Escolha inválida. Escolha n, p ou i.")
