nombre = "IVAN DANIEL VALVERDE DE LA CRUZ"
nombre = nombre.lower()
print( "Cadena: %s" %(nombre) )

nombre = nombre.upper()
print( "Cadena: %s" %(nombre) )

nombre = nombre.capitalize()
print( "Cadena: %s" %(nombre) )

nombre = nombre.replace('de','DEE')
print( "Cadena: %s" %(nombre) )

print( "Indice 5 : %s" %( nombre[5] ) )

print( "Longitud de la cadena: %s" %( len(nombre) ) )

print( type(len(nombre)) )

print( "=======================" )
print("Rango de cadena %s" %( nombre[0:4] ))
print("Rango de cadena %s" %( nombre[:4] ))
print("Rango de cadena %s" %( nombre[::-1] ))

nombre = "A luna ese anula"
nombre_invertido = nombre[::-1]
print( "Nombre original: %s , nombre invertido: %s" %( nombre, nombre_invertido ) )