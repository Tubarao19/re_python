#crear un detector de textos que tenga las sigts funcionalidades

oracion = input("Digite una oracion\n>>> ")
lista_palabras = oracion.split()


#-que devuelva cada palabra de la ultima oracion
'''
Buena implementacion de formart para ahorrar lineas de codigo.
10/10
'''
print(f"la palabra de la ultima oracion es: {lista_palabras[len(lista_palabras)-1]}\n>>> ")

#-que el string este completamente alreves y que las palabras esten de derecha a izq
print(f"La cadena al reves se veria de la sigt forma\n{' '.join(lista_palabras[::-1])}\n>>> ")

#-que diga si un string o no esta en el texto
'''
Buena implementacion.
10/10
'''
esta = input("Digite un texto que quiera ver si se encuentra\n>>> ")
verificacion = (esta in oracion)
print(f"El resultado de la verificacion es: {verificacion}\n>>> ")

#-cuantas veces aparece dicho caracter
'''
Buena implementacion.
10/10
'''
veces = input("Digite el caracter del que quiera saber el numero de apariciones\n>>> ")
print(f"El caracter elegido aparece la sigt cantidad de veces: {oracion.count(veces)}\n>>> ")

#-que devuelva la ultima letra de cada palabra que este dentro del string

letras = " ".join(map(lambda letra: letra[-1], lista_palabras))
print(f"la ultima letra de la oracion es:\n>>> {letras}")

#-que pueda hacer busqueda

posicion = input("Digite la palabra que desea buscar\n>>> ")
print(f"La frase a buscar se encuentra en la posicion {lista_palabras.index(posicion)}\n>>> ")
print(f"la frase digitada es: {posicion in oracion}\n>>> ")

#-que pueda extraer un string (palabra o frase)

palabra = input("Digite la palabra o frase que desea extraer\n>>> ")
extraer = lista_palabras[lista_palabras.index(palabra)]
print(f"La palabra a extraer es:\n>>> {extraer}")
print(lista_palabras)

'''
En resumen la practica te queda en 5/10 debido a que se le baja unas decimas por
la visualizacion del codigo en la terminal se vuelve engorroso pq todo esta junto,
pudiste aplicar saltos de linea al final de cada punto para separarlo del ejercicio
anterior, lee las correcciones y trata de corregirlas, el codigo se pudo leer bien
en su mayoria y tuviste buenas implementaciones
'''
