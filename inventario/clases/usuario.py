class Usuario:

	def __init__(self):
		self.id = 0
		self.nombre = ""
		self.apellidos = ""
		self.tipo_usuario = ( "Administrador", "Inventario", "Ventas" )
		self.visible = True

		self.usuarios = {}
		print("Constructor de la clase usuario")
	
	def listar_todo(self):
		print( 'Listado de usuarios: ', self.usuarios )