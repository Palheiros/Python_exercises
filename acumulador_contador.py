x = 1
soma = 0
while x <= 5: # estrutura de repetição. Irá repetir de 1 até 5, depois sai da estrutura.
    n = int(input(f"{x} Digite o número: ")) # faz o input do usuário, colocando o valor na variável 'n' de tipo integral (integer)
    soma = soma + n # Acumulador. A cada repetição a variável soma receberá o seu valor (primeira vez 0) e somará com o valor da variável 'n' (input do usuário)
    x = x + 1 # Contador. A cada repetição a variável 'x' receberá 1, para fazer o controle da estrutura de repetição.
print(f"Média: {soma / 5:.2f}") # Faz o output (imprime) a média dos valores digitados pelo usuário.
