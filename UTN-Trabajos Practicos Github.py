#Practico 1-Estructuras secuenciales
#1)Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!"

saludo="Hola Mundo!"
print(saludo)

#2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre=input("Como es tu nombre? ")
print(f"Hola",nombre,"!")

#3)Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre_completo=input("Como es tu nombre completo?")
edad=input("Cuantos años tienes?")
residencia=input("De donde sos?")
intro=print(f"Soy",nombre_completo,"tengo",edad,"años","y vivo en",residencia)

#4)Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math
x=math.pi
radio=float(input("Ingrese un radio: "))
area=math.pi*(radio**2)
print("El area del circulo es: ",area)
perimetro=2*(math.pi*radio)
print(f"El perimetro del circulo es:",perimetro)

#5)Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segunds_ingr=float(input("Ingrese una cantidad de segundos: "))
horas=float((segunds_ingr/60)/60)
print(f"Los segundos ingresados son:",horas,"horas")

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
print(f"La suma de dichos numeros es:",num1+num2)
print(f"La resta de dichos numeros es:",num1-num2)
print(f"La multiplicacion de dichos numeros es:",num1*num2)
print(f"La division de dichos numeros es:",num1/num2)

#8)Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

peso=float(input("Ingrese su peso:"))
altura=float(input("Ingrese su altura:"))
imc=(peso/altura**2)
print(f"Su IMC es de:",imc)

#9)Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

temp_C=float(input("Ingrese una temperatura en Celsius para convertirlo a Fahrenheit:"))
temp_F=(9/5*temp_C+32)
print(f"Son:",temp_F,"°F")

#10)Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num_prom1=float(input("Ingrese un numero para calcular su promedio:"))
num_prom2=float(input("Ingrese un segundo numero para calcular su promedio:"))
num_prom3=float(input("Ingrese un tercer numero para calcular su promedio:"))
promedio=(num_prom1+num_prom2+num_prom3)/3
print(f"El promedio de dichos numeros es de:",promedio)

#------------------------------------------------------------------------------

#Calculadora de propinas en un restaurante

monto_inicial=float(input("Ingrese el monto de la cuenta:$"))
propina_10=float(monto_inicial*0.10)
print(f"Propina sugerida(10%):$",propina_10)
monto_total_10=monto_inicial+propina_10
print(f"Total a pagar(10%):$",monto_total_10)
propina_15=float(monto_inicial*0.15)
print(f"Propina sugerida(15%):$",propina_15)
monto_total_15=monto_inicial+propina_15
print(f"Total a pagar(15%):$",monto_total_15)

#------------------------------------------------------------------------------

#Ejercicios Complementarios

#1)Crea una variable llamada "numero1" y asígnale un número entero de tu elección.

numero1=int(13)

#2)No borres la variable número uno y crea una variable llamada "numero2" asignándole un número decimal de tu elección.

numero2=float(27.5)

#3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".

suma=numero1+numero2

#4)Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para multiplicación y otra para división. Imprime estas variables.

resta=numero1-numero2
multip=numero1*numero2
dividir=numero1/numero2


#5)Crea una variable llamada "nombre" y asígnale tu nombre como valor.

nombre="Paul"


#6)Crea una variable llamada "precio" y asígnale un valor decimal que represente el precio de un artículo ficticio.

precio=float(4500.50)

#7)Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al 100% y el valor 0 al 0%.

descuento=.30

#8)Ahora, intenta calcular el precio final aplicando el descuento al precio original y almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que aplicar la lógica de matemáticas.

precio_final=precio*descuento
print(precio_final)

#9)Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu elección. Qué sea un string.

cadena="All work and no play makes Jack a dull boy"
print(cadena)

#10)Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de Python.

longitud=len(cadena)
print(longitud)

#11)Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo mismo.

precio=1350.75
print(int(precio))

#12)Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas en una tercera variable llamada "nombre_completo", el nombre y el apellido con un espacio entre medio. Puedes usar libremente la forma de concatenación que quieras.

nombre="Nico"
apellido="Gonzalez"
nombre_completo=f"{nombre} {apellido}"
print(nombre_completo)

#13)Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.

edad=25
edad-=5
print(edad)
edad=25
edad-=10
print(edad)

#14)Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3.

altura=1.73
altura*=4
print(altura)
altura=1.73
altura/=3
print(altura)

#15)Crea una variable que contenga tu nombre completamente en mayúsculas. Después transfórmalo todo en minúsculas con algún método o función de Python.

nombre3="ROBERTO PAUL PAIVA"
print(nombre3.lower())

#16)Por último, con la variable con el nombre en mayúsculas, aplica un método parecido para que se transforme todo en minúsculas excepto la primera letra.

print(nombre3.title())

#---------------------------------------------------------------------------------------

