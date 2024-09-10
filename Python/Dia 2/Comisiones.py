nombre_empleado = input("Digite su nombre: ")
ventas = int(input("Digite total de ventas: "))

comision = (ventas) * 13/100

comision_total = round(ventas + comision,2)

print(f"El valor de la venta total fue de {ventas} \nValor de la comision es {comision} \nVentas mas comision {comision_total} ")