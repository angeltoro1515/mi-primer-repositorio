#import random

#numero_secreto = random.randint(1 , 100)

#while True:
  #intento = int(input("ingresa tu numero"))

  #if intento < numero_secreto: 
   #print("el numero secreto es mayor")

  #elif intento > numero_secreto:
   #print("el numero es menor")

  #else:
   #print(" eres una lacra adivinaste")
   #break


#import random 

#opciones = ["piedra", "papel", "tijeras"]

#usuario = input("escoje piedra, papel o tijeras")
#computadora = random.choice(opciones)

#print ("la laptop escojio:", computadora)

#if usuario == computadora:
 #print("empate")

#elif (usuario == "piedra" and computadora == "tijeras") or\
      #(usuario == "tijeras" and computadora == "papel" ) or\
      #(usuario == "papel" and computadora == "piedra"):
      #print("eres una puta bestia, ganaste")
#else:
 #print("perdiste menol")
 
      

base_de_datos_de_dinosaurios = [
    ("tyrannosaurus Rex", "Rex", "Caranivoro", "Cretacico"),
    ("Velociraptor", "Raptor", "Carnivoro", "Cretacico"),
    ("Triceratops", "prorsus", "Hervivoro", "Cretacico"),
    ("Brachiosaurus", "Brachiosaurus", "Hervivoro", "Jurasico"),
    ("Stegosaurus", "Armatus", "Hervivoro", "Jurasico")
]

def informacion_dinosaurio(base_de_datos, nombre_dinosaurio):

    encontrado= False

    for dino in base_de_datos:

      if dino[0].lower() == nombre_dinosaurio.lower():
        print(f"Nombre: {dino[0]}, Especie: {dino[1]}, dieta: {dino[2]} Periodo : {dino[3]},  ")
        encontrado = True
      break

    if not encontrado:
       print("Dinosaurio no encontrado que la dilla")
def dinosaurios_por_dieta(base_de_datos, dieta_dinosaurio):
     encontrado= False

     for dino in base_de_datos:

        if dino[2].lower()== dieta_dinosaurio.lower():
           print(f"-Nombre: {dino[0]}, Especie: {dino[1]}, Periodo: {dino[3]} ")
           encontrado= True

           if not encontrado:
              print(f"No se encontraron dinosaurios con su dieta: {dieta_dinosaurio}")
def dinosaurio_por_periodo(base_de_datos, periodo_dinosaurio):
    encontrado=False

    for dino in base_de_datos:

       if dino[3] == periodo_dinosaurio:
         print(f"-nombre: {dino[0]}, Especie:{dino[1]}, dieta: {dino[2]} ")

         encontrado=True


         if not encontrado:
            print("nose encontraron dinos en el periodo")
def menu():
   print("1.- buscar por nombres")
   print("2.- buscar por dieta")
   print("3.- buscra por periodo") 

   usuario= int(input("elige una occion"))

   if usuario== 1:
    busqueda= input("igrasa el nombre del dinosaurio")
    informacion_dinosaurio(base_de_datos_de_dinosaurios, busqueda)

   elif usuario== 2:
      busqueda= input("ingra la dieta")
      dinosaurios_por_dieta(base_de_datos_de_dinosaurios,busqueda)


   elif usuario== 3:
      busqueda= input("ingrasa el periodo")
      dinosaurio_por_periodo(base_de_datos_de_dinosaurios, busqueda)

   else:
      print("estas como loquito")







