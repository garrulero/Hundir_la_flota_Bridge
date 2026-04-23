import numpy as np

#no tengo crear tablero porque se crea al hacer un objeto desde la clase
#colocar_barco esta dentro de la clase
class Tablero:
    def __init__(self, nombre):
        self.nombre = nombre
        # Creamos el tablero de 10x10 para el objeto
        self.matriz = np.full((10, 10), "_")

    def colocar_barco(self, lista_casillas):
        for f, c in lista_casillas:
            self.matriz[f, c] = "O"


