#Vas a programar un juego clásico contra la computadora: Piedra, papel o tijeras.
#Reglas:
#1.El programa debe mostrar un menú con las opciones:
#o Piedra
#o Papel
#o Tijera
#2.El jugador elegirá una opción.
#3.La computadora elegirá su jugada al azar.
#4.El programa debe comparar ambas jugadas y mostrar quién gana:
#o Piedra vence a Tijera.
#o Tijera vence a Papel.
#o Papel vence a Piedra.
#o Si ambos eligen lo mismo, es empate.
#Extra (para hacerlo más divertido):
#• Llevar un marcador de cuántas partidas gana el jugador y cuántas gana la computadora.
#• El juego termina cuando el jugador elija salir, mostrando el resultado final.


import random

opciones=["piedra", "papel", "tijera"]

player1=0
bot1=0

while True:
    print("MENU")
    print("1.Piedra")
    print("2.Papel")
    print("3.Tijera")
    print("4.Salir")
    
    eleccion=input("Elige una opcion (1-4): ")

    if eleccion == "4":
        print("GAME OVER")
        print("Resultado final:")
        print(f"Player 1:{player1} - Bot:{bot1}")
        if player1 > bot1:
            print("Felicidades! Ganaste el juego!")
        elif player1 < bot1:
            print("Bot ganó el juego.")
        else:
            print("El juego terminó en empate.")
        break

    if eleccion not in ["1", "2", "3"]:
        print("Opcion inválida.Por favor intenta de nuevo.")
        continue

    player=opciones[int(eleccion) - 1]
    bot=random.choice(opciones)

    print(f"Elegiste:{player}")
    print(f"Bot eligió:{bot}")

    if player == bot:
        print("Empate!")
    elif (player == "piedra" and bot == "tijera") or (player == "tijera" and bot == "papel") or (player == "papel" and bot == "piedra"):
        print("Ganaste!")
        player1 += 1
    else:
        print("Bot ganó.")
        bot1 += 1

print(f"Score:\nPlayer 1: {player1}\nBot:{bot1}")

