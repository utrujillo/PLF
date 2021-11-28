import pandas as pd
import os.path
from clases.tipo_usuario import TipoUsuario

class Usuario:

	def __init__(self):
		self.FILE = 'C:/Users/utrujillo/Desktop/PLF/inventario/files/usuario.xlsx'
		self.usuario = {
			"id": 0,
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
		os.system('cls')
		mensaje = '''
Listado de usuarios
**************************
		'''
		print(mensaje)
		print(self.usuarios )
	
	def crear(self):
		os.system('cls')
		self.usuario = self.solicitar_usuario()
		self.usuario["id"] = len(self.usuarios) + 1
		
		self.usuarios = self.usuarios.append( self.usuario, ignore_index = True )
		self.usuarios.to_excel( self.FILE )
		print( "La informacion %s fue almacenada con exito" %( self.usuario ) )
	
	def buscar_texto(self):
		os.system('cls')
		texto_buscar = input("Escribe el nombre a buscar: ")
		coincidencias = self.usuarios.query('nombre.str.contains("{0}") or apellidos.str.contains("{1}")'.format(texto_buscar, texto_buscar), engine='python')
		mensaje = '''
Listado de usuarios encontrados
**************************
		'''
		print( mensaje )
		print( coincidencias )
	
	def buscar_id(self):
		os.system('cls')
		id_buscar = int( input("ID a buscar: ") )
		coincidencia = self.usuarios.query('id == {0}'.format(id_buscar))
		return coincidencia
	
	def actualizar(self):
		os.system('cls')
		# Verificando que el usuario exista
		usuario = self.buscar_id()
		if( len(usuario) > 0 ):
			print( 'Usuario encontrado, favor de ingresar los nuevos datos' )
			print( usuario )
			# Obteniendo el registro del listado de usuarios
			usuario_original = self.usuarios.loc[ usuario.index ]
			# Solicitando la nueva informacion para el usuario
			self.usuario = self.solicitar_usuario()
			# Uniendo los datos del usuario original, con la nueva informacion (exeptuando el ID y el campo visible)
			usuario_original["nombre"] = self.usuario["nombre"]
			usuario_original["apellidos"] = self.usuario["apellidos"]
			usuario_original["tipo_usuario"] = self.usuario["tipo_usuario"]
			# Actualizando dentro del catalogo de usuarios el nuevo usuario
			self.usuarios.loc[ usuario.index ] = usuario_original
			self.usuarios.to_excel( self.FILE )
			print( "La informacion fue actualizada con exito" )
		else:
			print("El usuario no fue encontrado...")
	
	def eliminar(self):
		os.system('cls')
		usuario_eliminar = usuario = self.buscar_id()
		print( "Usurio a eliminar" )
		print( usuario_eliminar )
		verificar = input("Estas seguro de querer eleminar ? S/N ")

		if( verificar == "S" or verificar == "s" ):
			self.usuarios = self.usuarios.drop( usuario_eliminar.index )
			self.usuarios.to_excel( self.FILE )
			print( "Usuario eliminado..." )
	
	def solicitar_usuario(self):
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
		
		return self.usuario

