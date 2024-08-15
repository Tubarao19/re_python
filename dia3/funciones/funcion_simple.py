#creando una funcion simple
# def saludar():
#     print('Que onda viejo como estas?')

# saludar()

#crear funcion con parametro
# def saludar(nombre, sexo):
#     sexo = sexo.lower()
#     if(sexo == "mujer"):
#         adjetivo = "reina"
#     elif(sexo == "hombre"):
#         adjetivo = "titan"
#     else:
#         adjetivo = "no binario"
    
#     print(f"Hola {nombre}, {adjetivo} como estas?")

# saludar("Miguel", "HomBRE")

#crear funcion que retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña
    
password = crear_contraseña_random(4)
print(password)