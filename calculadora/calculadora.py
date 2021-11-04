class Calculadora:

	def __init__(self):
		self.history = []
		print("Se ejecuto el constructor")
	
	def suma(self, numero1, numero2):
		print( self.numero1 + self.numero2 )
		self.history.append("suma")

	def resta(self, numero1, numero2):
		self.history.append("resta")
		return numero1 - numero2
	
	def multiplicacion( self, numero1, numero2 ):
		print( numero1 * numero2 )
		self.history.append("multiplicacion")
	
	def division( self, numero1, numero2 ):
		print( numero1 / numero2 )
		self.history.append("division")