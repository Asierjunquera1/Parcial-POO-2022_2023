from ejercicio_1 import Pokemon
from ejercicio_1 import Tipo_arma
import random


class Pokemon_tierra(Pokemon):
    def __init__(self, ID, nombre, tipo_arma, salud, ataque, defensa):
        super().__init__(ID, nombre, tipo_arma, salud, ataque, None)
        
        if isinstance(defensa, int)==True and defensa>=11 and defensa <=20:
            pass
        else:
            raise TypeError("La defensa debe ser un entero entre el 11 y el 20")
        
        self.defensa=defensa
    
class Pokemon_agua(Pokemon):
     def __init__(self, ID, nombre, tipo_arma, salud, ataque, defensa):
        super().__init__(ID, nombre, tipo_arma, salud, None, defensa)
        
        if isinstance(ataque, int)==True and defensa>=11 and defensa <=20:
            pass
        else:
            raise TypeError("El ataque debe ser un entero entre el 11 y el 20")
        
        self.ataque=ataque

class Pokemon_aire(Pokemon):
    def __init__(self, ID, nombre, tipo_arma, salud, ataque, defensa):
        super().__init__(ID, nombre, tipo_arma, salud, ataque, defensa)
    
    def fight_defense(self, puntos_daño):
        afecta=random.randint(0,1)
        if afecta==0:
            return False
        elif afecta==1:
            super().fight_defense(puntos_daño)

class Pokemon_electricidad(Pokemon):
    def __init__(self, ID, nombre, tipo_arma, salud, ataque, defensa):
        super().__init__(ID, nombre, tipo_arma, salud, ataque, defensa)

    def fight_atack(self, pokemon_a_atacar):
        ataque_doble=random.randint(0,1)
        if ataque_doble==0:
            self.ataque=2*self.ataque
            super().fight_atack(pokemon_a_atacar)
            self.ataque=self.ataque/2
        elif ataque_doble==1:
            super().fight_atack(pokemon_a_atacar)


