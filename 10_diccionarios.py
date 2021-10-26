def run():

  # tupla = (10, 'Hola')
  # lista = [10, 'Hola']

  diccionario = {
    'numero': 10,
    'cadena': 'Hola',
    'nombre': 'Juan'
  }

  print( diccionario )
  print( diccionario['numero'] )

  telefonos = [ "212-732-1234", "646-123-4567" ]

  customer = {
    "firstName": 'John',
    "lastName": 'Doe',
    "address": {
      "streetAddress": "Av. Tecnologico",
      "city": "Acapulco",
      "state": "Guerrero",
      "postalCode": "39789",
    },
  }

  # customer['phoneNumbers'] = telefonos

  # print(customer['phoneNumbers'][1])

  # print(customer["address"]["city"])

  # print( customer['address'].keys() )
  for key in customer.keys():
    print("Llave %s" %(key))

if __name__ == '__main__':
  run()