'''
Adivina el Numero
Solicitar nombre del jugador
Maximo 8 intentos
Numero entre el 1 y el 100
Si el numero ingresado no esta en el rango, arrojar mensaje
Si ek numero ingresado es mayor o menor, arrojar mensaje
si adivina el numero, arrojar en cuantos intentos lo logro
'''
from random import randint
player_name = input("Ingresa Tu Nombre : ")
random_number = 10
'''randint(1,100)'''
max_try = 8
try_player = 1

while try_player <= max_try:
    number_player = int(input("Ingresa un numero del 1 a 100 : "))
    if try_player > max_try:
        print(f"Has Alcanzando el Maximo de Intentos")
    elif number_player < 1 or number_player > 100:
        print("El numero ingresado no esta en el rango.")
        try_player = try_player + 1
        continue
    elif number_player > random_number:
        print("El numero ingresado es mayor.")
        try_player = try_player + 1
        continue
    elif number_player < random_number:
        print("El numero ingresado es menor.")
        try_player = try_player + 1
        continue
    elif number_player == random_number:
        print(f"Has adivinado el numero en el intento N°{try_player}")
        try_player = try_player + 1
        break