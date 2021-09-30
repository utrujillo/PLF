# Crear un programa que convierta de MX a USD
valor_dolar = 20.5

dinero_actual = input('Cuantos pesos MX tienes? ')
dolares = float(dinero_actual) / valor_dolar
print("Tus %s MX son %s USD" %( dinero_actual, round(dolares,2) ))

# Tarea
# Crear transforme los dolares a pesos mexicanos e imprima en consola el siguiente texto
# Tus dolares (cantidad_usd) USD son (cantidad_mx) MX