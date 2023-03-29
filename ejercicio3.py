from ejercicio_1 import Pokemon
from ejercicio_2 import Pokemon_agua
from ejercicio_2 import Pokemon_tierra
from ejercicio_2 import Pokemon_electricidad

archivo1="coach_1_pokemons.csv"
archivo2="coach_2_pokemons.csv"

def get_data_from_user(archivo_a_leer):
    lista=[]
    with open(archivo_a_leer, "r") as archivo:
        for linea in archivo:
            linea=linea.rstrip()
            lista1=linea.split(",")
            lista.append(lista1)
    return lista


def jugar():
    entrenador1=get_data_from_user(archivo1)
    pokemon1_entrenador1=Pokemon_electricidad(entrenador1[1][1], entrenador1[1][2], entrenador1[1][3], entrenador1[1][4], entrenador1[1][5], entrenador1[1][6])
    pokemon2_entrenador1=Pokemon(entrenador1[2][1], entrenador1[2][2], entrenador1[2][3], entrenador1[2][4], entrenador1[2][5], entrenador1[2][6])
    pokemon3_entrenador1=Pokemon_agua(entrenador1[3][1], entrenador1[3][2], entrenador1[3][3], entrenador1[3][4], entrenador1[3][5], entrenador1[3][6])

    entrenador2=get_data_from_user(archivo2)
    pokemon1_entrenador2=Pokemon_tierra(entrenador2[1][1], entrenador2[1][2], entrenador2[1][3], entrenador2[1][4], entrenador2[1][5], entrenador2[1][6])
    pokemon2_entrenador2=Pokemon(entrenador2[2][1], entrenador2[2][2], entrenador2[2][3], entrenador2[2][4], entrenador2[2][5], entrenador2[2][6])
    pokemon3_entrenador2=Pokemon(entrenador2[3][1], entrenador2[3][2], entrenador2[3][3], entrenador2[3][4], entrenador2[3][5], entrenador2[3][6])
    
    pokemons_entrenador1=[pokemon1_entrenador1, pokemon2_entrenador1, pokemon3_entrenador1]
    pokemons_entrenador2=[pokemon1_entrenador2, pokemon2_entrenador2, pokemon3_entrenador2]

    entrenador1_elige=int(input("Entrenador 1, pulse 1 si elige su pokemon 1, 2 si elige su pokemon 2 y 3 si elige su pokemon 3: "))
    if entrenador1_elige==1:
        pokemon_elegido_entrenador1=pokemons_entrenador1[1]
    elif entrenador1_elige==2:
        pokemon_elegido_entrenador1=pokemons_entrenador1[2]
    elif entrenador1_elige==3:
        pokemon_elegido_entrenador1=pokemons_entrenador1[3]
    else:
        raise ValueError("Debes elegir un numero del 1 al 3")

    
    
    entrenador2_elige=int(input("Entrenador 2, pulse 1 si elige su pokemon 1, dos si elige su pokemon 2 y 3 si elige su pokemon 3: "))
    if entrenador2_elige==1:
        pokemon_elegido_entrenador2=pokemons_entrenador2[1]
    elif entrenador2_elige==2:
        pokemon_elegido_entrenador2=pokemons_entrenador2[2]
    elif entrenador2_elige==3:
        pokemon_elegido_entrenador2=pokemons_entrenador2[3]
    else:
        raise ValueError("Debes elegir un numero del 1 al 3")
    
    print("¡Comienza la pelea!")

    pokemons_muertos_entrenador1=[]
    pokemons_muertos_entrenador2=[]
   
    while len(pokemons_muertos_entrenador1)<3 and len(pokemons_muertos_entrenador2)<3:
        while pokemon_elegido_entrenador1.salud >=1 and pokemon_elegido_entrenador2.salud >=1:
            pokemon_elegido_entrenador1.fight_attack(pokemon_elegido_entrenador2)
            pokemon_elegido_entrenador2.fight_attack(pokemon_elegido_entrenador1)

        if pokemon_elegido_entrenador1.salud <=0 and pokemon_elegido_entrenador2.salud >=0:
            pokemons_muertos_entrenador1.append(pokemon_elegido_entrenador1)
            print("Entrenador 1, tu pokemon ha muerto")
        elif pokemon_elegido_entrenador2.salud <=0 and pokemon_elegido_entrenador1.salud >=0:
            pokemons_muertos_entrenador2.append(pokemon_elegido_entrenador2)
            print("Entrenador 2, tu pokemon ha muerto")

        else:
            pokemons_muertos_entrenador1.append(pokemon_elegido_entrenador1)
            pokemons_muertos_entrenador2.append(pokemon_elegido_entrenador2)
            print("Ambos pokemons han muerto")

        entrenador1_elige=int(input("Entrenador 1, pulse 1 si elige su pokemon 1, 2 si elige su pokemon 2 y 3 si elige su pokemon 3: "))
        while pokemons_entrenador1[entrenador1_elige] in pokemons_muertos_entrenador1:
            entrenador1_elige=int(input("Este pokemon esta muerto, elige otro: "))
        if entrenador1_elige==1:
            pokemon_elegido_entrenador1=pokemons_entrenador1[1]
        elif entrenador1_elige==2:
            pokemon_elegido_entrenador1=pokemons_entrenador1[2]
        elif entrenador1_elige==3:
            pokemon_elegido_entrenador1=pokemons_entrenador1[3]
        else:
            raise ValueError("Debes elegir un numero del 1 al 3")

    
        entrenador2_elige=int(input("Entrenador 2, pulse 1 si elige su pokemon 1, 2 si elige su pokemon 2 y 3 si elige su pokemon 3: "))
        while pokemons_entrenador2[entrenador2_elige] in pokemons_muertos_entrenador2:
            entrenador2_elige=int(input("Este pokemon esta muerto, elige otro: "))
        if entrenador2_elige==1:
            pokemon_elegido_entrenador2=pokemons_entrenador2[1]
        elif entrenador2_elige==2:
            pokemon_elegido_entrenador2=pokemons_entrenador2[2]
        elif entrenador2_elige==3:
            pokemon_elegido_entrenador2=pokemons_entrenador2[3]
        else:
            raise ValueError("Debes elegir un numero del 1 al 3")

    if len(pokemons_muertos_entrenador1)==3 and len(pokemons_muertos_entrenador2)<3:
        print("Entrenador 2, has ganado")
        print("Tu ", pokemon1_entrenador2.nombre ,"quedó con la siguiente vida:", pokemon1_entrenador2.salud, "tu", pokemon2_entrenador2.nombre "con: ", pokemon2_entrenador2.salud , "y tu ", pokemon3_entrenador2.nombre "con: ", pokemon3_entrenador2.salud)    
    elif len(pokemons_muertos_entrenador2)==3 and len(pokemons_muertos_entrenador1)<3:
        print("Entrenador 1, has ganado")
        print("Tu ", pokemon1_entrenador1.nombre ,"quedó con la siguiente vida:", pokemon1_entrenador1.salud, "tu", pokemon2_entrenador1.nombre "con: ", pokemon2_entrenador1.salud , "y tu ", pokemon3_entrenador1.nombre "con: ", pokemon3_entrenador1.salud)
    else:
        print("Habeis quedado empate")
        print("Todos vuestros pokemons han muerto")





if __name__ == "__main__":
    jugar()

    

        


    




    