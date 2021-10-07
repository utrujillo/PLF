def suma(n1, n2):
	print("Suma: %f" %(n1 + n2) )

def resta(numero1, numero2):
	return numero1 - numero2

def multiplicacion(n1, n2):
	print("Multiplicacion: %f" %(n1 * n2) )

def division(n1, n2):
	print("Division: %f" %(n1 / n2) )

numero1 = float( input("Ingresa un numero: ") )
numero2 = float( input("Ingresa otro numero: ") )

menu = '''
	*************
	Calculadora
	Elige una opcion a realizar con los siguientes numeros %f, %f
	1.- Suma
	2.- Resta
	3.- Multiplicacion
	4.- Division
	****************
'''

opcion = input( menu %(numero1, numero2) )
print("Opcion seleccionada %s" %(opcion))

if( opcion == "1" ):
	suma(numero1, numero2)
elif( opcion == "2" ):
	result = resta(numero1, numero2)
	print("Resta: %s" %(round(result, 2)) )
elif( opcion == "3" ):
	multiplicacion(numero1, numero2)
elif( opcion == "4" ):
	division(numero1, numero2)
else:
	print("Opcion no valida")

