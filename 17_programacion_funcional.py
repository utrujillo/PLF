def suma_dos( numero ):
    return numero + 2

def multiplica_dos( numero ):
    return numero * 2

def aplicar_operacion( funcion, numeros ):
    resultados = []
    for numero in numeros:
        resultado = funcion(numero)
        resultados.append( resultado )
    
    return resultados

def run():
    numeros = [1,2,3,4]
    resultados = aplicar_operacion( suma_dos, numeros )
    print( resultados )

    resultados = aplicar_operacion( multiplica_dos, numeros )
    print( resultados )

if __name__ == '__main__':
    run()