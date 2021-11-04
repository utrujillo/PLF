from calculadora.calculadora import Calculadora

operaciones = Calculadora(1,1)

operaciones.suma(3, 7)

print( operaciones.resta(3, 7) )

operaciones.multiplicacion( 3, 7 )

operaciones.division( 3, 7 )

print(operaciones.history)

operaciones.suma(5, 9)
operaciones.suma(10, 10)

print(operaciones.history)