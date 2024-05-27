<<<<<<< HEAD
ganho_hora,hora_mes=map(int,input("Informe quanto você ganha por hora e suas horas trabalhadas no mês: ").split())
salario_bruto=ganho_hora*hora_mes
ir=100*0.11
inss=100*0.08
sindicato=100*0.05
desconto=ir+inss+sindicato
salario_liquido=salario_bruto-desconto
=======
ganho_hora,hora_mes=map(int,input("Informe quanto você ganha por hora e suas horas trabalhadas no mês: ").split())
salario_bruto=ganho_hora*hora_mes
ir=100*0.11
inss=100*0.08
sindicato=100*0.05
desconto=ir+inss+sindicato
salario_liquido=salario_bruto-desconto
>>>>>>> 7984deec003c8b61061ac5b10687a7943a1065b0
print("Salário Bruto: %s\nIR: %s\nINSS: %s\nSindicato: %s\nSalário Liquido: %s"%(salario_bruto,ir,inss,sindicato,salario_liquido))