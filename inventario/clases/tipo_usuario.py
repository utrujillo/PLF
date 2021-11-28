import enum

class TipoUsuario( enum.Enum ):
    Administrador = 1
    Inventario = 2
    Ventas = 3

    def describe(self):
        return "{0}. {1}".format(self.value, self.name)