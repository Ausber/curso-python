mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
mi_lista3 = mi_lista + mi_lista2

#list.append() agrega un elemento a la lista
mi_lista3.append("g")

#list.pop() elimina el ultimo elemento de la lista si no se le manda parametro.
eliminado = mi_lista3.pop(0)
print(mi_lista3)
print(eliminado)

#list.sort() ordena los elementos de una lista ascendentemente
lista = ["g","o","b","m","c"]
lista.sort()
print(lista)

#list.reverse() ordena los elementos de una lista descendentemente
lista.reverse()
print(lista)