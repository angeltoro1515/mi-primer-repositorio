

#if edad >=18: 
    #print("eres mayor de edad")

#elif edad <= 13:
    #print("eres un adolecente kawai")

#else:
    #print("eres un niño tonto")


#frutas = ["pera", "manzana", "mango" , "kiwi", "patilla"]
#for animales in frutas:
    #print(animales)




#contador = 2
#while contador <10: 
 #print(contador)
 #contador += 2 





#precios = [10, 20, 30, 40]
#presio = [precio * 2 for precio in precios]
#print(presio)



#animales = [10, 24, 8, 13]
#num1= [num for num in animales if num > 15]
#print(num1)







base_de_datos_de_dinosaurios=[
    ("tyrannosaurio", "T. rex", "carnivoro", "cretacico"
     "triceratops", "herbivero", "cretacico"
      "Stegosaurus", "herbivero", "jurasico tardido"
       "diplodocius", "herbivoro", "jurasico tardido"
        "velociraptor", "carnivoro", "cretacico tardido" )]

def buscar_dinos_por_nombre(base_de_datos, nombre_dino):
   for dino in base_de_datos_de_dinosaurios:

       if dino[0] == nombre_dino:




def mostrar_dinos():
    for dino in base_de_datos_de_dinosaurios:
     print("dino")

def menu():
   print("1.- Mostrar Todos los Dinosaurios")
   print("2.- Buscar Dinosaurio por nombre")
   print("3.- Buscar Dinosaurio por dieta")
   print("4.- Buscar Dinosaurio por periodo")
   print("5.- Salir")

print("=== DINOSAURIOS DISPONIBLES EN JURASSIC PARK ===")
menu()
opcion = int(input("ingresa el numero del dinosaurio que quieres del (1,5)"))

if opcion == 1:
      mostrar_dinos()

      if opcion == 2:
         print

if opcion == 5:
      print("Saliendo.. nos vemos")

      





