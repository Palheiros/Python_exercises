# Programa que mostra o mínimo de cédulas e moedas para pagar determinado valor digitado pelo usuário
# Atenção: alguns valores não serão calculados corretamente
# devido a problemas com arredondamento e da representação de 0.01
# em ponto flutuante. Uma alternativa é multiplicar todos os valores
# por 100 e realizar todos os cálculos com números inteiros.

valor = float(input("Digite o valor a pagar: R$"))
cedulas = 0
atual = 200
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if atual >= 1:
            print(f"{cedulas} cédula(s) de R${atual}")
        else:
            print(f"{cedulas} moeda(s) de R${atual:.2f}")
        if apagar < 0.01:
            break
        if atual == 200:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        elif atual == 0.01:
            atual = 0.01
        cedulas = 0
