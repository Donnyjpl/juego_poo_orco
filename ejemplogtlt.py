class Personaje:
    def __init__(self, nivel):
        self.nivel = nivel
    
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
    
    
    
    def __gt__( self, otro_perso: object ):
        if self.nivel > otro_perso.nivel:
            return [ True if self.exp > otro_perso.exp else False ][0]
        else:
            return False

# Ejemplo de uso
personaje1 = Personaje(516)
personaje2 = Personaje(7)

print(personaje1.probabilidad_ganar(personaje2))  # Imprimirá 0.33
print(personaje2.probabilidad_ganar(personaje1))  # Imprimirá 0.66
print(personaje1.probabilidad_ganar(personaje1))  # Imprimirá 0.5