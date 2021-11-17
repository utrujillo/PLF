import pandas as pd

class Usuario:

	def __init__(self):
		# ( "Administrador", "Inventario", "Ventas" )
		self.FILE = 'C:/Users/utrujillo/Desktop/PLF/inventario/files/usuario.xlsx'
		self.usuario = {
			"id": "",
			"nombre": "",
			"apellidos": "",
			"tipo_usuario": "",
			"visible": True
		}

		self.usuarios = pd.read_excel( self.FILE )
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

		diccionario_usuarios = pd.DataFrame( self.usuarios )
		print( diccionario_usuarios )
		diccionario_usuarios.to_excel( self.FILE )
