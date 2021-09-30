print("Hola mundo")
print(10)
print("Hola mundo "+ str(10) )

# variables un espacio en memoria
# 1. comenzar con numeros
# 2. no contener espacios
# 3. no comenzar con caracteres especiales
# 4. solo ciertos caracteres especiales son aplicables (_-)

cadena = "Esto es una cadena"
print( cadena )
print( cadena + " Hola mundo" )
saludo = "Hola mundo"
print( cadena +" "+ saludo )

print("%s %s" %(cadena, saludo))
print("Hey %s, verificando si %s ?" %(cadena, saludo))

print("Hey "+ cadena +", verificando si "+ saludo +" ?")

menu = """
Bienvenidos al curso de Programacion logica y funcional

  1. Uso de elementos basicos en Python
  %s
  2. Trabajando con cadenas

Esto es un saludo
"""

print( menu %(cadena) )

nombre = "Juan"
numero = 2.5
"Hey [nombre] verificando si [numero] es numero?"
print("Hey %s, verificando si %f es numero" %(nombre, numero))

# print( "El tipo de dato es: %s" %( type(numero) ) )

texto = input("Escribe un texto: ")
print( texto )