# ============================================================
# SOLUCIÓN: AUDITORÍA DE INVENTARIO Y REABASTECIMIENTO
# Estudiante: Emmanuel Orellano Villazón
# Curso: Fundamentos de Programación - Código: 213022
# Universidad Nacional Abierta y a Distancia - UNAD
# ============================================================

# ------------------------------------------------------------------
# MÓDULO 1: DATOS INICIALES
# Matriz con formato: [Código, Nombre, Stock Actual, Stock Mínimo]
# Se utiliza lista de listas (lista anidada) como estructura de datos
# ------------------------------------------------------------------
inventario = [
    ["ART-001", "Teclado Mecánico",      15,  20],
    ["ART-002", "Monitor 24 pulgadas",    3,  10],
    ["ART-003", "Mouse Inalámbrico",     25,  15],
    ["ART-004", "Cable HDMI 2m",          2,  30],
    ["ART-005", "Memoria RAM 8GB",        8,  10],
    ["ART-006", "Disco Duro 1TB",         0,   5],
    ["ART-007", "Audífonos USB",         12,  12],
]

# ------------------------------------------------------------------
# MÓDULO 2: FUNCIÓN PRINCIPAL
# calcular_pedido(): determina la cantidad exacta a solicitar
# para un artículo según su stock actual vs. stock mínimo requerido
# ------------------------------------------------------------------
def calcular_pedido(stock_actual, stock_minimo):
    """
    Calcula la cantidad de unidades a pedir para un artículo.

    Parámetros:
        stock_actual  (int): Unidades disponibles actualmente.
        stock_minimo  (int): Nivel mínimo requerido de inventario.

    Retorna:
        int: Cantidad a pedir (0 si el stock es suficiente).
    """
    # Estructura condicional: si el stock actual es menor al mínimo
    if stock_actual < stock_minimo:
        # La cantidad a pedir es la diferencia para cubrir el mínimo
        cantidad_a_pedir = stock_minimo - stock_actual
        return cantidad_a_pedir
    else:
        # El stock es suficiente, no se necesita pedir
        return 0

# ------------------------------------------------------------------
# MÓDULO 3: FUNCIÓN DE CLASIFICACIÓN DE ESTADO
# Clasifica el estado del stock para el informe visual
# ------------------------------------------------------------------
def clasificar_estado(stock_actual, stock_minimo):
    """
    Clasifica el estado del inventario de un artículo.

    Retorna:
        str: "CRÍTICO", "NORMAL" o "EXCEDENTE"
    """
    if stock_actual == 0:
        return "CRÍTICO"
    elif stock_actual < stock_minimo:
        return "BAJO"
    elif stock_actual == stock_minimo:
        return "JUSTO"
    else:
        return "OK"

# ------------------------------------------------------------------
# MÓDULO 4: FUNCIÓN PARA GENERAR EL INFORME COMPLETO
# Recorre la matriz con un ciclo for y muestra los resultados
# ------------------------------------------------------------------
def generar_informe(inventario):
    """
    Recorre el inventario y genera el informe de auditoría.
    Utiliza ciclo for para iterar sobre cada artículo de la matriz.
    """
    print("=" * 75)
    print("       SISTEMA DE AUDITORÍA DE INVENTARIO - UNAD TECH STORE")
    print("=" * 75)
    print(f"{'Código':<10} {'Nombre':<25} {'S.Actual':>9} {'S.Mínimo':>9} {'A.Pedir':>8} {'Estado':<10}")
    print("-" * 75)

    # Lista para acumular artículos que necesitan pedido
    lista_pedidos = []
    total_articulos = 0
    articulos_con_pedido = 0

    # CICLO FOR: recorre cada fila (artículo) de la matriz inventario
    for articulo in inventario:
        # Se extraen los datos de cada posición de la sublista
        codigo       = articulo[0]
        nombre       = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        # Se llama a la función calcular_pedido para obtener la cantidad
        cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

        # Se llama a la función clasificar_estado para el estado visual
        estado = clasificar_estado(stock_actual, stock_minimo)

        # Se imprime la fila del artículo en formato tabular
        print(f"{codigo:<10} {nombre:<25} {stock_actual:>9} {stock_minimo:>9} {cantidad_pedir:>8} {estado:<10}")

        # Si se necesita pedir, se agrega a la lista de pedidos
        if cantidad_pedir > 0:
            lista_pedidos.append([nombre, cantidad_pedir, estado])
            articulos_con_pedido += 1

        total_articulos += 1

    print("-" * 75)
    print(f"  Total artículos auditados: {total_articulos}  |  Artículos con pedido pendiente: {articulos_con_pedido}")

    # Se retorna la lista de pedidos para usarla en otra función
    return lista_pedidos

# ------------------------------------------------------------------
# MÓDULO 5: FUNCIÓN PARA MOSTRAR LA LISTA DE PEDIDOS
# ------------------------------------------------------------------
def mostrar_lista_pedidos(lista_pedidos):
    """
    Muestra únicamente los artículos que requieren reabastecimiento.
    """
    print("\n" + "=" * 50)
    print("       LISTA DE PEDIDOS A REALIZAR")
    print("=" * 50)

    # Verificar si hay pedidos pendientes (condicional)
    if len(lista_pedidos) == 0:
        print("  ✔  Todo el inventario está en niveles óptimos.")
    else:
        print(f"  {'Artículo':<28} {'Cantidad':>8}  {'Estado'}")
        print("-" * 50)

        # CICLO FOR: recorre la lista de pedidos generada
        for pedido in lista_pedidos:
            nombre    = pedido[0]
            cantidad  = pedido[1]
            estado    = pedido[2]
            print(f"  {nombre:<28} {cantidad:>8}  {estado}")

        print("-" * 50)
        total_unidades = 0
        for pedido in lista_pedidos:
            total_unidades += pedido[1]
        print(f"  TOTAL DE UNIDADES A PEDIR: {total_unidades}")

    print("=" * 50)

# ------------------------------------------------------------------
# MÓDULO 6: FUNCIÓN PRINCIPAL main()
# Punto de entrada del programa - orquesta todos los módulos
# ------------------------------------------------------------------
def main():
    print("\n")
    # Llamada a la función que genera el informe y retorna pedidos
    lista_pedidos = generar_informe(inventario)
    # Llamada a la función que muestra solo los artículos a pedir
    mostrar_lista_pedidos(lista_pedidos)
    print("\n  Auditoría finalizada exitosamente.")
    print("  Sistema desarrollado por: Emmanuel Orellano Villazón")
    print("  UNAD - Fundamentos de Programación - 2026\n")

# ------------------------------------------------------------------
# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------------------------------------------
if __name__ == "__main__":
    main()
