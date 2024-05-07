import random
class Personaje:
    def __init__(self,nombre,nivel=1, experiencia=0):
         self.nombre=nombre
         self.nivel=nivel
         self.experiencia=experiencia
         
    def estado(self):
        print(f"NOMBRE:   {self.nombre},   NIVEL:   {self.nivel},   EXP:   {self.experiencia}")


  
    def nombre_jugador(self):
        return self.nombre 
       
    def asignar_estado(self, experiencia):
        if experiencia < 0:
            if self.nivel > 1:
                self.experiencia += experiencia
                while self.experiencia < 0 and self.nivel > 1:
                    self.experiencia += 100
                    self.nivel -= 1
            else:
                self.experiencia = 0  # La experiencia no puede ser negativa si el personaje está en el nivel 1
        else:
            self.experiencia += experiencia
            while self.experiencia >= 100:
                self.experiencia -= 100
                self.nivel += 1        
                   
    def probabilidad_ganar(self, otro_personaje):
        if self > otro_personaje:
            return 0.66
        elif self < otro_personaje:
            return 0.33
        else:
            return 0.5
    
    def __gt__(self, otro_personaje):
        return self.nivel > otro_personaje.nivel
    
    def __lt__(self, otro_personaje):
        return self.nivel < otro_personaje.nivel
    
    def __eq__(self, otro_personaje):
        return self.nivel == otro_personaje.nivel    
        
    @staticmethod
    def juego(probabilidad):
        print("Ha aparecido un orco.")
        print(f"Probabilidad de ganar: {probabilidad * 100}%")
        print("Si ganas, recibirás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        opcion = int(input("¿Deseas atacar (1) o huir (2)? "))
        return opcion    
    
    def ataque(self, probabilidad, otro_personaje):
        resultado = random.uniform(0, 1)
        if resultado <= probabilidad:
            print("\n" * 5)  # Agrega 10 líneas en blanco para mover el texto hacia el medio
            print(" " * 10 + "¡Ganaste!".upper())  # Agrega espacio para centrar el texto y usa mayúsculas
            print("\n" * 5)  # Agrega 10 líneas en blanco al final para desplazar el texto hacia arriba
            self.asignar_estado(50)
            otro_personaje.asignar_estado(-30)
        else:
            print("\n" * 5)  # Agrega 10 líneas en blanco para mover el texto hacia el medio
            print(" " * 10 + "¡Perdiste!".upper())  # Agrega espacio para centrar el texto y usa mayúsculas
            print("\n" * 5)  # Agrega 10 líneas en blanco al final para desplazar el texto hacia arriba
            self.asignar_estado(-30) 
            otro_personaje.asignar_estado(50) 

    
         