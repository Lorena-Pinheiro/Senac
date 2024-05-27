<<<<<<< HEAD
#Faça um programa que leia o nome de um produto, a quantidade comprada, o valor unitário e o percentual de desconto a ser aplicado para o pagamento.
#Imprima na tela o nome do produto e ovalor total da venda.

nome=input("Informe o nome do produto: ")
quant=int(input("Informe a quantidade comprada: "))
valor=float(input("Informe o valor unitário: "))
desc=int(input("Informe o percentual de desconto: "))
valt=(desc/100)*(valor*quant)
=======
#Faça um programa que leia o nome de um produto, a quantidade comprada, o valor unitário e o percentual de desconto a ser aplicado para o pagamento.
#Imprima na tela o nome do produto e ovalor total da venda.

nome=input("Informe o nome do produto: ")
quant=int(input("Informe a quantidade comprada: "))
valor=float(input("Informe o valor unitário: "))
desc=int(input("Informe o percentual de desconto: "))
valt=(desc/100)*(valor*quant)
>>>>>>> 7984deec003c8b61061ac5b10687a7943a1065b0
print(f"{nome}: R$ {valt}")