# Generador de tablas de multiplicar: 
# Crea un programa que pida al usuario un número 
# y luego imprima la tabla de multiplicar de ese número, 
# desde 1 hasta 10, utilizando un ciclo for.

usu = int(input('digite el numero a multiplicar\n>>>'))
print(f'la tabla de multiplicar del {usu} es:\n>>>')
contador = 0
for contare in range(1, 11):
    print(f'{usu} x {contador} = {usu * contador}')
    contador += 1