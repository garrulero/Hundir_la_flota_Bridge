class Barco:
    def __init__(self, fila_inicio, col_inicio, orientacion, eslora):
        self.fila = fila_inicio
        self.columna = col_inicio
        self.orientacion = orientacion.upper()
        self.eslora = eslora
        
        self.coordenadas = []
        
        # Si es Horizontal, sumamos a la columna (Y)
        if self.orientacion == "H":
            for i in range(self.eslora):
                self.coordenadas.append((self.fila, self.columna + i))
                
        # Si es Vertical, sumamos a la fila (X)
        elif self.orientacion == "V":
            for i in range(self.eslora):
                self.coordenadas.append((self.fila + i, self.columna))
                
        else:
            print("⚠️ Error: Orientación no válida. Usa 'H' o 'V'.")

    def __str__(self):
        return f"Barco de eslora {self.eslora} ({self.orientacion}) en: {self.coordenadas}"