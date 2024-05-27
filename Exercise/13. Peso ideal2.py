sexo=int(input("Digite 1 para mulher e 2 para homem: "))
if(sexo==1):
    alt=float(input("Informe a sua altura: "))
    peso=(62.1*alt)-44.7
else:
    alt=float(input("Informe a sua altura: "))
    peso=(72.7*alt)-58
print("Seu peso ideal é %.2s"%peso)