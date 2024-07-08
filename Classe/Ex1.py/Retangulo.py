class Retangulo():
    
    def __init__(self,largura,altura):
        self.largura = largura  
        self.altura = altura
        
    def area(self,largura,altura):
        self.area = largura * altura
        return self.area
    
    def perimetro(self,largura,altura):
        self.perimetro = 2 * (largura + altura)
        return self.perimetro