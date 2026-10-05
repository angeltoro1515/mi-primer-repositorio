from metro_caracas import metro_Caracas
from funciones import obtener_siguiente_estacion


print("=== BIENVENIDO AL METRO DE CARACAS ===")

linea_usuario= input("ingrea la linea del emtro que te encuentras (linea1 o linea2)")
estacion_usuario= input("ingresa el estacion que te encuentras")

resultado= obtener_siguiente_estacion(metro_Caracas, linea_usuario, estacion_usuario)
print("\n" + resultado)
