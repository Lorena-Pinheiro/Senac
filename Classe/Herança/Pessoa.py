class Pessoa():
    
    def __init__(self,nome,idade,endereco,cidade,estado):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        
    def relatorio(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereco}\nCidade: {self.cidade}\nEstado: {self.estado}")