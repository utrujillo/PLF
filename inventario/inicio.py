from menu.menu import menu, seleccion_submenu
from clases.usuario import Usuario

def run():
    menu()
    opcion = int(input('Selecciona una opcion: '))

    seleccion_submenu( opcion )
    opcion_submenu = int(input('Que operacion deseas realizar: '))

    usuario = Usuario()
    
    if( opcion_submenu  == 1 ):
        usuario.listar_todo()




if __name__ == '__main__':
    run()