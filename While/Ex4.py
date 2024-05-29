while True:
    op=int(input("1 - Cliente\n0 - Sair"))
    if(op==0):
        print("sair")
        break
    elif(op==1):
        prod=1
        soma=0
        while (prod!=0):
            prod=int(input("Digite o valor do produto: "))
            soma=soma+prod
        print("Total= R$",soma)
        valor=int(input("Digite o valor em dinheiro: "))
        troco=valor-soma
        print("Troco: R$",troco)
