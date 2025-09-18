#Practico 4-Estructuras Repetitivas
#1)Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

i=0
while i <= 100:
    print(i)
    i += 1

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num=input("Ingrese un numero entero: ")

num_cant=len(num.lstrip("-"))

print(f"El numero tiene {num_cant} digitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese un segundo numero: "))

if num1 > num2:
    num1, num2 = num2, num1

suma=0
for i in range(num1+ 1, num2):
    suma += i

print(f"La suma de los numeros comprendidos entre {num1} y {num2}, excluyendo ambos, es: {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma=0

while True:
    num=int(input("Ingres un numero entero (Ingrese 0 para terminar): "))
    if num==0:
        break
    suma += num

print(f"El total acumulado es:{suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_rand=random.randint(0, 9)

intentos=0
adivinado=False

print("Adivine el numero entre 0 y 9: ")

while not adivinado:
    intento=int(input("Ingresa un numero: "))
    intentos += 1

    if intento == num_rand:
        adivinado=True
        print(f"Correcto! El numero era {num_rand}.")
        print(f"Fueron {intentos} intentos para adivinarlo.")
    else:
        print("No es el numero, intenta de nuevo.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario

num=int(input("Ingrese un numero entero positivo: "))

if num > 0:
    suma=0
    for i in range(1, num):
        suma +=i
    print(f"La suma de los numeros comprendidos entre 0 y {num} es:{suma}")
else:
    print("Error: debe ingresar un numero positivo.")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cant=100

pares=0
impares=0
positivos=0
negativos=0

for i in range(cant):
    num=int(input(f"Ingrese el numero {i+1}: "))

    if num % 2==0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    else:
        negativos += 1

print("Resultados")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

cant=10

suma=0

for i in range(cant):
    num=int(input(f"Ingrese el numero {i+1}: "))
    suma += num

media=suma/cant

print("Resultados")
print(f"La media de los {cant} numeros es: {media}")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num=input("Ingrese un numero: ")

invertido=num[::-1]

print(f"El numero invertido es: {invertido}")

