import numpy as np
import random
import clases.clases as cl 

def crear_tablero(tamano=10):
    tabla = np.full((tamano, tamano), "_")
    return tabla

def mostrar_tablero(tablero):
    print("      Y (COLUMNAS)")
    print("    0 1 2 3 4 5 6 7 8 9")
    print("  ---------------------")
    for i in range(10):
        fila_str = " ".join(tablero[i])
        if i == 4:
            print(f"{i} | {fila_str} | X (FILAS)")
        else:
            print(f"{i} | {fila_str} |")
    print("  ---------------------\n")

def colocar_barco(barco, tablero):
    for fila, columna in barco.coordenadas:
        tablero[fila, columna] = "O"

# ATENCIÓN: Ahora recibe 'lista_barcos' para saber a quién está disparando
def disparar(fila, columna, tablero_objetivo, tablero_radar, lista_barcos):
    if tablero_objetivo[fila, columna] == "O":
        tablero_objetivo[fila, columna] = "X"
        tablero_radar[fila, columna] = "X"
        
        # Lógica para comprobar si está HUNDIDO
        barco_tocado = None
        for barco in lista_barcos:
            if (fila, columna) in barco.coordenadas:
                barco_tocado = barco
                break
                
        # Revisamos si todas las casillas de ese barco son "X"
        hundido = True
        for f, c in barco_tocado.coordenadas:
            if tablero_objetivo[f, c] != "X":
                hundido = False
                break
                
        if hundido:
            print(f"💥 ¡TOCADO Y HUNDIDO! (Destruido barco de eslora {barco_tocado.eslora})")
        else:
            print("💥 ¡TOCADO!")
        return True
        
    elif tablero_objetivo[fila, columna] == "_":
        print("💦 ¡AGUA!")
        tablero_objetivo[fila, columna] = "A"
        tablero_radar[fila, columna] = "A"
        return False
    else:
        print("Ya habías disparado en estas coordenadas.")
        return False

def crear_barcos_aleatorios(lista_esloras):
    lista_barcos = []
    tablero_temp = crear_tablero() 
    
    for eslora in lista_esloras:
        colocado = False
        while not colocado:
            orientacion = random.choice(["H", "V"])
            
            if orientacion == "H":
                x = random.randint(0, 9)
                y = random.randint(0, 9 - eslora)
            else:
                x = random.randint(0, 9 - eslora)
                y = random.randint(0, 9)
                
            barco_temp = cl.Barco(x, y, orientacion, eslora)
            
            # LÓGICA ANTI-MUTANTES: Comprobamos la casilla y las de su alrededor (perímetro)
            colision = False
            for f, c in barco_temp.coordenadas:
                # Comprobamos un cuadrado de 3x3 alrededor de la coordenada
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        nf = f + i
                        nc = c + j
                        # Si está dentro del tablero y hay una "O", hay colisión
                        if 0 <= nf <= 9 and 0 <= nc <= 9:
                            if tablero_temp[nf, nc] == "O":
                                colision = True
            
            if not colision:
                lista_barcos.append(barco_temp)
                colocar_barco(barco_temp, tablero_temp)
                colocado = True
                
    return lista_barcos

def crear_barcos_jugador(lista_esloras, tablero):
    lista_barcos = []
    print("--- ALMIRANTE, COLOQUE SU FLOTA ---")
    
    for tamano in lista_esloras:
        barco_valido = False
        while not barco_valido:
            print(f"\n[ POSICIONANDO BARCO DE ESLORA {tamano} ]")
            mostrar_tablero(tablero) 
            
            try:
                x = int(input("Fila inicial (X) [0-9]: "))
                y = int(input("Columna inicial (Y) [0-9]: "))
                ori = input("Orientación (H para horizontal, V para vertical): ").upper()
                
                nuevo_barco = cl.Barco(x, y, ori, tamano)
                
                if len(nuevo_barco.coordenadas) == 0:
                    continue 
                
                fuera_de_rango = False
                for f, c in nuevo_barco.coordenadas:
                    if f < 0 or f > 9 or c < 0 or c > 9:
                        fuera_de_rango = True
                        break
                        
                colision = False
                if not fuera_de_rango:
                    for f, c in nuevo_barco.coordenadas:
                        if tablero[f, c] == "O":
                            colision = True
                            break
                            
                if fuera_de_rango:
                    print("⚠️ Error: El barco se sale del tablero en esa posición.")
                elif colision:
                    print("⚠️ Error: El barco choca con otra nave de tu flota.")
                else:
                    lista_barcos.append(nuevo_barco)
                    colocar_barco(nuevo_barco, tablero)
                    barco_valido = True
                    
            except ValueError:
                print("⚠️ Error: Las coordenadas deben ser números enteros.")
                
    return lista_barcos