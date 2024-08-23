from datetime import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.now()

# Formatear la fecha y hora como una cadena
fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

# Crear un fichero y escribir la fecha y hora en él
with open("fecha_hora.txt", "w") as fichero:
    fichero.write("Fecha y Hora: " + fecha_hora_formateada)

print("Fichero creado con la fecha y hora actual.")