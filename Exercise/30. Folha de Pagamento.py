valor_hora,hora_trabalhada=map(int,input("Informe o valor da hora e quantas horas foram trabalhadas no mês: ").split())
salario_bruto=valor_hora*hora_trabalhada
if(salario_bruto<=900):
    inss=salario_bruto*10/100
    fgts=salario_bruto*11/100
    total_desconto=inss
    salario_liquido=salario_bruto-total_desconto
    print("Salário Bruto: R$ %s\nIR: Isento\nINSS: R$ %s\nFGTS: R$ %s\nTotal de descontos: R$ %s\nSalário Liquido: R$ %s"%(salario_bruto,inss,fgts,total_desconto,salario_liquido))
elif(salario_bruto>900 and salario_bruto<=1500):
    ir=salario_bruto*5/100
    inss=salario_bruto*10/100
    fgts=salario_bruto*11/100
    total_desconto=inss+ir
    salario_liquido=salario_bruto-total_desconto
    print("Salário Bruto: R$ %s\nIR: %s\nINSS: R$ %s\nFGTS: R$ %s\nTotal de descontos: R$ %s\nSalário Liquido: R$ %s"%(salario_bruto,ir,inss,fgts,total_desconto,salario_liquido))
elif(salario_bruto>1500 and salario_bruto<=2500):
    ir=salario_bruto*10/100
    inss=salario_bruto*10/100
    fgts=salario_bruto*11/100
    total_desconto=inss+ir
    salario_liquido=salario_bruto-total_desconto
    print("Salário Bruto: R$ %s\nIR: %s\nINSS: R$ %s\nFGTS: R$ %s\nTotal de descontos: R$ %s\nSalário Liquido: R$ %s"%(salario_bruto,ir,inss,fgts,total_desconto,salario_liquido))
elif(salario_bruto>2500):
    ir=salario_bruto*20/100
    inss=salario_bruto*10/100
    fgts=salario_bruto*11/100
    total_desconto=inss+ir
    salario_liquido=salario_bruto-total_desconto
    print("Salário Bruto: R$ %s\nIR: %s\nINSS: R$ %s\nFGTS: R$ %s\nTotal de descontos: R$ %s\nSalário Liquido: R$ %s"%(salario_bruto,ir,inss,fgts,total_desconto,salario_liquido))