# Programa que simula a compra de produtos e soma dos seus preços
# Ao final deve mostrar a quantidade dos itens e valor a ser pago

soma = 0
total = 0
total_itens = 0

while True:
    print ("Digite o código do produto desejado ou '0' para encerrar:")
    codigo = int(input("\n 1. R$0,50\n 2. R$1,00\n 3. R$4,00\n 4. R$7,00\n 5. R$8,00\n"))
    if codigo == 0:
        break
        
    quantidade = int(input("Digite a quantidade desejada: "))
    total_itens += quantidade

    if codigo == 1:
        soma += 0.50 * quantidade
    elif codigo == 2:
        soma += 1.00 * quantidade
    elif codigo == 3:
        soma += 4.00 * quantidade
    elif codigo == 4:
        soma += 7.00 * quantidade
    elif codigo == 5:
        soma += 8.00 * quantidade
    else: 
        print("Código inválido. Digite de 1 a 5 ou '0' para terminar.")
                
    total = total + soma

print (f"\nObrigado. Você comprou um total de {total_itens} itens no valor de R${soma:.2f}.")
    
