from menu.menu import menu, seleccion_submenu

def run():
    menu()
    opcion = int(input('Selecciona una opcion: '))
    seleccion_submenu( opcion )


if __name__ == '__main__':
    run()