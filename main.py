"""Ejercicio 7"""
lista_datos = list()
while True:
    Nombre = input("Indica a continuación tu nombre : ")
    if Nombre == "fin":
        break
    Telefono = int(input("Indica tu número de teléfono: "))

    datos_personales = {}

    datos_personales["Nombre"] = Nombre
    datos_personales["Teléfono"] = Telefono

    lista_datos.append(datos_personales)

for datos_personales in lista_datos :
    print("Estos son mis datos personales: ", datos_personales)
