def menu():
    menu = '''
    ***************************************
        Sistema de inventario PLF
        
        1.- Catalogo de productos
        2.- Catalogo de unidad
        3.- Modulo de usuarios
    ***************************************
    '''
    print( menu )

def seleccion_submenu( opcion ):
    if( opcion == 3 ):
        submenu_usuario()
    else:
        print( 'Opcion no valida' )

def submenu_usuario():
    submenu = '''
    ---------------------------------------
        Modulo de Usuarios
        Que operacion deseas realizar
        1.- Lista todo
        2.- Crear usuario
        3.- Busqueda por texto
        4.- Busqueda por ID
        5.- Actualizar por ID
        6.- Eliminar por ID
    ---------------------------------------
    '''
    print( submenu )