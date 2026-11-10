class Objeto:
    def __init__(self, nombre, valor, peso):
        self.nombre = nombre
        self.valor = valor
        self.peso = peso
        self.ratio = valor / peso

def mochila_fraccional(capacidad, objetos):
    # Paso Greedy: Ordenar por densidad de valor de mayor a menor
    objetos.sort(key=lambda x: x.ratio, reverse=True)
    
    valor_total = 0.0
    capacidad_restante = capacidad
    resultado = []

    for obj in objetos:
        if capacidad_restante == 0:
            break

        if obj.peso <= capacidad_restante:
            # Tomar objeto completo
            capacidad_restante -= obj.peso
            valor_total += obj.valor
            resultado.append(f"- Objeto {obj.nombre}: 100% (Completo)")
        else:
            # Tomar una fracción del objeto
            fraccion = capacidad_restante / obj.peso
            valor_obtenido = obj.valor * fraccion
            valor_total += valor_obtenido
            resultado.append(f"- Objeto {obj.nombre}: {fraccion*100:.2f}% (Fracción: {capacidad_restante}/{obj.peso})")
            capacidad_restante = 0 # Mochila llena

    return valor_total, resultado

# --- Ejemplos de Ejecución ---
if __name__ == "__main__":
    print("=== EJEMPLO 1 ===")
    cap1 = 50
    objs1 = [Objeto("A", 60, 10), Objeto("B", 100, 20), Objeto("C", 120, 30)]
    v_total1, res1 = mochila_fraccional(cap1, objs1)
    print(f"Capacidad Máxima: {cap1}")
    print("Objetos seleccionados:")
    for r in res1:
        print(r)
    print(f"Valor total obtenido: {v_total1:.2f}\n")

    print("=== EJEMPLO 2 ===")
    cap2 = 25
    objs2 = [Objeto("A", 80, 20), Objeto("B", 100, 10), Objeto("C", 120, 30)]
    v_total2, res2 = mochila_fraccional(cap2, objs2)
    print(f"Capacidad Máxima: {cap2}")
    print("Objetos seleccionados:")
    for r in res2:
        print(r)
    print(f"Valor total obtenido: {v_total2:.2f}")
