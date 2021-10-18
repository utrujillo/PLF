# Arreglo
array = ("Hola", "Mundo")
print( array[0] )

# Lista
lista = ['Hola', 4, 4.5, True]
print( lista[2] )

lista.append( "Agregando elemento" )
print( lista )

lista.pop(1)
print( lista )

for item in lista:
  print( "Elemento %s" %(item) )

for item in lista[::-1]:
  print( "Elemento %s" %(item) )

lista2 = ['item1', False, 3.5]

suma_lista = lista + lista2

print( suma_lista )

print( "Size lisa: %s" %( len(suma_lista) ) )


