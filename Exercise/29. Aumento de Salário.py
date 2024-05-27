salario=int(input("Informe o seu salário: "))
if(salario<280):
    percentual=1.20
    aumento=percentual*salario
    valor_aumento=aumento-salario
    print("Salário Inicial: R$%s\nPercentual do Aumento: %s\nValor do Aumento: R$%s\nSalário Final: R$%s"%(salario,percentual,valor_aumento,aumento))
elif(salario>=280 and salario<700):
    percentual=1.15
    aumento=percentual*salario
    valor_aumento=aumento-salario
    print("Salário Inicial: R$%s\nPercentual do Aumento: %s\nValor do Aumento: R$%s\nSalário Final: R$%s"%(salario,percentual,valor_aumento,aumento))
elif(salario>=700 and salario<1500):
    percentual=1.10
    aumento=percentual*salario
    valor_aumento=aumento-salario
    print("Salário Inicial: R$%s\nPercentual do Aumento: %s\nValor do Aumento: R$%s\nSalário Final: R$%s"%(salario,percentual,valor_aumento,aumento))
elif(salario>=1500):
    percentual=1.05
    aumento=percentual*salario
    valor_aumento=aumento-salario
    print("Salário Inicial: R$%s\nPercentual do Aumento: %s\nValor do Aumento: R$%s\nSalário Final: R$%s"%(salario,percentual,valor_aumento,aumento))