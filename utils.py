import numpy as np

#no tengo crear tablero porque se crea al hacer un objeto desde la clase
#colocar_barco esta dentro de la clase
class Tablero:
    def __init__(self, nombre):
        self.nombre = nombre
        # aqui se puede cambiar el tamaño del tablero
        self.matriz = np.full((3, 3), "_")

    def colocar_barco(self, lista_casillas):
        for f, c in lista_casillas:
            self.matriz[f, c] = "O"


