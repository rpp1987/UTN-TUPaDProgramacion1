#Practico 1-Estructuras secuenciales
#1)Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!"

saludo="Hola Mundo!"
print(saludo)

#2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre=input("Como es tu nombre?: ")
print(f"Hola {nombre}!")

#3)Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre_completo=input("Como es tu nombre completo?: ")
edad=input("Cuantos años tienes?: ")
residencia=input("De donde sos?: ")
intro=print(f"Soy {nombre_completo}, tengo {edad} años, y vivo en {residencia}.")

#4)Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math
x=math.pi
radio=float(input("Ingrese un radio: "))
area=math.pi*(radio**2)
print(f"El area del circulo es {area:.2f}")
perimetro=2*(math.pi*radio)
print(f"El perimetro del circulo es {perimetro:.2f}")

#5)Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segunds_ingr=float(input("Ingrese una cantidad de segundos: "))
horas=float((segunds_ingr/60)/60)
print(f"Los segundos ingresados son {horas:.2f} horas")

#6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num_ingr=int(input("Ingrese un numero para ver su tabla de multiplicar:"))
print(f"{num_ingr} X 1 = {num_ingr*1}")
print(f"{num_ingr} X 2 = {num_ingr*2}")
print(f"{num_ingr} X 3 = {num_ingr*3}")
print(f"{num_ingr} X 4 = {num_ingr*4}")
print(f"{num_ingr} X 5 = {num_ingr*5}")
print(f"{num_ingr} X 6 = {num_ingr*6}")
print(f"{num_ingr} X 7 = {num_ingr*7}")
print(f"{num_ingr} X 8 = {num_ingr*8}")
print(f"{num_ingr} X 9 = {num_ingr*9}")
print(f"{num_ingr} X 10 = {num_ingr*10}")

#7)Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1=int(input("Ingrese un numero entero que no sea 0: "))
num2=int(input("Ingrese otro numero entero que no sea 0: "))
print(f"La suma de dichos numeros es  {num1+num2}")
print(f"La resta de dichos numeros es {num1-num2}")
print(f"La multiplicacion de dichos numeros es {num1*num2}")
print(f"La division de dichos numeros es {num1/num2:.2f}")

#8)Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

peso=float(input("Ingrese su peso:"))
altura=float(input("Ingrese su altura:"))
imc=(peso/altura**2)
print(f"Su IMC es de {imc:.2f}")

#9)Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

temp_C=float(input("Ingrese una temperatura en Celsius para convertirlo a Fahrenheit: "))
temp_F=(9/5*temp_C+32)
print(f"Son {temp_F}°F")

#10)Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num_prom1=float(input("Ingrese un numero para calcular su promedio:"))
num_prom2=float(input("Ingrese un segundo numero para calcular su promedio:"))
num_prom3=float(input("Ingrese un tercer numero para calcular su promedio:"))
promedio=(num_prom1+num_prom2+num_prom3)/3
print(f"El promedio de dichos numeros es de {promedio:.2f}")

