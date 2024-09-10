#Enumerator crea una tupla con el indice y valor
lista = ['a','b','c']

"""for indice,item in enumerate(range(50,55)):
    print(indice,item)"""
"""
mis_tuples = list(enumerate(lista))
print(mis_tuples[0][1])"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in list(enumerate(lista_nombres)):
    if(nombre.startswith("M")):
        print(indice)