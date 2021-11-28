from menu.menu import menu, seleccion_submenu
from clases.usuario import Usuario

def run():
	salir = False
	usuario = Usuario()

	while salir == False:
		menu()
		opcion = int(input('Selecciona una opcion: '))

		seleccion_submenu( opcion )
		opcion_submenu = int(input('Que operacion deseas realizar: '))

		if( opcion_submenu  == 1 ):
			usuario.listar_todo()
		elif ( opcion_submenu == 2 ):
			usuario.crear()
		elif ( opcion_submenu == 3 ):
			usuario.buscar_texto()
		elif ( opcion_submenu == 4 ):
			coincidencia = usuario.buscar_id()
			mensaje = '''
Identificador encontrado
**************************
		'''
			print(mensaje)
			print( coincidencia )
		elif( opcion_submenu == 5 ):
			usuario.actualizar()
		elif( opcion_submenu == 6 ):
			usuario.eliminar()

		terminar = input('Deseas realizar otra operacion? S/N ')

		if( terminar == "N" or terminar == "n" ):
			salir = True

if __name__ == '__main__':
	run()