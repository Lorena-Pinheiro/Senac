class Preso:
    
    def __init__(self,nome=None,acusacao=None,data_nasc=None,sexo=None,endereco=None,condenacao=None):
        self.__nome = nome
        self.__acusacao = acusacao
        self.__data_nasc = data_nasc
        self.__sexo = sexo
        self.__endereco = endereco
        self.__condenacao = condenacao
        
    def cadastro_Preso(self):
        self.__nome = input("Nome: ")
        self.__acusacao = input("Acusação: ")
        self.__data_nasc = input("Data de nascimento: ")
        self.__sexo = input("Sexo: ")
        self.__endereco = input("Endereço: ")
        self.__condenacao = input("Condenação: ")
    
    def relatorio_Preso(self):
        print(f"Nome: {self.__nome}\nAcusação: {self.__acusacao}\nData de Nascimento: {self.__data_nasc}\nSexo: {self.__sexo}\nEndereço: {self.__endereco}\nCondenação: {self.__condenacao}")
        
    
    