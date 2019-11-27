# 6.	CONEVAL: Medición de la pobreza municipal
# a.	Periodicidad: cada 5 años
# b.	Liga: https://datos.gob.mx/busca/dataset?tags=pobreza


# ANEXO ESTADÍSTICO DE POBREZA A NIVEL MUNICIPIO 2010 Y 2015
# Estableciendo conexion ej: https://www.coneval.org.mx/Medicion/Paginas/AE_pobreza_municipal.aspx

# Librerias

import pandas as pd
import requests
import zipfile
import io
import os
import time


# Tiempo de inicio
start_time=time.time()

# url de conexion
url = "https://www.coneval.org.mx/Medicion/Documents/Pobreza_municipal/Concentrado_indicadores_de_pobreza.zip"

# Data Frame vacio
data=pd.DataFrame([])

# Establece la conexion
r = requests.get(url)
print("El estado de la respuesta es:", r.status_code) # Debe ser 200
z = zipfile.ZipFile(io.BytesIO(r.content))                      
z.extractall() # Descomprime todo
print("Directorios: ", os.listdir())

files=os.listdir(os.getcwd())

# Concentrados
con_mun = pd.read_excel("Concentrado, indicadores de pobreza.xlsx", sheet_name="Concentrado municipal")
con_est = pd.read_excel("Concentrado, indicadores de pobreza.xlsx", sheet_name="Concentrado estatal")

print("-------------------------------Done!-------------------------------") 
# Fin del tiempo
end_time=time.time()

time_in_minutes = float(end_time-start_time)/60
print("Tiempo transcurrido en minutos: ", time_in_minutes)

# encabezados, falta proceso de limpieza
con_mun.head(50)
con_est.head(50)