import utils as ut
import numpy as np


tablero_jugador_barcos=ut.Tablero("tablero_jugador_barcos")
tablero_jugador_disparos=ut.Tablero("tablero_jugador_disparos")
tablero_rival_barcos=ut.Tablero("tablero_rival_barcos")
tablero_rival_disparos=ut.Tablero("tablero_rival_disparos")

print(tablero_jugador_barcos.matriz)
barco1x = int(input("dime la ubicacion(fila) del barco1:"))

barco1y = int(input("dime la ubicacion(columna) del barco1:"))
barco1orie =input("Orientación ('V' o 'H'): ").upper()
if barco1orie == "V":
    barco1y_2 = barco1y
    barco1x_2=barco1x+1
else:
    barco1y_2 = barco1y+1
    barco1x_2=barco1x

listabarco1 = [(barco1x, barco1y), (barco1x_2, barco1y_2)]


tablero_jugador_barcos.colocar_barco(listabarco1)


print(tablero_jugador_barcos.matriz)