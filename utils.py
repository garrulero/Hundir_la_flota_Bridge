import numpy as np
import utils as ut

def crear_tablero():
    tablero = np.full((10, 10), "_")

    return (tablero)




def colocar_barco(lista_casillas, tablero):
    for casilla in lista_casillas:
        # 'casilla' es una tupla, por ejemplo (8, 5)
        # Extraemos los números:
        f = casilla[0]
        c = casilla[1]
        
        # AQUÍ VA TU IDEA:
        tablero[f, c] = 'O'