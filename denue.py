# Programa para descarga de datos: 
# 1.	DENUE: (FINALIZADO USANDO WEB Scraping)
# a.	Periodicidad: Anual 
# b.	Liga: https://www.inegi.org.mx/app/descarga/?ti=6

# Librerias

import pandas as pd # DataFrame
import requests # Conexion
import zipfile # Archivos ZIP
import io # bytes
import os # Sistema operativo
import time # Tiempo

# Para tomar el tiempo 
start_time=time.time()

#Estableciendo conexion
url_DENUE="https://www.inegi.org.mx/contenidos/masiva/denue/denue_00_"
formato="_csv.zip"


# Para otros años cambia la url ejemplo: 
# https://www.inegi.org.mx/contenidos/masiva/denue/denue_00_55_1118_csv.zip
# Para el 11/2018


# Listado de clases
lista=["55","52","46111","46112-46311","46321-46531","46591-46911","53","81"]

# 55 Corporativos
# 52 Servicios Financieros y de Seguros
# 46111 Comercio al por menor 1
# 46112-46311 Comercio al por menor 2
# 46321-46531 Comercio al por menor 3
# 46591-46911 Comercio al por menor 4
# 53 Servicios inmobiliarios y de alquiler de bienes muebles e intangibles 
# 81_1118	Otros servicios excepto actividades gubernamentales 

# Crea Data Frame vacio
data=pd.DataFrame([])

# Para cada n en la lista hace una consulta, descomprime y hace un Data Frame
for n in lista:
  r = requests.get(url_DENUE + n + formato)
  print("El estado de la respuesta es:", r.status_code) # Debe ser 200
  z = zipfile.ZipFile(io.BytesIO(r.content))                                  
  z.extract("conjunto_de_datos/denue_inegi_"+n+"_.csv") # Descomprime
  #print("Directorios: ", os.listdir())
  
  temp_data=pd.read_csv("conjunto_de_datos/denue_inegi_"+n+"_.csv",  encoding='latin-1')
  #data=pd.DataFrame([], columns=temp_data.columns)
                   
  df=pd.concat([data,temp_data],axis=0)       
  
  
                    
print("-------------------------------Done!-------------------------------") 
end_time=time.time()

time_in_minutes = float(end_time-start_time)/60

# Tiempo total
print("Tiempo transcurrido en minutos: ", time_in_minutes)


df. shape # dimensiones
df.head() # Primeros datos