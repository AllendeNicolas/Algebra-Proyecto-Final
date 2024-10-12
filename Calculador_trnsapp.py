import numpy as np

"""Aqui se definen la variables de la Ecuación General donde: (Distancia), (Autonomía), (Costo Gasoil), (Capacidad del Tanque), C_v (Costo de Viaticos),
(Cosot Peaje), (Cosot Repostaje o Recarga de combustible), G_ad (Gastos adicionales)""" 

#C_comb (Es una simplificación de la ecuación, con el fin de hacer economía de código, obtenemos directamente el costo total del Gasoil, directamente teneindo en cuenta la distancia (D) y la autonomía (A) del vehículo.)

#PARA USAR EL CÓDIGO, SEGUIR CORRECTAMENTE LAS INSTRUCCIONES DEL PROGRAMA:

def calcular_costo_total(distancia, autonomia, precio_gasoil, capacidad_tanque, costo_viaticos=0, costo_peaje=0, costo_repostaje=0, gastos_adicionales=0):

    # Costo del combustible (Fórmula Simplificada)
    costo_combustible = (distancia / autonomia) * precio_gasoil
    
    # Preguntar si hay costos de viáticos
    if costo_viaticos == 0:
        viaticos = input("¿Hay costos de viáticos? (sí/no): ").strip().lower()
        if viaticos in ('sí', 'si'):
            costo_viaticos = float(input("Ingrese el monto de los viáticos: "))
    
    # Preguntar si hay costos de peaje
    if costo_peaje == 0:
        peajes = input("¿Hay costos de peaje? (sí/no): ").strip().lower()
        if peajes in ('sí', 'si'):
            num_peajes = int(input("Ingrese el número de peajes: "))
            costo_peaje = sum([float(input(f"Ingrese el costo del peaje {i+1}: ")) for i in range(num_peajes)])
    
    # Preguntar si hay costos de repostajes
    if costo_repostaje == 0:
        repostajes = input("¿Hay costos de repostajes? (sí/no): ").strip().lower()
        if repostajes in ('sí', 'si'):
            num_repostajes = int(input("Ingrese el número de repostajes: "))
            costo_repostaje = sum([float(input(f"Ingrese el costo del repostaje {i+1}: ")) for i in range(num_repostajes)])
    
    # Costo de los repostajes
    num_repostajes = np.ceil(distancia / (autonomia * capacidad_tanque)) - 1
    total_repostajes = num_repostajes * costo_repostaje
    
    # Preguntar si hay gastos adicionales
    gastos_adicionales = 0 
    agregar_gastos = input("¿Desea agregar algún gasto adicional? (sí/no): ").strip().lower()
    while agregar_gastos in ('sí', 'si'):
        gastos_adicionales = float(input("Ingrese el monto del gasto adicional: "))
        gastos_adicionales += gastos_adicionales
        agregar_gastos = input("¿Desea agregar otro gasto adicional? (sí/no): ").strip().lower()
               
    # Costo total
    costo_total_viaje = costo_combustible + costo_viaticos + costo_peaje + total_repostajes + gastos_adicionales
    
    return costo_total_viaje

def comparar_rutas():
    # Solicitar datos generales
    precio_gasoil = float(input("Ingrese el costo del combustible por litro: "))
    autonomia = float(input("Ingrese la autonomía del vehículo (km/l): "))
    capacidad_tanque = float(input("Ingrese la capacidad total del tanque de combustible (litros): "))
    
    # Solicitar número de rutas
    num_rutas = int(input("Ingrese el número de rutas (1, 2 o 3): "))
    distancias = [float(input(f"Ingrese la distancia de la ruta {i+1} (km): ")) for i in range(num_rutas)]
    
    # Calcular costos para cada ruta
    costos = []
    for i, dist in enumerate(distancias):
        print(f"\nCalculando costos para la ruta {i+1}:")
        costo = calcular_costo_total(dist, autonomia, precio_gasoil, capacidad_tanque)
        costos.append(costo)
        print(f"Costo total de la ruta {i+1}: {costo:.2f} $")
    
    # Determinar la ruta más económica
    ruta_mas_economica = np.argmin(costos) + 1
    print(f"\nSugiero que elija la ruta N° {ruta_mas_economica}, para realizar su próximo viaje.")

# Ejecutar la comparación de rutas
comparar_rutas()