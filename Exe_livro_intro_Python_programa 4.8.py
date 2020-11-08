x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
operação = str(input("Qual operação deseja (+, -, / ou *): "))

if operação == '+':
    resultado = x + y
elif operação == '-':
    resultado = x - y
elif operação == '/':
    resultado = x / y
elif operação == '*':
    resultado = x * y
else:
    print("Operação inválida")

print(f"Resultado da operação: {resultado:.2f}")
