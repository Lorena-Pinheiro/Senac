p1,p2,p3=map(float,input("Informe o preço dos 3 produtos: "))
if(p1<p2 and p1<p3):
    print("O pruduto 1 é o mais barato")
elif(p2<p1 and p2<p3):
    print("O pruduto 2 é o mais barato")
else:
    print("O pruduto 3 é o mais barato")