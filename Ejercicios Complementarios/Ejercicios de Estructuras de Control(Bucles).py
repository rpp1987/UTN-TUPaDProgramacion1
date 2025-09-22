#Ejercicio 1: Bucle for para números pares
#Objetivo: Imprimir números pares usando un bucle for.
#Instrucciones:
#1.Escribe un bucle for que imprima los números pares del 2 al 20 (inclusive).
#2.Usa un condicional o el paso del rango para lograrlo.


for i in range(2, 21, 2): 
    if i % 2 == 0:
        print(i)

#Ejercicio 2:Bucle while con suma acumulativa
#Objetivo: Usar un bucle while para controlar una condición de salida.
#Instrucciones:
#1.Pide al usuario que ingrese números hasta que la suma supere 100.
#2.Imprime la suma total al final.

num=int(input("Ingrese un numero hasta para que la suma sea 100: "))

while num > 0:
    num += int(input("Ingrese otro numero: "))
    if num >= 100:
        print(f"La suma total es {num}.")
        break


#Ejercicio 3: Filtrar palabras por letra inicial
#Objetivo: Iterar sobre una lista y aplicar filtros.
#Instrucciones: Dada una lista de palabras (ej: ["apple", "banana", "avocado"]), imprime solo las que empiezan con "a".

bandas=["Aerosmith", "AC/DC", "Green Day", "Metallica", "AFI", "Black Sabbath"]

for banda in bandas:
    if banda.capitalize().startswith("A"):
        print(banda)



#Ejercicio 4: Tabla de multiplicar del 7
#Objetivo: Usar un bucle para generar patrones.
#Instrucciones: Imprime la tabla de multiplicar del 7 (desde 7x1=7 hasta 7x10=70).

for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")


#Ejercicio 5:Contador de vocales
#Objetivo: Contar caracteres específicos en un string.
#Instrucciones:
#1.Pide al usuario una cadena de texto.
#2.Cuenta y muestra cuántas vocales (a, e, i, o, u) contiene.



frase=input("Ingrese una frase: ")
vocales="aeiou"

contador=0

for letra in frase.lower():
    if letra in vocales:
        contador += 1

print(f"Su frase contiene {contador} vocales.")


#Ejercicio 6: Números repetidos en una lista
#Objetivo: Filtrar elementos duplicados manteniendo el orden.
#Instrucciones: Dada una lista (ej: [3, 1, 3, 5, 1]), crea una nueva lista con los números que aparecen más de una vez (en este caso: [3, 1]).

colores=["azul", "negro", "blanco", "rojo", "azul", "verde", "violeta", "azul", "rojo"]
duplicados=[]

for color in colores:
    if colores.count(color) > 1 and color not in duplicados:
        duplicados.append(color)

print(duplicados)



#Ejercicio 7: FizzBuzz
#Objetivo: Implementar lógica condicional en bucles.
#Instrucciones:
#1.Imprime números del 1 al 100, pero:
# oPara múltiplos de 3 → "Fizz".
# oPara múltiplos de 5 → "Buzz".
# oPara múltiplos de ambos → "FizzBuzz".


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#Ejercicio 8: Frecuencia de palabras
#Objetivo: Usar diccionarios para contar elementos.
#Instrucciones: Dada una cadena (ej: "hola hola mundo"), devuelve un diccionario con la frecuencia de cada palabra (ej: {"hola": 2, "mundo": 1}).

frase=input("Ingrese una frase: ")
palabras=frase.split()
frecuencia={}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(frecuencia)


#Ejercicio 9: Filtrar consonantes
#Objetivo: Manipular strings con condiciones.
#Instrucciones: Dada una cadena, crea una nueva cadena que solo contenga sus consonantes (ej: "Hola" → "Hl").

cadena=input("Ingrese una palabra o frase: ")
vocales="aeiouAEIOU"
consonantes=""

for char in cadena:
    if char.isalpha() and char not in vocales:
        consonantes += char

print(consonantes)


#Ejercicio 10: Números primos
#Objetivo: Implementar un algoritmo con bucles anidados.
#Instrucciones:
#1.Pide al usuario un número entero positivo.
#2.Imprime todos los números primos menores o iguales a ese número.

num=int(input("Por favor ingrese un numero entero positivo: "))

for num in range(2, num + 1):
    es_primo=True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo=False
            break
    if es_primo:
        print(num)

