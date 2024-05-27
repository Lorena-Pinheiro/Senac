import math
a,b,c=map(input("Informe os valores de A, B e C: ").split())
if(a==0):
    print("A equação não é de segundo grau")
delta=b**2-4*a*c
if(delta>0):
    x1=-b+math.isqrt(delta)/2*a
    x2=-b-math.isqrt(delta)/2*a
    print("O valor de x1 é %s e o x2 é %s"%(x1,x2))
elif(delta==0):
    x1=-b+math.isqrt(delta)/2*a
    print("O valor de x é %s"%(x1))
else:
    print("A equações não possui raízes reais")