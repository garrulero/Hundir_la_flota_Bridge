import utils as ut
import random

# --- INICIALIZACIÓN ---
# Creamos tableros del jugador (barcos y radar) y de la máquina (solo barcos)
tablero_jugador = ut.crear_tablero()
tablero_radar = ut.crear_tablero() 
tablero_maquina = ut.crear_tablero()

# Colocamos las dos flotas de forma automática (cumpliendo el requisito mínimo)
ut.colocar_barcos(tablero_jugador)
ut.colocar_barcos(tablero_maquina)

print("--- HUNDIR LA FLOTA ---")
print("\nESTA ES TU FLOTA ALMIRANTE:")
print(tablero_jugador)
print("\n¡Que comience la batalla!")

# --- BUCLE DE TURNOS ---
juego_activo = True
while juego_activo:
    
    # TURNO JUGADOR
    print("\n--- TU TURNO ---")
    print("Radar de impactos:")
    print(tablero_radar)
    
    try:
        fila = int(input("Introduce fila a disparar (0-9): "))
        col = int(input("Introduce columna a disparar (0-9): "))
    except ValueError:
        print("Usa solo números.")
        continue # Vuelve a pedir el dato sin perder el turno

    # Validamos que el disparo esté en el mapa
    if 0 <= fila <= 9 and 0 <= col <= 9:
        # Disparamos. Si devuelve True, es que hemos tocado
        if ut.disparar((fila, col), tablero_maquina):
            print("💥 ¡TOCADO!")
            tablero_radar[fila, col] = "X"
        else:
            print("💦 ¡AGUA!")
            # Marcamos agua en el radar solo si no había ya una X
            if tablero_radar[fila, col] == "_":
                tablero_radar[fila, col] = "A"
                
        # Condición de victoria: no quedan "O" en el tablero rival
        if "O" not in tablero_maquina:
            print("\n🏆 ¡HAS GANADO! ¡Destruiste la flota enemiga!")
            break
    else:
        print("Disparo fuera del mapa.")
        continue # Obliga a repetir el turno del jugador
        
        
    # TURNO MÁQUINA
    print("\n--- TURNO ENEMIGO ---")
    f_maq = random.randint(0, 9)
    c_maq = random.randint(0, 9)
    print(f"El enemigo dispara en: ({f_maq}, {c_maq})")
    
    if ut.disparar((f_maq, c_maq), tablero_jugador):
        print("💥 ¡TE HAN DADO!")
        # Condición de derrota
        if "O" not in tablero_jugador:
            print("\n☠️ ¡HAS PERDIDO! Tu flota ha sido destruida.")
            print(tablero_jugador)
            break
    else:
        print("💦 Disparo enemigo al agua.")
        
print("Fin de la partida.")