
def mostrarMenu():
    print('\nAgenda de contactos')
    print('1. Agregar nuevo contacto')
    print('2. Eliminar contacto')
    print('3. Buscar')
    print('4. Lista')
    print('5. Salir')

def agregarContacto(agenda):
    nombre = input('Por favor introduzca el nombre COMPLETO del contacto: ')
    telefono = input('Por favor introduzca el teléfono: ')
    email = input('Por favor introduzca su email: ')
    agenda[nombre] = {'telefono': telefono, 'email': email}
    print(f'Se ha agregado el contacto nombre {nombre} exitosamente')

def eliminarContacto(agenda):
    nombre = input('Ingrese el nombre a elinminar: ')
    if nombre in agenda: 
        del agenda[nombre]
        print(f'El nombre {nombre} ha sido eliminado')
    else:
        print('No se ha encontrado un contacto con el nombre seleccionado')

def buscarContacto(agenda):
    nombre = input('Ingrese nombre a buscar: ')
    if nombre in agenda:
        print(f'Nombre: {nombre}')
        print(f'Teléfono: {agenda[nombre]['telefono']}')
        print(f'Email: {agenda[nombre]['email']}')
    else:
        print(f'El contacto {nombre} no ha sido encontrado.')

def listarContacto(agenda):
    if agenda:
        print('\nLista de contactos: ')
        for nombre,info in agenda.items():
            print(f'Nombre: {nombre}')
            print(f'Telefono: {info['telefono']}')
            print(f'Email: {info['email']}')
            print(('.' * 20))
    else: 
        print('La agenda aún está vacía')

def agendaContacto():
    agenda= {}

    while True:
        mostrarMenu()
        opcion = input('Elija una opción: ')

        if opcion == '1':
            agregarContacto(agenda)
        elif opcion == '2':
            eliminarContacto(agenda)
        elif opcion == '3':
            buscarContacto(agenda)
        elif opcion == '4':
            listarContacto(agenda)
        elif opcion == '5':
            print('Saliendo...')
            break
        else: 
            print('Por favor seleccione una opción válida')

agendaContacto()
