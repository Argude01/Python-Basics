# Capitalize : agrega la primer letra mayúscula
nombre = input("¿Cómo te llamas? : ").capitalize()
print(nombre)

# Strip : elimina los espacios al inicio y al final de la cadena de carácteres
nombre_completo = input("¿Cuál es tu nombre completo? : ").strip()
print(nombre_completo)

# replace : reemplaza algunas letras por otras
nombre_encriptado = input("Escribe tu contraseña: ").replace('a', '3')
print(nombre_encriptado)
print("La contraseña tiene " + str(len(nombre_encriptado)) + " carácteres.")

# slice : separando las cadenas en varias partes
print("Nombre: " + nombre)
print(nombre[1:7:2]) #tomando desde la posición 2 hasta la 8 de dos en dos
print(nombre[1::2]) #tomando desde la posición 2 hasta el fin de dos en dos
print(nombre[::-1]) #recorre la cadena de atras hacia adelante

