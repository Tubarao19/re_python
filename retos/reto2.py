# Crea una lista
lista = list(range(1,11))
lista2 = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
lista3 = [23, 87, 45, 12, 67, 34, 78, 90, 56, 11]
# Desordena la lista


# Ordenala en orden ascendente
'''
Buena implementacion.
10/10
'''
lista.sort()
print(f'lista ascendente\n>>> {lista}')

# Ordenala en orden descendente
'''
Buena implementacion.
10/10
'''
lista.reverse()
print(f'lista descendente\n>>> {lista}')
# Encuentra datos exactos
'''
Te falto convertir el dato "str" a "int" con el input recuerda que es una lista de datos numericos y al hacer la busqueda
no te encontrara el dato por el tipo.
3/10
'''
encuentra = int(input('Digita el dato que deseas encontrar\n>>> '))
print(f'El dato exacto es\n>>> {lista[lista.index(encuentra)]}')
# Elimina datos los datos que te dé el usuario
'''
Te falto convertir el dato "str" a "int" con el input recuerda que es una lista de datos numericos y al hacer la busqueda
no te encontrara el dato por el tipo.
3/10
'''
eliminar = int(input('digite el dato que desea eliminar\n>>> '))
print(f'El dato "{lista.pop((lista.index(eliminar)))}" a sido eliminado\n>>> {lista}')
# Suma las posiciones iguales entre 3 listas y su valor se guarda en una 4ta
'''
Buena implementacion.
10/10
'''
lista4 = list(map(lambda x,y,z : x+y+z,lista,lista2,lista3))
print(f'la suma de las 3 listas es:\n>>> {lista4}')
# Multiplica las posiciones iguales entre 2 listas y su valor se acumula en una tercera
'''
Buena implementacion.
10/10
'''
multi = list(map(lambda l1, l2 : l1 * l2, lista, lista2))
print(multi)

# Añade datos a una lista desde la entrada de usuario
'''
Buena implementacion.
10/10
'''
agregar = input('Digite el dato que desea agregar\n>>> ')
lista.append(agregar)
print(lista)
# Invierte la lista
invertido = lista[::-1]
print(f'lista invertida\n>>> {invertido}')
# Vacía toda la lista
'''
Buena implementacion.
10/10
'''
print(f'lista vaciada\n>>> {lista.clear()}')
# Resta las posiciones inversas entre 2 lístas y que su valor se guarde en una 3era lista
'''
Buena implementacion.
10/10
'''
lista.reverse()
lista2.reverse()
lista_3 = list(map (lambda l1, l2 : l1 - l2, lista, lista3))
print(f'El resultado de las listas en reversa restadas es\n>>> {lista_3}')
'''
En resumen te queda en un 8/10, te falto tener en cuenta los cambios de datos al momento de las entradas de datos.
ten mucho cuidado con eso, debido a que al especificar el dato directamente en el input evitas el mal funcionamiento del
codigo. sigue tratando de mejorar la visibilidad del codigo...
'''