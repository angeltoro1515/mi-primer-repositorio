def obtener_siguiente_estacion(metro, linea, estacion_actual):
    siguiente= metro[linea],[estacion_actual],["estacion_siguiente"][0]
    tiempo= metro[linea],[estacion_actual],["tiempo_estimado"]
    return f"de {estacion_actual} vas a {siguiente} y tarda {tiempo} min."


