turno=input("Informe o turno em que você estuda:\nM-matutino\nV-vespertino\nN-noturno")
if(turno=="M" or turno=="m"):
    print("Bom Dia!")
elif(turno=="V" or turno=="v"):
    print("Boa Tarde!")
elif(turno=="N" or turno=="n"):
    print("Boa Noite!")
else:
    print("Valor Inválido")