pesos = input("¿Cuántos pesos hondureños tienes?: ")
pesos = float(pesos)
valor_dolar = 28.14
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")

print("----------------------------")
dolares = input("¿Cuántos dólares tienes?: ")
dolares = float(dolares)
pesos = dolares * 28.14
pesos = str(round(pesos, 2))
print("Tienes L." + pesos + " lempiras hondureños.")

