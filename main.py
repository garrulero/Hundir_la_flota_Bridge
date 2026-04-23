import utils as ut
import numpy as np

# 1. Creamos los 4 tableros a partir de la clase
tablero_jugador_barcos = ut.Tablero("Mis Barcos")
tablero_jugador_disparos = ut.Tablero("Mis Disparos")
tablero_rival_barcos = ut.Tablero("Barcos Rival")
tablero_rival_disparos = ut.Tablero("Disparos Rival")
# mostramos el tablero 
print("______________PLANTILLA TABLERO_____________")
print(tablero_jugador_barcos.matriz)
# 2.AQUI CONFIGURAMOS EL NUMERO DE BARCOS A COLOCAR EN EL TABLERO DEL JGADOR Y DEL RIVAL
config_barcos = [2,2] 

# 3. SE COLOCAN LOS BARCOS CON ESTA FUNCION DE CLASE DEL JUGADOR Y DESPUES CON OTRA FUNCION LAS DEL RIVAL
ut.colocar_barcos_jugador(tablero_jugador_barcos, config_barcos)

ut.colocar_config_barcos(tablero_rival_barcos, config_barcos)


#4. IM PRIMIMOS LOS TABLEROS CON LOS BARCOS COLOCADOS
print("\n--- TABLERO RIVAL ---")
print(tablero_rival_barcos.matriz)
print("\n--- TABLERO JUGADOR ---")
print(tablero_jugador_barcos.matriz)


# ==========================================
# 5. FASE DE COMBATE (Bucle de prueba)
# ==========================================
print("\n--- ¡EMPIEZA EL COMBATE! ---")

# Este bucle te dejará disparar infinitas veces para probar el sistema
while True:
    print("\n🎯 TU TURNO")
    try:
        f_ataque = int(input("Introduce la fila para atacar (0-9): "))
        c_ataque = int(input("Introduce la columna para atacar (0-9): "))
        
        print("\nLanzando misil...")
        
        # ¡LA MAGIA OCURRE AQUÍ! 
        # Disparamos directamente contra la matriz donde están los barcos del rival
        tablero_rival_barcos.disparar(f_ataque, c_ataque)
        
        # Imprimimos el tablero del rival para ver si ha aparecido la 'X' o la 'A'
        print(tablero_rival_barcos.matriz)
        
    except ValueError:
        print("❌ Por favor, introduce un número válido.")
    except IndexError:
        print("❌ ¡Apunte bien, Capitán! Esa coordenada se sale del mapa.")