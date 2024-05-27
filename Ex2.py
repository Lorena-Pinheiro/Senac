while True:
    operação=input("Digite uma das operações:\nMultiplicação\nDivisão\nAdição\nSubtração\nPara sair digite 'Parar'\n")
    if(operação=="Multiplicação" or operação=="multiplicação"):
        n1=int(input("Digite o primeiro número: "))
        n2=int(input("Digite o segundo número: "))
        conta=n1*n2
        print(f"{n1}*{n2}={conta}")
    elif(operação=="Divisão" or operação=="divisão"):
        n1=int(input("Digite o primeiro número: "))
        n2=int(input("Digite o segundo número: "))
        conta=n1/n2
        print(f"{n1}/{n2}={conta}")
    elif(operação=="Adição" or operação=="adição"):
        n1=int(input("Digite o primeiro número: "))
        n2=int(input("Digite o segundo número: "))
        conta=n1+n2
        print(f"{n1}+{n2}={conta}")
    elif(operação=="Subtração" or operação=="subtração"):
        n1=int(input("Digite o primeiro número: "))
        n2=int(input("Digite o segundo número: "))
        conta=n1-n2
        print(f"{n1}-{n2}={conta}")
    elif(operação=="Parar" or operação=="parar"):
        break
    else:
        print("Operação inválida")