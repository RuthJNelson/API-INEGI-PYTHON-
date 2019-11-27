# 9.	CONAPO: Índice de marginación
# a.	Periodicidad: 5 años
# b.	Liga:http://conapo.gob.mx/es/CONAPO/Datos_Abiertos_del_Indice_de_Marginacion

# Librerias

import pandas as pd
import time

# Inicio del tiempo
start_time=time.time()

# Descarga los .csv
# OJO CON LOS CAMPOS COMBINADOS
Indice_EF=pd.read_csv("http://conapo.gob.mx/work/models/CONAPO/Marginacion/Datos_Abiertos/Entidad_Federativa/Base_Indice_de_marginacion_estatal_90-15.csv", encoding='latin-1') # Índice de marginación por entidad federativa 1990 - 2015 
Indice_MM=pd.read_csv("http://conapo.gob.mx/work/models/CONAPO/Marginacion/Datos_Abiertos/Municipio/Base_Indice_de_marginacion_municipal_90-15.csv", encoding='latin-1') #Índice de marginación por municipio 1990 - 2015
Indice_Loc=pd.read_csv("http://conapo.gob.mx/work/models/CONAPO/Marginacion/Datos_Abiertos/Localidad/Base_marginacion_localidad_95-10.csv", encoding='latin-1') # Índice de marginación por localidad 1995 - 2010
Indice_AGEB=pd.read_csv("http://conapo.gob.mx/work/models/CONAPO/Marginacion/Datos_Abiertos/AGEB_Urbana/Base_marginacion_AGEB_00-10.csv", encoding='latin-1') # Índice de marginación por AGEB urbana 2000 - 2010


print("-------------------------------Done!-------------------------------") 
end_time=time.time()
# Tiempo final
time_in_minutes = float(end_time-start_time)/60
print("Tiempo transcurrido en minutos: ", time_in_minutes)

# Encabezados
Indice_EF.head()
Indice_MM.head()
Indice_Loc.head()
Indice_AGEB.head()