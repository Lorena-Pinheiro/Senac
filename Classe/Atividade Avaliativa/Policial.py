class Policial:
    
    def __init__(self,nome=None,senha=None,matricula=None,fone=None,email=None,endereco=None):
        self.nome = nome
        self.__senha = senha
        self.matricula = matricula
        self.__fone = fone
        self.__email = email
        self.__endereco = endereco
        
    def cadastro_Policial(self):
        self.nome = input("Nome: ")
        self.__senha = input("Senha: ")
        self.matricula = input("Matrícula: ")
        while True:
            try:
                self.__fone = input("Fone: ")
                break
            except:
                print("Valor Inválido. Digite apenas números")
        self.__email = input("Email: ")
        self.__endereco = input("Endereço: ")
    
    def relatorio_Policial(self):
        print(f"Nome: {self.nome}\nSenha: {self.__senha}\nMatrícula: {self.matricula}\nFone: {self.__fone}\nEmail: {self.__email}\nEndereço: {self.__endereco}")