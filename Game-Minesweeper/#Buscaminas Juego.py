# Buscaminas Juego 🥶

import random
import os

# Tablero (Emojis disponibles para el tablero: 🟥🟧🟨🟩🟦🟪🟫⬛⬜🔴🟠🟡🟢🔵🟣🟤⚫⚪♦︎▫︎▪︎)

def creacion_tablero(filas, columnas, val):
    #Crea el tablero
    tablero = []
    for i in range(filas):
        tablero.append([])
        for j in range(columnas):
            tablero[i].append(val)
    return tablero

def muestra_tab(tablero):
    #Muestra en filas y columnas el tablero
    print("* * * * * * * * * * * * * * * * * *")
    for h in tablero:
        print("*", end=" ")
        for elemento in h:
            print(elemento, end=" ")
        print("*")
    print("* * * * * * * * * * * * * * * * * *")

def colocacion_bombas(tablero, cantidad_bombas, filas, columnas):
    #Coloca las minas
    bombas_escondidas = []
    contador = 0
    while contador <= cantidad_bombas:
        y = random.randint(0, filas-1)
        x = random.randint(0, columnas-1)
        if tablero[y][x] != "💣":
            tablero[y][x] = "💣"
            contador += 1
            bombas_escondidas.append((y,x))
    return tablero, bombas_escondidas

def pistas(tablero, filas, columnas):
    #Recorre el tablero y pone el número de minas vecinas que tiene cada casilla
    for y in range(filas):
        for x in range(columnas):
            if tablero[y][x] == "💣":
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if 0 <= y+i <= filas-1 and 0 <= x+j <= columnas-1:
                            if tablero[y+i][x+j] != "💣":
                                tablero[y+i][x+j] += 1
    return tablero

def expandir(oculto, visible, y, x, filas, columnas, simbolo):
    #Recorre todas las casillas vecinas, y comprueba si son ceros, si es así las descubre, y recorre las vecinas de estas, hasta encontrar casillas con pistas, que también descubre.
    espacios_vacios = [(y,x)]
    while len(espacios_vacios) > 0:
        y, x = espacios_vacios.pop()
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 0 <= y+i <= filas-1 and 0 <= x+j <= columnas-1:
                    if visible[y+i][x+j] == simbolo and oculto[y+i][x+j] == 0:
                        visible[y+i][x+j] = 0
                        if (y+i, x+j) not in espacios_vacios:
                            espacios_vacios.append((y+i, x+j))
                    else:
                        visible[y+i][x+j] = oculto[y+i][x+j]
    return visible

def tablero_listo(tablero, filas, columnas, simbolo):
    #Comprueba si el tablero no tiene ninguna casilla con el valor visible inicial
    for y in range(filas):
        for x in range(columnas):
            if tablero[y][x] == simbolo:
                return False
    return True

#Menu

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():
    limpiar_pantalla()
    print("Bienvenido a Buscaminas")
    print("1. Iniciar juego")
    print("2. Instrucciones")
    return int(input("Selecciona una opción: "))

def mostrar_instrucciones():
    limpiar_pantalla()
    print()
    print("Instrucciones del juego Buscaminas:\n")
    print("- Usa las teclas" + ' "W, A, S, D" ' + "para moverte de posición")
    print("- Usa M para descubrir una casilla")
    print("- Usa b para marcar una casilla")
    print("- Usa v para desenmarcar una casilla")
    print("- Evita las minas y descubre todas las casillas seguras para ganar")
    print()

a = mostrar_menu()

while a != 1:
  if a == 2:
    mostrar_instrucciones()
    a = mostrar_menu()

limpiar_pantalla()
print("¡Jugando Buscaminas!")

def menu():
    #Devuelve el movimiento u opción elegida por el usuario
    print()
    eleccion = input("¿w/s/a/d - m - b/v? ")
    return eleccion

def sustituye_ceros(tablero):
    for i in range(12):
        for j in range(16):
            if tablero[i][j] == 0:
                tablero[i][j] = " "
    return tablero

columnas = 16
filas = 12

visible = creacion_tablero(filas, columnas, "▫︎")

oculto = creacion_tablero(filas, columnas, 0)
oculto, bombas_escondidas = colocacion_bombas(oculto, 15, filas, columnas)
oculto = pistas(oculto, filas, columnas)

# Colocamos ficha inicial y mostramos tablero

y = random.randint(2, filas-3)
x = random.randint(2, columnas-3)

actual = visible[y][x]
visible[y][x] = "x"

os.system("cls")

muestra_tab(visible)

# Bucle principal

bombas_marcadas = []

jugando = True

while jugando:

    movimiento = menu()

    if movimiento == "w":
        if y == 0:
            y = 0
        else:
            visible[y][x] = actual
            y -= 1
            actual = visible[y][x]
            visible[y][x] = "x"

    elif movimiento == "s":
        if y == filas-1:
            y = filas-1
        else:
            visible[y][x] = actual
            y += 1
            actual = visible[y][x]
            visible[y][x] = "x"

    elif movimiento == "a":
        if x == 0:
            x = 0
        else:
            visible[y][x] = actual
            x -= 1
            actual = visible[y][x]
            visible[y][x] = "x"

    elif movimiento == "d":
        if x == columnas-1:
            x = columnas-1
        else:
            visible[y][x] = actual
            x += 1
            actual = visible[y][x]
            visible[y][x] = "x"

    elif movimiento == "b":
        if actual == "▫︎":
            visible[y][x] = "#"
            actual = visible[y][x]
            if (y,x) not in bombas_marcadas:
                bombas_marcadas.append((y,x))

    elif movimiento == "v":
        if actual == "#":
            visible[y][x] = "▫︎"
            actual = visible[y][x]
            if (y,x) in bombas_marcadas:
                bombas_marcadas.remove((y,x))

    elif movimiento == "m":
        if oculto[y][x] == "💣":
            visible[y][x] = "💣"
            jugando = False

        elif oculto[y][x] != 0:
            visible[y][x] = oculto[y][x]
            actual = visible[y][x]

        elif oculto[y][x] == 0:
            visible[y][x] = 0
            visible = expandir(oculto, visible, y, x, filas, columnas, "▫︎")
            visible = sustituye_ceros(visible)
            actual = visible[y][x]

    os.system("cls")

    muestra_tab(visible)

    victoria = False

    if tablero_listo(visible, filas, columnas, "▫︎") and \
        sorted(bombas_escondidas) == sorted(bombas_marcadas) and \
        actual != "▫︎":
        victoria = True
        jugando = False

if not victoria:
    print("                           ")
    print("     🥶HAS PERDIDO🥶      ")
    print("                           ")
else:
    print("                           ")
    print("  🏆🎖️ HAS GANADO 🎖️🏆   ")
    print("                           ")

print()
input(" 'Enter' para salir ... ")