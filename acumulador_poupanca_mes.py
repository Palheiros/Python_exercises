#Programa que simula ganhos e depósitos mensais de uma poupança

depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 0.3 para 0.3%): "))
investimento = float(input("Depósito mensal: "))
mês = 1
saldo = depósito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
    mês = mês + 1
print(f"O ganho obtido com os juros foi de R${saldo-depósito:8.2f}.")