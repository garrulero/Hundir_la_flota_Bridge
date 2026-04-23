import numpy as np

class Tablero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.matriz = np.full((4, 4), "_")

    def colocar_barco(self, lista_casillas):
        for f, c in lista_casillas:
            self.matriz[f, c] = "O"

    def disparar(self, fila, col):
        """
        Comprueba si el disparo acierta, falla o está repetido.
        Devuelve True si puedes volver a tirar, False si pierdes el turno.
        """
        if self.matriz[fila, col] == "O":
            self.matriz[fila, col] = "X"
            print("💥 ¡TOCADO!")
            return True
        elif self.matriz[fila, col] == "_":
            self.matriz[fila, col] = "A"
            print("💦 ¡AGUA!")
            return False
        else:
            print("⚠️ Ya habías disparado aquí.")
            return False

def colocar_barcos_jugador(objeto_tablero, lista_esloras):
    """
    Recorre la lista de esloras y pide al usuario coordenadas.
    """
    for eslora in lista_esloras:
        print(f"\n---  BARCO DE ESLORA {eslora} ---")
        colocado = False
        while not colocado:
            try:
                f = int(input("Fila inicial (0-9): "))
                c = int(input("Columna inicial (0-9): "))
                orie = input("Orientación ('V' o 'H'): ").upper()

                piezas = []
                for i in range(eslora):
                    if orie == "V":
                        piezas.append((f + i, c))
                    else:
                        piezas.append((f, c + i))

                # Verificamos límites ANTES de pintar
                ultima_f, ultima_c = piezas[-1]
                if ultima_f > 9 or ultima_c > 9:
                    print("❌ ERROR: El barco se sale del tablero.")
                    continue 

                # Verificamos choques ANTES de pintar
                hay_choque = False
                for f_pieza, c_pieza in piezas:
                    if objeto_tablero.matriz[f_pieza, c_pieza] == "O":
                        hay_choque = True
                        break
                
                if hay_choque:
                    print("❌ ERROR: Ya hay un barco en esas coordenadas.")
                    continue 

                # Si llegamos aquí, es seguro pintar
                objeto_tablero.colocar_barco(piezas)
                print(f"✅ Barco de {eslora} colocado con éxito.")
                print(objeto_tablero.matriz)
                colocado = True
                
            except ValueError:
                print("❌ ERROR: Introduce un número válido.")
            except Exception as e:
                print(f"❌ ERROR inesperado: {e}. Inténtalo de nuevo.")

def colocar_barcos_rival(objeto_tablero, lista_esloras):
    """
    La máquina coloca sus barcos comprobando que no choca con otros ('O') 
    y que no se sale del tablero usando np.random.
    """
    for eslora in lista_esloras:
        colocado = False
        
        while not colocado:
            try:
                # 1. Usamos Numpy (ponemos 10 porque excluye el límite superior)
                f = np.random.randint(0, 10)
                c = np.random.randint(0, 10)
                orie = np.random.choice(["V", "H"])

                # 2. Calculamos las casillas teóricas que ocuparía
                piezas_teoricas = []
                for i in range(eslora):
                    if orie == "V":
                        piezas_teoricas.append((f + i, c))
                    else:
                        piezas_teoricas.append((f, c + i))

                # 3. VERIFICACIÓN DE LÍMITES: ¿Se sale del mapa?
                ultima_f, ultima_c = piezas_teoricas[-1]
                if ultima_f > 9 or ultima_c > 9:
                    raise IndexError 
                
                # 4. VERIFICACIÓN DE CHOQUES: ¿Hay alguna 'O' ya en ese sitio?
                hay_choque = False
                for fila_pieza, col_pieza in piezas_teoricas:
                    if objeto_tablero.matriz[fila_pieza, col_pieza] == "O":
                        hay_choque = True
                        break 
                
                # 5. RESULTADO: Si no hay choque, lo pintamos
                if not hay_choque:
                    objeto_tablero.colocar_barco(piezas_teoricas)
                    colocado = True 

            except IndexError:
                pass