import random
from pynput import keyboard as bk
import os

# Laberinto
laberinto = [
    ".........#",
    "#.#######.#",
    "#.#.....#.#",
    "#.#.###.#.#",
    "#...#...#.#",
    "###.#.###.#",
    "#...#.....#",
    "#########.."
]

nombre = input("Por favor ingrese su nombre: ")
print("¡Comienza el juego!\nUsa las teclas de flecha para mover al personaje.")



fila = len(laberinto)
columna = len(laberinto[0])
posicion_personaje = [0, 0]

def crearLaberinto():
    global fila, columna, laberinto
    fila = len(laberinto)
    columna = len(laberinto[0])

def mostrarLaberinto():
    global laberinto
    # Limpia la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(fila):
        for x in range(columna):
            if posicion_personaje == [i, x]:
                print("P", end="")
            else:
                print(laberinto[i][x], end="")
        print("")
    

def moverPersonaje(key):
    global posicion_personaje
    nueva_posicion = list(posicion_personaje)
    if key == bk.Key.up:
        nueva_posicion[0] -= 1
    elif key == bk.Key.down:
        nueva_posicion[0] += 1
    elif key == bk.Key.left:
        nueva_posicion[1] -= 1
    elif key == bk.Key.right:
        nueva_posicion[1] += 1
    # Verificar si la nueva posición es válida
    if (
        0 <= nueva_posicion[0] < fila
        and 0 <= nueva_posicion[1] < columna
        and laberinto[nueva_posicion[0]][nueva_posicion[1]] == "."):
        posicion_personaje = nueva_posicion
        mostrarLaberinto()
        verificar_final()

def verificar_final():
    global fila, columna, posicion_personaje
    if posicion_personaje == [fila - 1, columna - 1]:
        print(f"¡Felicidades {nombre}! ¡Has terminado el laberinto!")
        exit()  # Finaliza el programa

def on_key_release(key):
    if key in [bk.Key.up, bk.Key.down, bk.Key.left, bk.Key.right]:
        moverPersonaje(key)

def menu():
    # Configurar el listener del teclado
    listener = bk.Listener(on_release=on_key_release)
    listener.start()
    mostrarLaberinto()
    listener.join()

menu()