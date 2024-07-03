class ControleRemoto():
    def __init__(self,cor,altura,profundidade,largura):
        self.cor=cor
        self.altura=altura
        self.profundidade=profundidade
        self.largura=largura
        
    def mudar_canal(self,botao):
        if botao=='+':
            print('aumentar canal')
        elif botao=='-':
            print('diminuir canal')
        else:
            print('Valor Inválido')