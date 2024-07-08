from Pessoa import *

class Aluno(Pessoa):
    
    def __init__(self, mensalidade,nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.mensalidade = mensalidade
        print(f"---------------\nSeja Bem-Vindo querido Aluno!!!\n{super().relatorio()}Mensalidade: {self.mensalidade}\n---------------" )