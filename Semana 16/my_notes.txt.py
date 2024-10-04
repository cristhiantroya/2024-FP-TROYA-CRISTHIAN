# Crea un nuevo archivo llamado my_notes.txt.
my_notes = open('my_notes.txt', 'w')

# Método write(): escribir una línea a la vez
my_notes.write("Nota 1: Reunion a las 3pm.\n")
my_notes.write("Nota 2: Estudiar para el examen .\n")
my_notes.write("Nota 3: Realizar las compras.\n")

# Cierra el archivo después de escribir
my_notes.close()

# Abre el archivo my_notes.txt para lectura.
my_notes = open('my_notes.txt', 'r')

# Lee el contenido del archivo línea por línea utilizando el método adecuado.

# Método 1. read()
print('Método 1: read()')
print('--------------------')
print(my_notes.read())  # Lee todo el contenido del archivo
my_notes.close()  # Cierra el archivo después de leer

# Método 2. readlines()
my_notes = open('my_notes.txt', 'r')  # Vuelve a abrir el archivo para leer
print('Método 2: readlines()')
print('--------------------')
for linea in my_notes.readlines():  # Lee todas las líneas del archivo
    print(linea.rstrip('\n'))  # Imprime cada línea sin el salto de línea final

# Cierra el archivo después de leer
my_notes.close()