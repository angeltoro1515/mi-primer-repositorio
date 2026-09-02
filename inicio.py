print("hola mundo")

num1 = float(input("ingresa el primer numero: "))
num2 = float(input ("ingresa el segundo numero: "))
operador = input(" ingresa el operador (+, -, *, /): ")

if operador == "+":
 print("resultado:", num1 + num2)

elif operador == "-":
    print("resultado:", num1 - num2)
  

elif operador == "*":
    print ("resultado:", num1 * num2)
 
elif operador == "/":
  if num2 != 0: 
     print("resultado:", num1 /num2)

  else:
      print("no se puede dividir entre 0.")

else:
   print("operador no valido.")


base = float( input("ingresa la base del triangulo:"))
altura = float( input("ingresa el altura del triangilo:"))

area = (base * altura) /2

print("el area de un trangulo es", area)



celsius = float( input("ingresa la temperatura en grados:"))

farenheit = (celsius * 9 / 5) +32
print("la tempertura de farenheit es:", farenheit)



numero = int(input("ingresa un numero entero"))

if numero % 2 == 0:
   print("el nuemro es par")

else:
   print("el numero es impar") 


n1 = float(input("ingresa el primer numero para comparar"))
n2 = float(input(" ingresa el segundo numero para comparar"))

if n1 > n2:
  print("el primer numero es mayor:",n1)

elif n2 > n1:
   print("el segundo numero es mayor:",n2)

else:
   print("ambos numeros son iguales")



anio = int(input("ingresa un año"))
if anio % 4 == 0:
   print("un año es bisiesto")

else:
   print(" un año es es bisiesto")

 





