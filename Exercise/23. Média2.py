n1,n2=map(int,input("Informe as duas notas do aluno: ").split())
media=(n1+n2)/2
if(media>=7):
    print("Aprovado")
elif(media==10):
    print("Aprovado com distinção")
else:
    print("Reprovado")
