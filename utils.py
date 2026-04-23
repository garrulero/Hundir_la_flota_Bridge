"""
Archivo utils.py (Las Herramientas y Reglas)
Contiene la inteligencia del juego y la fábrica de objetos.
"""
import numpy as np

# Clase Tablero: estructura de variables y metodos
class Tablero:
    def __init__(self, nombre):
        # el __init__: Construye el tablero 10x10 vacio
        self.nombre = nombre
        self.matriz = np.full((10, 10), "_")

    def colocar_barco(self, lista_casillas):
        #  Coge las coordenadas ya calculadas y pinta las letras "O".
        for f, c in lista_casillas:
            self.matriz[f, c] = "O"

    def disparar(self, fila, col):
        # Método disparar: Recibe una coordenada, evalúa si es un acierto o fallo, 
        # y marca "X" (tocado) o "A" (agua).
        # comprueba si la casilla a la que se a disparado es 'O' o 'vacia y lo cambia por X o A si toca hacerlo
        if self.matriz[fila, col] == "O":
            self.matriz[fila, col] = "X"
            print("TOCADO")
            return True
        elif self.matriz[fila, col] == "_":
            self.matriz[fila, col] = "A"
            print("AGUA")
            return False
        
        else:
            # si no es O ni _ es que es X o A entonces ya se a disparado
            print("Ya habías disparado aquí.")
            return False

#  pide coordenadas, comprueba límites y solapamientos, y da la orden de colocar el barco
def colocar_barcos_jugador(objeto_tablero, lista_esloras):
    for eslora in lista_esloras:
        print(f"\n--- BARCO DE ESLORA {eslora} ---")
        colocado = False
        
        while not colocado:
            f = int(input("Fila inicial (0-9): "))
            c = int(input("Columna inicial (0-9): "))
            orie = input("Orientación ('V' o 'H'): ").upper()

            piezas = []
            for i in range(eslora):
                if orie == "V":
                    piezas.append((f + i, c))
                else:
                    piezas.append((f, c + i))

            # VERIFICAMOS QUE NO SALGA DEL MAPA
            ultima_f, ultima_c = piezas[-1]
            if ultima_f > 9 or ultima_c > 9:
                print("El barco se sale del tablero. Prueba otra vez.")
                continue 

            # VERIFICAR SOLAPAMIENTO DE BARCOS
            hay_choque = False
            for f_pieza, c_pieza in piezas:
                if objeto_tablero.matriz[f_pieza, c_pieza] == "O":
                    hay_choque = True
                    break
            
            if hay_choque:
                print("Ya hay un barco en esas coordenadas. Prueba otra vez.")
                continue 

            # SI PASA TODO LO EJECITAMOSEJECUTAMOS
            objeto_tablero.colocar_barco(piezas)
            print(f" Barco de {eslora} colocado.")
            print(objeto_tablero.matriz)
            colocado = True

#  Usamos np.random para buscar huecos válidos a ciegas y coloca su flota sin pisar sus propios barcos.
#lo mismo que arribapara el jugsdor pero con random
def colocar_barcos_rival(objeto_tablero, lista_esloras):
    for eslora in lista_esloras:
        colocado = False
        
        while not colocado:
            f = np.random.randint(0, 10)
            c = np.random.randint(0, 10)
            orie = np.random.choice(["V", "H"])

            piezas_teoricas = []
            for i in range(eslora):
                if orie == "V":
                    piezas_teoricas.append((f + i, c))
                else:
                    piezas_teoricas.append((f, c + i))

            # Si se sale del mapa, 'continue' reinicia el bucle al instante
            ultima_f, ultima_c = piezas_teoricas[-1]
            if ultima_f > 9 or ultima_c > 9:
                continue 
            
            # Verificamos que las casillas no estén ocupadas
            hay_choque = False
            for fila_pieza, col_pieza in piezas_teoricas:
                if objeto_tablero.matriz[fila_pieza, col_pieza] == "O":
                    hay_choque = True
                    break 
            
            # Si todo ok, lo pintamos 
            if not hay_choque:
                objeto_tablero.colocar_barco(piezas_teoricas)
                colocado = True