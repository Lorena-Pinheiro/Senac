class ContaBancaria:
    
    def __init__(self,nome,saldo,cpf,senha):
        self.nome = nome
        self.__saldo = saldo
        self.__cpf = cpf
        self.__senha = senha
        
    def extrato(self,senha):
        if senha == self.__senha:
            print(f'Saldo: {self.__saldo}')
        else:
            print('Senha Inválida')
            
    def depositar(self,valor):
        self.__saldo += valor
        
    def sacar(self,senha,valor):
        if senha == self.__senha:
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente.')
        else:
            print('Senha Inválida')