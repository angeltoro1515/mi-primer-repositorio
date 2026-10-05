entrenamiento= {
    "fuerza": {
        "lagartijas": {
            "repeticiones": 20,
            "bloques": 5
        },

        "dominadas": {
            "repeticiones": 10,
            "bloques": 3
        },

    "cardio": {
        "burpis":{
            "repeticiones": 20,
            "bloques": 3
        },

        "saltar_cuerda": {
            "repeticiones": 20,
            "bloques": 7
        }
    }

    }

}








def motras_entrenamiento( entrenamiento, categoria, ejercicio ):
    siguiente= entrenamiento[categoria][ejercicio]["repeticiones"]
    bloques= entrenamiento[categoria][ejercicio]["bloques"]
    return  f"de {ejercicio} vas a hacer {siguiente} repeticiones y de ahi vas {bloques} bloques"



def menu():
 print ("=== BIENVENIDO A LA GUIA DE ENTRENAMIENTO ===")   
print ("recuerda calentar")




categoria_usuario= input("que actegoria quieres hacer (fuerza o cardio?)")
ejecicio_usuario= input("que ejercicio quieres hacer?:")

resultado= motras_entrenamiento(entrenamiento, categoria_usuario, ejecicio_usuario)
print(resultado)


       


    
            
        
            



