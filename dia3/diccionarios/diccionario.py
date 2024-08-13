# Ejercicio: Contar la cantidad de veces que cada número aparece en una lista y almacenarlo en un diccionario.

# Datos: [2, 7, 10, 15, 16, 10, 22, 35, 10, 2]
# Ejercicio: Contar la cantidad de palabras que comienzan con cada letra y almacenarlo en un diccionario.

# Datos: ["apple", "banana", "orange", "umbrella", "avocado", "grape", "elephant"]
# Ejercicio: Contar cuántos números en una lista son mayores que 10 y almacenarlos en un diccionario bajo una clave específica.

# Datos: [3, 12, 9, 15, 7, 20, 8, 30]
# Ejercicio: Contar la cantidad de caracteres en una cadena y almacenar la frecuencia de cada carácter en un diccionario.

# Datos: "Hello World! This Is A Test String."
# Ejercicio: Contar cuántas veces aparece cada carácter en una cadena y almacenar el conteo en un diccionario.

# Datos: "abracadabra"
# Ejercicio: Contar la cantidad de palabras en una lista que tienen más de 5 letras y almacenar el conteo bajo una clave específica en un diccionario.

# Datos: ["short", "longer", "lengthy", "tiny", "massive", "small", "huge"]
# Ejercicio: Contar cuántos elementos en una lista de números son múltiplos de 3 y almacenar el conteo bajo una clave específica en un diccionario.

# Datos: [1, 3, 6, 7, 9, 12, 14, 18, 21, 25, 27]
# Ejercicio: Contar la cantidad de valores únicos en una lista y almacenarlos en un diccionario con su frecuencia.

# Datos: [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 7]
# Ejercicio: Contar cuántos elementos en una lista de listas tienen una longitud mayor a 2 y almacenar el conteo bajo una clave específica en un diccionario.

# Datos: [[1, 2], [3, 4, 5], [6], [7, 8, 9], [10, 11], [12, 13, 14]]
# Ejercicio: Contar cuántas palabras en una cadena de texto tienen una longitud menor o igual a 4 letras y almacenar el conteo bajo una clave específica en un diccionario.

# Datos: "This is a test sentence to count words with four or less letters."

dic = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(dic['c2'][1].upper())

# Crea un diccionario llamado mi_dic que almacene la siguiente 
# información de una persona:
# nombre: Karen
# apellido: Jurgens
# edad: 35
# ocupacion: Periodista
# Los nombres de las claves y valores deben ser iguales a la consigna.

mi_dic = dict(nombre='Karen', apellido='Jurgens', edad=35, ocupacion='Periodista')
print(mi_dic)

# Actualiza la información de nuestro diccionario llamado 
# mi_dic  (reasignando nuevos valores a las 
# claves según corresponda), y agrega una nueva clave llamada 
# "pais" (sin tilde). Los nuevos datos son:
# nombre: Karen
# apellido: Jurgens
# edad: 36
# ocupacion: Editora
# pais: Colombia
mi_dic = dict(nombre='Karen', apellido='Jurgens', edad=36, ocupacion='Editora', pais='colombia')
print(mi_dic)