from Pessoa import *

class Professor(Pessoa):
    
    def __init__(self, salario,nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.salario = salario
        print(f"---------------\nSeja Bem-Vindo querido Professor!!!\n{super().relatorio}\nSalário: {self.salario}\n---------------")