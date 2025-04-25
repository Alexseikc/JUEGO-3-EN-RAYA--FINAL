import os
import pygame
import time

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

win_sound_file = "orchestral-win-331233.mp3"  
move_sound_file = "sound-alert-device-turn-on-turn-off-win-done-chakongaudio-174892.mp3"  
bg_music_file = "relaxing-guitar-loop-v5-245859.mp3"  
draw_sound_file = "error-126627.mp3"  

def load_music(file):
    try:
        pygame.mixer.music.load(file)
    except pygame.error as e:
        print(f"Error al cargar el archivo {file}: {e}")

def play_sound(file):
    try:
        pygame.mixer.music.stop()
        load_music(file)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error al reproducir sonido: {e}")

def play_background_music():
    load_music(bg_music_file)
    pygame.mixer.music.play(-1)

tablero = [" " for _ in range(9)]
jugador1 = ""
jugador2 = ""

def elegir_simbolo():
    global jugador1, jugador2
    while True:
        simbolo = input("Jugador 1, elige tu símbolo (X o O): ").upper()
        if simbolo in ["X", "O"]:
            jugador1 = simbolo
            jugador2 = "O" if jugador1 == "X" else "X"
            print(f"\nJugador 1: {jugador1} | Jugador 2: {jugador2}\n")
            break
        else:
            print("Entrada no válida. Por favor elige X o O.")

def mostrar_tablero():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TRES EN RAYA ===")
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
    print()

def comprobar_ganador(simbolo):
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in combinaciones:
        if tablero[combo[0]] == tablero[combo[1]] == tablero[combo[2]] == simbolo:
            return True
    return False

def tablero_lleno():
    return " " not in tablero

def jugar_turno(jugador):
    while True:
        try:
            posicion = int(input(f"{jugador}, elige una posición (1-9): ")) - 1
            if 0 <= posicion < 9 and tablero[posicion] == " ":
                tablero[posicion] = jugador
                play_sound(move_sound_file)
                break
            else:
                print("Posición inválida o ya ocupada. Intenta otra.")
                play_sound(draw_sound_file)
        except ValueError:
            print("Por favor, introduce un número del 1 al 9.")
            play_sound(draw_sound_file)

def jugar():
    while True:
        global tablero
        tablero = [" " for _ in range(9)]  
        
        elegir_simbolo()
        turno_actual = jugador1
        play_background_music()

        while True:
            mostrar_tablero()
            jugar_turno(turno_actual)

            if comprobar_ganador(turno_actual):
                mostrar_tablero()
                print(f"¡{turno_actual} ha ganado!")
                play_sound(win_sound_file)
                pygame.time.delay(5000)
                break

            if tablero_lleno():
                mostrar_tablero()
                print("¡El juego terminó en empate!")
                play_sound(draw_sound_file)
                pygame.time.delay(3000)
                break

            turno_actual = jugador2 if turno_actual == jugador1 else jugador1

        
        while True:
            respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()
            if respuesta in ['s', 'n']:
                break
            print("Por favor, introduce 's' para sí o 'n' para no.")

        if respuesta == 'n':
            print("¡Gracias por jugar! Hasta la próxima.")
            print("Hecho por Cevallos, Lema, Sánchez y Campos")
            break

jugar()
pygame.quit()