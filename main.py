import utils as ut
import numpy as np

# se crean los 4 tableros (objetos-9 a partir de la clase tablero en utils)
tablero_jugador_barcos = ut.Tablero("Mis Barcos")
tablero_jugador_disparos = ut.Tablero("Mis Disparos")
tablero_rival_barcos = ut.Tablero("Barcos Rival")
tablero_rival_disparos = ut.Tablero("Disparos Rival")

# comprobaciones
print("______________PREVIEW TABLERO_____________")
print(tablero_jugador_barcos.matriz)


# cuantos barcos y de que eslora:
config_barcos = [2, 2, 2, 3, 3, 4] 

# SE colocan los barcos del jugador y rival
ut.colocar_barcos_jugador(tablero_jugador_barcos, config_barcos)
ut.colocar_barcos_rival(tablero_rival_barcos, config_barcos)

# se imprimen los tableros
print("\n--- TABLERO RIVAL ---")
print(tablero_rival_barcos.matriz)
print("\n--- TABLERO JUGADOR ---")
print(tablero_jugador_barcos.matriz)


# no hay sistema de turnos asique bucle infinito
while True:
    f_ataque = int(input("Introduce la fila para atacar (0-9): "))
    c_ataque = int(input("Introduce la columna para atacar (0-9): "))

    tablero_rival_barcos.disparar(f_ataque, c_ataque)
    
    print(tablero_rival_barcos.matriz)