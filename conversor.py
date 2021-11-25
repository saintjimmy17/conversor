def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 

1- Pesos argentinos
2- Pesos colombianos
3- Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("argentinos", 180)
elif opcion == 2:
    conversor("colombianos", 3875)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingresa una opcion correcta por favor")



