import numpy as np

"""Aqui se definen la variables de la Ecuación General donde: D (Distancia), A (Autonomía), C_g (Costo Gasoil), T (Capacidad del Tanque), C_v (Costo de Viaticos),
C_p (Cosot Peaje), C_r (Cosot Repostaje o Recarga de combustible), G_ad (Gastos adicionales)""" 

#C_comb (Es una simplificación de la ecuación, con el fin de hacer economía de código, obtenemos directamente el costo total del Gasoil, directamente teneindo en cuenta la distancia (D) y la autonomía (A) del vehículo.)

#PARA USAR EL CÓDIGO, SEGUIR CORRECTAMENTE LAS INSTRUCCIONES DEL PROGRAMA:

def calcular_costo_total(D, A, C_g, T, C_v=0, C_p=0, C_r=0, G_ad=0):

    # Costo del combustible (Fórmula Simplificada)
    C_comb = (D / A) * C_g
    
    # Preguntar si hay costos de viáticos
    if C_v == 0:
        viaticos = input("¿Hay costos de viáticos? (sí/no): ").strip().lower()
        if viaticos in ('sí', 'si'):
            C_v = float(input("Ingrese el monto de los viáticos: "))
    
    # Preguntar si hay costos de peaje
    if C_p == 0:
        peajes = input("¿Hay costos de peaje? (sí/no): ").strip().lower()
        if peajes in ('sí', 'si'):
            num_peajes = int(input("Ingrese el número de peajes: "))
            C_p = sum([float(input(f"Ingrese el costo del peaje {i+1}: ")) for i in range(num_peajes)])
    
    # Preguntar si hay costos de repostajes
    if C_r == 0:
        repostajes = input("¿Hay costos de repostajes? (sí/no): ").strip().lower()
        if repostajes == 'sí':
            num_repostajes = int(input("Ingrese el número de repostajes: "))
            C_r = sum([float(input(f"Ingrese el costo del repostaje {i+1}: ")) for i in range(num_repostajes)])
    
    # Costo de los repostajes
    num_repostajes = np.ceil(D / (A * T)) - 1
    C_repostajes = num_repostajes * C_r
    
    # Preguntar si hay gastos adicionales
    gastos_adicionales = 0 
    agregar_gastos = input("¿Desea agregar algún gasto adicional? (sí/no): ").strip().lower()
    while agregar_gastos == 'sí':
        G_ad = float(input("Ingrese el monto del gasto adicional: "))
        gastos_adicionales += G_ad
        agregar_gastos = input("¿Desea agregar otro gasto adicional? (sí/no): ").strip().lower()
               
    # Costo total
    C_t = C_comb + C_v + C_p + C_repostajes + gastos_adicionales
    
    return C_t

def comparar_rutas():
    # Solicitar datos generales
    C_g = float(input("Ingrese el costo del combustible por litro: "))
    A = float(input("Ingrese la autonomía del vehículo (km/l): "))
    T = float(input("Ingrese la capacidad total del tanque de combustible (litros): "))
    
    # Solicitar número de rutas
    num_rutas = int(input("Ingrese el número de rutas (1, 2 o 3): "))
    distancias = [float(input(f"Ingrese la distancia de la ruta {i+1} (km): ")) for i in range(num_rutas)]
    
    # Calcular costos para cada ruta
    costos = []
    for i, D in enumerate(distancias):
        print(f"\nCalculando costos para la ruta {i+1}:")
        costo = calcular_costo_total(D, A, C_g, T)
        costos.append(costo)
        print(f"Costo total de la ruta {i+1}: {costo:.2f} $")
    
    # Determinar la ruta más económica
    ruta_mas_economica = np.argmin(costos) + 1
    print(f"\nSugiero que elija la ruta N° {ruta_mas_economica}, para realizar su próximo viaje.")

# Ejecutar la comparación de rutas
comparar_rutas()