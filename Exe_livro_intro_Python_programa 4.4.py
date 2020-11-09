#algoritmo que pergunta o salário de um funcionário e calcula o valor do aumento
#Se o salário for > R$3000 aumento de 10%, se < aumento de 15%

salario = float(input("Digite seu salário: "))
pc_aumento = 0.15
if salario > 3000:
    pc_aumento = 0.10
aumento = salario * pc_aumento
novoSalario = salario + aumento
print(f"Seu aumento será de: R$ {aumento:.2f}")
print(f"Valor do novo salário: R${novoSalario:.2f}")
