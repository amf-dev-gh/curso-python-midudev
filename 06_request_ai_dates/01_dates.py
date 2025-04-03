# Trabajando con fechas y horas en python

from datetime import datetime, timedelta

# Obtener la hora actual
now = datetime.now()
print("Fecha y hora actual ", now)

# Crear una fecha y hora especifica
specific_date = datetime(1994, 5, 23, 9, 30)
print(specific_date)

# Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato especificado
# formato:

# Se puede cambiar el idioma de las fechas, por defecto en ingles
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

format_date = now.strftime("%A %B %Y %H:%M:%S")
print(f"Fecha formateada: {format_date}")

## Operaciones con fechas. sumar, restar dias, minutos
yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Mañana: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hour_after}")

## Obtener propiedades individuales de una fecha
year = now.year
print(year)

day = now.day
print(day)

# Cacuclar diferencia entre fechas
date1 = datetime.now()
date2 = datetime(2025, 5, 23)
diferece = date2 - date1
print(diferece)