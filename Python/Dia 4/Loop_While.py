"""monedas = 5

while monedas > 0 :
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else:
    print("No tengo mas dinero")"""

"""respuesta = 's'
while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n): ")
else:
    print('Gracias')"""

## pass  Reservar un espacio
## break Sale del loop
## continue  Continua con la siguiete iteracion
"""nombre = input('Tu Nombre: ')
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)"""

numero = 50

while numero >= 0 :
    if numero%5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1
        continue
