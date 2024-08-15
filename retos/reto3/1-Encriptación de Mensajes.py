# Encriptación de Mensajes:
# Crea un programa que encripte y desencripte mensajes usando un cifrado César.
abcedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

mensaje = input('Digite aqui su mensaje a encriptar\n>>> ')
desplazamiento = int(input('Digite el numero de desplazamiento\n>>> '))

# Usa loops para desplazar los caracteres y maneja casos de excepción para 
#for 
def encriptar(mensaje, desplazamiento, encriptado = ''):
    for letra in mensaje.upper():
        try:
            indice = abcedario.index(letra)  # Encuentra la posición de la letra
            indice += desplazamiento  # Desplaza la letra
            if indice >= 27:  # Si el índice supera las 27 letras, vuelve a empezar
                indice -= 27
            encriptado += abcedario[indice]  # Añade la letra encriptada al resultado
        except ValueError:
            encriptado += letra  # Si el dato dado no está en el abecedario, se añade    
    return encriptado
constraseña = encriptar(mensaje, desplazamiento)
print(constraseña)

# caracteres especiales.
#try, except ? *, etc
'''for letra in mensaje.upper():
        if letra in abcedario:#si se encuentra dicha letra que almacene la 
            indice = abcedario.find(letra)#posicion donde este en la variable indice
            indice += desplazamiento #una vez encontrada sumar para encontrar el reemplazo
            if indice >= 27:#si supera las 27 letras entonces vuelve a empezar
                indice -= 27
            encriptado += abcedario[indice]
        else:
            encriptado += letra#si hay un dato que no se encuentra se añade'''


encrip = input("Digite la clave que desea desencriptar\n>>> ")
#desencriptar
def desencriptar(encrip):
    for clave in range(1, len(abcedario)):
        mensaje = ""
        for letra in encrip.upper():
            try:
                indice = abcedario.index(letra)  # Encuentra la posición de la letra
                indice -= clave  # Desplaza la letra según la clave
                if indice < 0:  # Si el índice es negativo, se ajusta al final del abecedario
                    indice += len(abcedario)
                mensaje += abcedario[indice]  # Añade la letra desencriptada al resultado
            except ValueError:
                mensaje += letra  # Si la letra no está en el abecedario, se añade tal cual
        print(f'\n>>> El número de desplazamiento es: {clave} y el mensaje desencriptado es:\n{mensaje}')

desencriptar(encrip)

'''for clave in range(1, len(abcedario)):
        frase = ""
        for letra in encrip.upper():
            if letra in abcedario:#si se encuentra dicha letra que almacene la 
                indice = abcedario.index(letra)#posicion donde este en la variable indice
                indice -= clave #una vez encontrada sumar para encontrar el reemplazo
                if indice < 0:#si supera las 27 letras entonces vuelve a empezar
                    indice += 27
                frase += abcedario[indice]
            else:
                frase += letra#si hay un dato que no se encuentra se añade
        print(f'Numero de desplazamiento: {clave} mensaje encriptado:>>> {frase}')'''