for contador in range(1,11):
  print("Contador: %i" %( contador ))

vocales = "aeuio"

cadena = "Habitantes"
for index,letra in enumerate(cadena):
  if index % 2 == 0:
    if( letra in vocales ):
      print("Posicion %i letra par es %s" %( index, letra ))