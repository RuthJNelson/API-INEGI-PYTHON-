# 5.	Encuesta Nacional de Ocupación y Empleo
# a.	Periodicidad: trimestral
# b.	Liga: https://www.inegi.org.mx/programas/enoe/15ymas/default.html#Tabulados

# Librerias

import pandas as pd
import requests, zipfile, io, os
import time

# Inicio del tiempo
start_time=time.time()

#Estableciendo conexion ej: https://www.inegi.org.mx/contenidos/programas/enoe/15ymas/tabulados/indicadores_estrategicos_15ymas_2019_trim1_xls.zip

url_1=" https://www.inegi.org.mx/contenidos/programas/enoe/15ymas/tabulados/indicadores_estrategicos_15ymas_"

# ejmplo 2019, trim1
ano=input("Ingresa el año en 4 digitos ej: 2019: ")
print("Formato trimestre ej: trim1, trim2")
trim=input("Ingresa el trimestre: ")

# url consolidada
url = url_1+ano+"_"+trim+"_xls.zip"

# Crea Data Frame vacio
data=pd.DataFrame([])

# Establece la conexion
r = requests.get(url)
print("El estado de la respuesta es:", r.status_code) # Debe ser 200
z = zipfile.ZipFile(io.BytesIO(r.content))                      
z.extractall() # Descomprime todos
print("Directorios: ", os.listdir())

files=os.listdir(os.getcwd()+"/Entidades")

InF_ENOE = pd.DataFrame([], columns = ["Entidad", "PobTotal", "PobMas15", "PEAOcupada", "PEADesocupada", "PEAInformal"]) # "PorcentajeInformal"

aux = pd.read_excel(os.getcwd()+"/Entidades/"+files[0])

# Consolida directorios (codigo tomado del Word: LigasExogenas)
u=0
for f in files:
  aux = pd.read_excel(os.getcwd()+"/Entidades/" + f)
  InF_ENOE.loc[u, "Entidad"] = f[20:-4]
  InF_ENOE.loc[u, "PobTotal"] = aux.iloc[7,4]
  InF_ENOE.loc[u, "PobMas15"] = aux.iloc[9,4]
  InF_ENOE.loc[u, "PEAOcupada"] = aux[aux["Unnamed: 2"] == "Ocupada"]["Unnamed: 4"].values[0]
  InF_ENOE.loc[u, "PEADesocupada"] = aux[aux["Unnamed: 2"] == "Desocupada"]["Unnamed: 4"].values[0]
  InF_ENOE.loc[u, "PEAInformal"] = aux[aux["Unnamed: 2"] == "Sector informal"]["Unnamed: 4"].values[0]
  # InF_ENOE.loc[u, "PorcentajeInformal"] = aux[aux["Unnamed: 2"] == "PorcentajeInformal"]["Unnamed: 4"].values[0]
  u=u+1



print("-------------------------------Done!-------------------------------") 
end_time=time.time()

time_in_minutes = float(end_time-start_time)/60
print("Tiempo transcurrido en minutos: ", time_in_minutes)

# Ordena por Entidad
InF_ENOE.sort_values(by=["Entidad"], inplace=True)
InF_ENOE.head()