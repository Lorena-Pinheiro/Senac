n1,n2,n3=map(int,input("Digite 3 números: ").split())
if(n1>n2 and n1>n3 and n3<n1 and n3<n2):
    print("O maior número é %s\nO menor número é %s"%(n1,n3))
elif(n1>n2 and n1>n3 and n2<n1 and n2<n3):
    print("O maior número é %s\nO menor número é %s"%(n1,n2))
elif(n2>n1 and n2>n3 and n3<n1 and n3<n2):
    print("O maior número é %s\nO menor número é %s"%(n2,n3))  
elif(n2>n1 and n2>n3 and n1<n2 and n1<n3):
    print("O maior número é %s\nO menor número é %s"%(n2,n1))
elif(n3>n1 and n3>n2 and n2<n1 and n2<n3):
    print("O maior número é %s\nO menor número é %s"%(n3,n2))
elif(n3>n1 and n3>n2 and n1<n2 and n1<n3):
    print("O maior número é %s\nO menor número é %s"%(n3,n1))   