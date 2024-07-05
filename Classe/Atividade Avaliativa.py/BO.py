class BO:
    
    def __init__(self,tipo=None,vitima=None,acusado=None,fone_vitima=None,email_vitima=None,endereco_vitima=None):
        self.tipo = tipo
        self.__vitima = vitima
        self.acusado = acusado
        self.__fone_vitima = fone_vitima
        self.__email_vitima = email_vitima
        self.__endereco_vitima = endereco_vitima
        
    def cadastro_BO(self):
        self.tipo = input("Tipo: ")
        self.__vitima = input("Vítima: ")
        self.acusado = input("Acusado: ")
        while True:
            try:
                self.__fone_vitima = input("Fone da Vítima: ")
                break
            except:
                print("Valor Inválido. Digite apenas números")
        self.__email_vitima = input("Email da Vítima: ")
        self.__endereco_vitima = input("Endereço da Vítima: ")
        
    def relatorio_BO(self):
        print(f"Tipo: {self.tipo}\nVítima: {self.__vitima}\nAcusado: {self.acusado}\nFone da Vítima: {self.__fone_vitima}\nEmail da Vítima: {self.__email_vitima}\nEndereço: {self.__endereco_vitima}")
           