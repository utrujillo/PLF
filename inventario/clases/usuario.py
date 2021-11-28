import pandas as pd
import os.path
from clases.tipo_usuario import TipoUsuario

class Usuario:

	def __init__(self):
		# ( "Administrador", "Inventario", "Ventas" )
		self.FILE = 'C:/Users/utrujillo/Desktop/PLF/inventario/files/usuario.xlsx'
		self.usuario = {
			"nombre": "",
			"apellidos": "",
			"tipo_usuario": "",
			"visible": True
		}
		
		if(  os.path.isfile( self.FILE ) ):
			self.usuarios = pd.read_excel( self.FILE, index_col = 0 )
		else:
			self.usuarios = pd.DataFrame([])
		print("Constructor de la clase usuario")
	
	def listar_todo(self):
		mensaje = '''
Listado de usuarios
**************************

		'''
		print(mensaje)
		print(self.usuarios )
	
	def crear(self):
		self.usuario["nombre"] = input("Nombre: ")
		self.usuario["apellidos"] = input("Apellidos: ")

		for tipo in TipoUsuario:
			print( tipo.describe() )
		tipo_usuario = int( input( "Seleccionar el tipo de usuario: " ) )
		
		if( tipo_usuario > len(TipoUsuario) ):
			print( 'Usuario no existente, se asignara un valor nulo' )
			self.usuario["tipo_usuario"] = ""
		else:
			self.usuario["tipo_usuario"] = TipoUsuario(tipo_usuario)
		
		self.usuarios = self.usuarios.append( self.usuario, ignore_index = True )

		os.system('cls')
		self.usuarios.to_excel( self.FILE )
		print( "La informacion %s fue almacenada con exito" %( self.usuario ) )
