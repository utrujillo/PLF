from menu.menu import menu, seleccion_submenu
from clases.usuario import Usuario

def run():
    salir = False
    usuario = Usuario()
    
    while salir == False:
        # menu()
        # opcion = int(input('Selecciona una opcion: '))

        seleccion_submenu( 3 )
        opcion_submenu = int(input('Que operacion deseas realizar: '))
        
        if( opcion_submenu  == 1 ):
            usuario.listar_todo()
        elif ( opcion_submenu == 2 ):
            usuario.crear()
        
        terminar = input('Deseas realizar otra operacion? S/N ')
        print( terminar, salir )
        if( terminar == "S" ):
            salir = True



if __name__ == '__main__':
    run()