# Crear un Diccionario
informacion_personal = {
    "nombre": "Diego Torres",
    "edad": 22,
    "ciudad": "Guyaquil",
    "profesion": "Ingeniero"
}

# Acceder y Modificar Valores
# Modificar la ciudad
informacion_personal["ciudad"] = "Cuenca"
# Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "Arquitecto"

# Verificar Existencia de Claves
# Verificar si la clave 'telefono' existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998887777"

# Eliminar una Clave
# Eliminar la clave 'edad'
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el Diccionario Final
print("Información Personal:")
for clave, valor in informacion_personal.items():
    print(f"- {clave}: {valor}")