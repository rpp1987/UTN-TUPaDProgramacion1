#Practico 3-Estructuras Condicionales
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#edad=int(input("Por favor ingrese su edad: "))
#
#if edad < 0:
#    print("Error:No has nacido todavia.Por favor ingrese su edad.")
#elif edad < 18 and edad > 1:
#    print("Es menor de edad.")
#else:
#    print("Es mayor de edad.")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

#nota=int(input("Por favor ingrese su nota: "))
#
#if nota >=6 and nota <=10:
#    print("Aprobado")
#else:
#    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

#num=int(input("Ingrese un numero: "))
#
#if num % 2==0:
#    print("Ha ingresado un numero par.")
#else:
#    print("Por favor, ingrese un numero par.")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.

#edad=int(input("Por favor ingrese su edad: "))
#
#if edad >= 30:
#    print("Sos un/a adulto/a.")
#elif edad >= 18 and edad < 30:
#    print("Sos un/a adulto/a joven.")
#elif edad >= 12 and edad < 18:
#    print("Sos un/a adolescente.")
#else:
#    print("Sos un/a niño/a.")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

#password=input("Por favor ingrese una contraseña: ")
#caracteres=len(password)
#
#if caracteres >=8 and caracteres <=14:
#    print("Ha ingresado una contraseña correcta.")
#else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma: import random numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.

#from statistics import mode, median, mean
#import random
#
#num_ale=[random.randint(1,50) for i in range(10)]
#
#meanx=mean(num_ale)
#medianx=median(num_ale)
#modex=mode(num_ale)
#
#print(f"Mean:{meanx}")
#print(f"Median:{medianx}")
#print(f"Mode:{modex}")
#
#
#if meanx > medianx and medianx > modex:
#    print("Hay sesgo positivo.")
#elif meanx < medianx and medianx < modex:
#    print("Hay sesgo negativo.")
#else:
#    if meanx == medianx and medianx == modex:   
#        print("Sin sesgo.")
#    else:
#        print("No entra en ninguna categoria")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.


#frase=input("Por favor ingrese una frase o palabra: ")
#
#if frase[-1].lower() in "aeiou":
#    frase=frase+"!"
#
#print(frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

#nombre=input("Por favor ingrese su nombre: ")
#opcion=input("Por favor elija una opcion\n1)Si quiere su nombre en mayúsculas\n2)Si quiere su nombre en minúsculas\n3)Si quiere su nombre con la primera letra mayúscula: ")
#
#opcion1=nombre.upper()
#opcion2=nombre.lower()
#opcion3=nombre.title()
#
#
#if opcion == "1":
#    print(opcion1)
#elif opcion == "2":
#    print(opcion2)
#else:
#    print(opcion3)

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

#magnitud=float(input("Por favor ingrese una magnitud: "))
#
#if magnitud >= 7:
#    print("Extremo(puede causar graves daños a gran escala.)")
#elif magnitud >= 6 and magnitud < 7:
#    print("Muy fuerte (puede causar daños significativos).")
#elif magnitud >= 5 and magnitud < 6:
#    print("Fuerte (puede causar daños en estructuras débiles).")
#elif magnitud >= 4 and magnitud < 5:
#    print("Moderado (sentido por personas, pero generalmente no causa daños).")
#elif magnitud >= 3 and magnitud < 4:
#    print("Leve (ligeramente perceptible).")
#else:
#    print("Muy leve (imperceptible).")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:
#Periodo del año    Estación en el hemisferio norte     Estación en el hemisferio sur
#Desde el 21 de                 Invierno                                Verano
#diciembre hasta el 
#20 de marzo (incluidos)

#Desde el 21 de                 Primavera                               Otoño
#marzo hasta el 20 de 
#junio (incluidos)

#Desde el 21 de                 Verano                                  Invierno
#junio hasta el 20 de
#septiembre (incluidos)

#Desde el 21 de                 Otoño                                   Primavera
#septiembre hasta el 20 de
#diciembre (incluidos)

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio=input("¿En que hemisferio se encuentra?: ").capitalize()
mes=int(input("¿En que mes estamos? (1-12): "))
dia=int(input("¿Que dia es? (1-31): "))

estacion_norte=""
estacion_sur=""


if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    estacion_norte="Invierno"
    estacion_sur="Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    estacion_norte="Primavera"
    estacion_sur="Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    estacion_norte="Verano"
    estacion_sur="Invierno"
elif (mes == 9 and dia >= 21) or  (10 <= mes <= 11) or (mes == 12 and dia <= 20):
    estacion_norte="Otoño"
    estacion_sur="Primavera"

if hemisferio == "Norte":
    print("Estas en:",estacion_norte)
elif hemisferio == "Sur":
    print("Estas en:",estacion_sur)
else:
    print("Error,hemisferio no valido.")

