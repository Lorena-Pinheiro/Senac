peso=int(input("Informe o peso de peixes: "))
if(peso>50):
    excesso=peso-50
    multa=(peso-50)*4
    print("Multa: R$ %s\n%s quilos além do limite"%(multa,excesso))
else:
    print("Peso dentro do regulamento de pesca")