from enum import Enum

class Tipo_arma(Enum):
    Puñetazo=1
    Patada=2
    Codazo=3
    Cabezazo=4


class Pokemon:
    def __init__(self, ID, nombre, tipo_arma, salud, defensa):
        
        lista_IDs=[]
        
        if ID not in lista_IDs:
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
            raise TypeError("El el tipo de arma debe ser uno de estos 4: Puñetazo, Patada, Codazo o Cabezazo")

        if isinstance(salud, int)==True and salud>=1 and salud <=100:
            pass
        else:
            raise TypeError("La salud debe ser un entero del 1 al 100")
        
        if isinstance(defensa, int)==True and defensa>=1 and defensa <=10:
            pass
        else:
            raise TypeError("La defensa debe ser un entero entre el 1 y el 10")


        self.ID=ID
        self.nombre=nombre
        self.tipo_arma=tipo_arma
        self.salud=salud
        self.ataque=Tipo_arma.tipo_arma.value
        self.defensa=defensa
        self.alive=True

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

    def get_defensa(self):
        return self.defensa

    def set_ID(self, ID):
        self.ID=ID

    def set_nombre(self, nombre):
        self.ID=nombre
    
    def set_tipo_arma(self, tipo_arma):
        self.ID=tipo_arma
    
    def set_salud(self, salud):
        self.ID=salud
    
    def set_defensa(self, defensa):
        self.ID=defensa

    def is_alive(self):
        return self.alive
