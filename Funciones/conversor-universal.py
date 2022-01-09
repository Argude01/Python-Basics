def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes? : ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 

1 - Pesos hondureños
2 - Pesos colombianos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("hondureños", 2451)
elif opcion == 2:
    conversor("colombianos", 3875)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print('Ingresa una opción correcta por favor')