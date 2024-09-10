'''dic = {'clave': 100, 'Clave': 500}

a = dic.popitem()

print(a)
print(dic)
'''

caracteres = ',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#'

removed = caracteres.lstrip(',:_#,,,,,,:::____##')

print(removed)
print(caracteres)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

result = marcas_smartphones.isdisjoint(marcas_tv)

print(result)