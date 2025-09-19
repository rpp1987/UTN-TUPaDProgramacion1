# 1.Generá un cartón 5x5 con números aleatorios entre 1 y 50, sin repetirse.
# 2.Mostrá el cartón al jugador en forma de matriz.
# 3.El programa debe sortear números al azar entre 1 y 50, uno por uno.
# 4.Cada vez que salga un número:
# o Si está en el cartón, reemplazarlo por un 0.
# o Si no está, avisar que no aparece.
# o Mostrar el cartón actualizado después de cada sorteo.
# 5.El juego termina cuando el cartón completo queda en 0 (¡Bingo!).
# Desafío extra: Validar cuando haya una línea completa (una fila llena de ceros) y mostrar el mensaje "¡Línea!".

import random

carton=random.sample(range(1, 51), 25)
carton_matriz=[carton[i*5:(i+1)*5] for i in range(5)]

def mostrar_carton(c):
    for fila in c:
        print(" ".join(f"{num:2}" for num in fila))
    print()

def linea_completa(c):
    for fila in c:
        if all(num == 0 for num in fila):
            return True
    return False

print("Bienvenidos al Bingo!")
print("Carton Inicial")
mostrar_carton(carton_matriz)

sorteados=[]

while True:
    numero_sorteado = random.randint(1, 50)
    if numero_sorteado in sorteados:
        continue
    sorteados.append(numero_sorteado)
    print(f"Numero sorteado:{numero_sorteado}")

    encontrado = False
    for i, fila in enumerate(carton_matriz):
        for j, num in enumerate(fila):
            if num == numero_sorteado:
                carton_matriz[i][j] = "O"
                encontrado = True

    if encontrado:
        print("Numero encontrado en el carton, se reemplaza por O")
    else:
        print("El numero no esta en el carton.")

    mostrar_carton(carton_matriz)

    if linea_completa(carton_matriz):
        print("Linea!")
        break

    if all(all(num == 0 for num in fila) for fila in carton_matriz):
        print("Bingo! Carton completo.")
        break
