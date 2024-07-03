class Clientes():
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def cadastro(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def alteracao(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def relatorio(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nCpf: {self.cpf}")