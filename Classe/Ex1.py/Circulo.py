class Circulo():
    def __init__(self,raio):
        self.raio = raio
        
    def area(self,raio):
        self.area = 3.14159*(raio**2)
        return self.area
        
    def perimetro(self,raio):
        self.perimetro = 2*3.14159*raio
        return self.perimetro