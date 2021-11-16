class Usuario:

	def __init__(self):
		# ( "Administrador", "Inventario", "Ventas" )
		self.usuario = {
			"id": "",
			"nombre": "",
			"apellidos": "",
			"tipo_usuario": "",
			"visible": True
		}

		self.usuarios = []
		print("Constructor de la clase usuario")
	
	def listar_todo(self):
		print( 'Listado de usuarios: ', self.usuarios )
	
	def crear(self):
		self.usuario["nombre"] = input("Nombre: ")
		self.usuario["apellidos"] = input("Apellidos: ")
		tipo = '''
	( "Administrador", "Inventario", "Ventas" )
		'''
		print(tipo)
		self.usuario["tipo_usuario"] = input('Escribe el tipo: ')
		self.usuarios.append( self.usuario )
		print( self.usuarios )
