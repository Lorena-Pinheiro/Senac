n1,n2,n3=map(int,input("Digite 3 números: ").split())
if(n1>n2 and n1>n3):
    print("O maior número é %s"%n1)
elif(n2>n1 and n2>n3):
    print("O maior número é %s"%n2)
else: 
    print("O maior número é %s"%n3)