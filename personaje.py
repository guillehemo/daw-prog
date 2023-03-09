class Personaje:
    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    def atributos(self):
        print("Fuerza", self.fuerza)
        print("Inteligencia", self.inteligencia)
        print("Defensa", self.defensa)
        print("Vida",self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    

        
mi_personaje = Personaje("BitBoss", 10, 1, 5, 100)
mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 100)
mi_personaje.morir()
mi_personaje.atributos()


