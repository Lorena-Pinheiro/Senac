class Aluno():
    def __init__(self,nome,matricula,n1,n2,n3,n4):
        self.nome = nome
        self.matricula = matricula
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        
    def media(self):
        self.media = (self.n1+self.n2+self.n3+self.n4)/4
        if self.media >= 6:
            print(f"Média: {self.media}\nAprovado")
        else:
            print(f"Média: {self.media}\nReprovado")
            
            
aluno1 = Aluno("Fulano","fhsjfhsjdk",6,7,10,8)
aluno1.relatorio()