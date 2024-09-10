"""
Colecion de Elementos
Un set tiene datos unicos.
No poseen indices.
Sus elementos son inmutables
"""

"""mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(2 in mi_set)
"""

"""
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)"""

s1 = {1,2,3}
s1.add((4))
s1.remove(3)
s1.discard(6)
sorteo = s1.pop()
s1.clear()
print(s1)
print(sorteo)
