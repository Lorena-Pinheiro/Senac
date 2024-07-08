class Funcionario():
    def __init__(self,nome,cargo,salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def impostos(self,inss,fgts):
        self.impostos = inss + fgts
        
    def beneficios(self,b1,b2,b3):
          self.beneficios = b1 + b2 + b3
          
    def salario_liquido(self):
        salario = self.salario + self.beneficios - self.impostos
        return salario