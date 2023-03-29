from enum import Enum

class Tipo_arma(Enum):
    punch=1
    kick=2
    elbow=3
    headbutt=4


class Pokemon:
    lista_IDs=[]
    def __init__(self, ID, nombre, tipo_arma, salud, ataque, defensa):
        
        if ID not in Pokemon.lista_IDs:
            pass
        else:
            raise ValueError("Este ID pertenece a otro pokemon")
        if isinstance(ID, int)==True:
            pass
        else:
            raise TypeError("El ID debe ser un entero")

        if isinstance(nombre, str)==True:
            pass
        else:
            raise TypeError("El nombre debe ser una cadena de texto")
        
        if isinstance(tipo_arma, Tipo_arma)==True:
            pass
        else:
            raise TypeError("El el tipo de arma debe ser uno de estos 4: punch, kick, elbow o headbutt")

        if isinstance(salud, int)==True and salud>=1 and salud <=100:
            pass
        else:
            raise TypeError("La salud debe ser un entero del 1 al 100")
        
        if isinstance(ataque, int)==True and ataque>=1 and ataque <=10:
            pass
        else:
            raise TypeError("La ataque debe ser un entero entre el 1 y el 10")

        if isinstance(defensa, int)==True and defensa>=1 and defensa <=10:
            pass
        else:
            raise TypeError("La defensa debe ser un entero entre el 1 y el 10")


        self.ID=ID
        self.nombre=nombre
        self.tipo_arma=tipo_arma
        self.salud=salud
        self.ataque=ataque
        self.defensa=defensa
    
    def __del__(self):
        Pokemon.lista_IDs.remove(self.ID)


    def imprimir(self):
        print("Pokemon ID", self.ID, "con nombre", self.nombre, "tiene como arma", self.tipo_arma, "y salud", self.salud)

    
    def get_nombre(self):
        return self.nombre

    def get_tipo_arma(self):
        return self.tipo_arma

    def get_salud(self):
        return self.salud

    def get_ID(self):
        return self.ID
    
    def get_ataque(self):
        return self.ataque
    
    def get_defensa(self):
        return self.defensa

    
    def set_ID(self, ID):
        self.ID=ID

    def set_nombre(self, nombre):
        self.nombre=nombre
    
    def set_tipo_arma(self, tipo_arma):
        self.tipo_arma=tipo_arma
    
    def set_salud(self, salud):
        self.salud=salud
    
    def set_ataque(self, ataque):
        self.ataque=ataque

    def set_defensa(self, defensa):
        self.defensa=defensa

   
    def is_alive(self):
        return self.salud>0
    
    
    def fight_defense(self, puntos_daño):
        if puntos_daño <= self.defensa:
            return False
        else:
            daño_recibido=puntos_daño-self.defensa
            self.salud-=daño_recibido
            return True

    def fight_atack(self, pokemon_a_atacar):
        pokemon_a_atacar.fight_defense(self.ataque)

    
