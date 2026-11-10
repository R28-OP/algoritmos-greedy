def cobertura_antenas(casas, R):
    # Paso previo: Asegurar que las casas estén ordenadas
    casas.sort()
    
    antenas = []
    i = 0
    n = len(casas)

    while i < n:
        # Primera casa sin cobertura
        casa_sin_cobertura = casas[i]
        
        # Posición óptima greedy para la antena
        pos_antena = casa_sin_cobertura + R
        antenas.append(pos_antena)
        
        # Avanzar el índice pasando todas las casas cubiertas por esta antena [pos - R, pos + R]
        limite_derecho = pos_antena + R
        while i < n and casas[i] <= limite_derecho:
            i += 1

    return antenas

# --- Ejemplos de Ejecución ---
if __name__ == "__main__":
    print("=== EJEMPLO 1 ===")
    casas1 = [1, 2, 7, 11, 20, 21, 30]
    R1 = 5
    antenas1 = cobertura_antenas(casas1, R1)
    print(f"Casas: {casas1}")
    print(f"Rango de cobertura R: {R1}")
    print(f"Antenas colocadas en posiciones: {antenas1}")
    print(f"Cantidad total de antenas: {len(antenas1)}\n")

    print("=== EJEMPLO 2 ===")
    casas2 = [2, 4, 8, 15, 18, 22]
    R2 = 3
    antenas2 = cobertura_antenas(casas2, R2)
    print(f"Casas: {casas2}")
    print(f"Rango de cobertura R: {R2}")
    print(f"Antenas colocadas en posiciones: {antenas2}")
    print(f"Cantidad total de antenas: {len(antenas2)}")
