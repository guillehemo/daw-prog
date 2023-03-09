class coche:
    pass
    def __init__ (self, marca, modelo, color, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindrada = cilindrada
    
    def atributos(self):
        print("La marca es ", self.marca)
        print("El modelo es ", self.modelo)
        print("El color es ", self.color)
        print("La cilindrada es ", self.cilindrada)
        
mi_coche = coche("Mercedes", "C220", "blanco", 2000)
mi_coche.atributos()