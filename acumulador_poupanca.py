#Programa que simula os ganhos de uma poupança de acordo com o input do usuário

depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros mensal(Ex.: 0.3 para 0.3%): "))
print("")
mês = 1
saldo = depósito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Saldo do mês {mês} é de R${saldo:.2f}.") #:.2f após a variável é para imprimir o resultado com apenas duas casas decimais
    mês += 1 #forma abreviada de mês = mês + 1
print("")
print(f"O ganho obtido com os juros foi de R${saldo-depósito:.2f}.")
