# 3.	Reporte de Inclusión Financiera, CNBV:
# a.	Periodicidad: Trimestral 
# b.	Liga: https://www.cnbv.gob.mx/Inclusi%C3%B3n/Paginas/Bases-de-Datos.aspx

# Programa modificado

# Librerias

import csv
import xlrd
import requests
import os
import pandas as pd
import time

os.getcwd()

# Protocolo WEB para la conexion
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# tiempo de inicio
start_time=time.time()


# Se debe ingresar el año y el mes del consulta:
print("Ingresa el año de la consulta ej: 2019, 2018 ...")
ano=input("Año: ")
print("Ingresa el mes de consulta a dos dígitos ej: enero=01, febrero=02, marzo=03")
mes=input("Mes: ")


if ano=="2019" and mes=="03":

  # url ejemoplo: https://www.cnbv.gob.mx/Inclusi%C3%B3n/BasesDeDatos/Base_de_Datos_de_Inclusion_Financiera_201903.xlsm
  url="https://www.cnbv.gob.mx/Inclusi%C3%B3n/BasesDeDatos/Base_de_Datos_de_Inclusion_Financiera_"+ano+mes +".xlsm"

  # Descarga esas hojas y hace un proceso de limpieza
  BD_Infraestructura_Mun=pd.read_excel(url,sheet_name="BD Infraestructura Mun", skiprows=10, usecols="B:AE") # Selecciona desde la fila 10
  BD_Infraestructura_Mun.columns=BD_Infraestructura_Mun.iloc[0].values # Pone los encabezados
  BD_Infraestructura_Mun=BD_Infraestructura_Mun.drop(0) # Borra la primera fila
  # BD_Infraestructura_Mun=BD_Infraestructura_Mun.loc[:,BD_Infraestructura_Mun.columns.notnull()] # Borra la primera columna que se llama nan
  BD_Infraestructura_Mun.head()

  print("Fin descarga 1")

  BD_Infraestructura_Edo=pd.read_excel(url,sheet_name="BD Infraestructura Edo", skiprows=10, usecols="C:AE") # Selecciona desde la fila 10
  BD_Infraestructura_Edo.columns=BD_Infraestructura_Edo.iloc[0].values # Pone los encabezados
  BD_Infraestructura_Edo=BD_Infraestructura_Edo.drop(0) # Borra la primera fila
  # BD_Infraestructura=BD_Infraestructura.loc[:,BD_Infraestructura.columns.notnull()] # Borra la primera columna que se llama nan
  BD_Infraestructura_Edo.head()

  print("Fin descarga 2")

  BD_Tenencia_Uso_Banca_Mun=pd.read_excel(url,sheet_name="BD Tenencia Uso Banca Mun", skiprows=10, usecols="B:AQ") # Selecciona desde la fila 10
  BD_Tenencia_Uso_Banca_Mun.columns=BD_Tenencia_Uso_Banca_Mun.iloc[0].values # Pone los encabezados
  BD_Tenencia_Uso_Banca_Mun=BD_Tenencia_Uso_Banca_Mun.drop(0) # Borra la primera fila
  # BD_Infraestructura=BD_Infraestructura.loc[:,BD_Infraestructura.columns.notnull()] # Borra la primera columna que se llama nan
  BD_Tenencia_Uso_Banca_Mun.head()

  print("Fin descarga 3")

  BD_Tenencia_Uso_Banca_Edo=pd.read_excel(url,sheet_name="BD Tenencia Uso Banca Edo", skiprows=10, usecols="C:AQ") # Selecciona desde la fila 10
  BD_Tenencia_Uso_Banca_Edo.columns=BD_Tenencia_Uso_Banca_Edo.iloc[0].values # Pone los encabezados
  BD_Tenencia_Uso_Banca_Edo=BD_Tenencia_Uso_Banca_Edo.drop(0) # Borra la primera fila
  # BD_Infraestructura=BD_Infraestructura.loc[:,BD_Infraestructura.columns.notnull()] # Borra la primera columna que se llama nan
  BD_Tenencia_Uso_Banca_Edo.head()

  print("Fin descarga 4")



  print("-------------------------------Done!-------------------------------") 
  end_time=time.time()

  time_in_minutes = float(end_time-start_time)/60
  print("Tiempo transcurrido en minutos: ", time_in_minutes)

  # Encabezados
  # BD_Infraestructura_Mun.head()
  # BD_Infraestructura_Edo.head()
  # BD_Tenencia_Uso_Banca_Mun.head()
  # BD_Tenencia_Uso_Banca_Edo.head()
  
  
elif ano=="2018" and mes!="03":
  
  
  # url ejemoplo: https://www.cnbv.gob.mx/Inclusi%C3%B3n/BasesDeDatos/Base_de_Datos_de_Inclusion_Financiera_201903.xlsm
  url="https://www.cnbv.gob.mx/Inclusi%C3%B3n/BasesDeDatos/Base_de_Datos_de_Inclusion_Financiera_"+ano+mes +".xlsm"

  # Descarga esas hojas y hace un proceso de limpieza
  BD_Acceso_Mun=pd.read_excel(url,sheet_name="BD Acceso Mun", skiprows=10, usecols="B:AG") # Selecciona desde la fila 10
  BD_Acceso_Mun.columns=BD_Acceso_Mun.iloc[0].values # Pone los encabezados
  BD_Acceso_Mun=BD_Acceso_Mun.drop(0) # Borra la primera fila
  BD_Acceso_Mun.head()
  
  print("Fin descarga 1")

  
  BD_Acceso_Edo=pd.read_excel(url,sheet_name="BD Acceso Edo", skiprows=10, usecols="C:AG") # Selecciona desde la fila 10
  BD_Acceso_Edo.columns=BD_Acceso_Edo.iloc[0].values # Pone los encabezados
  BD_Acceso_Edo=BD_Acceso_Edo.drop(0) # Borra la primera fila
  BD_Acceso_Edo.head()
  
  print("Fin descarga 2")

  
  BD_Uso_Banca_Mun=pd.read_excel(url,sheet_name="BD Uso Banca Mun", skiprows=10, usecols="B:AQ") # Selecciona desde la fila 10
  BD_Uso_Banca_Mun.columns=BD_Uso_Banca_Mun.iloc[0].values # Pone los encabezados
  BD_Uso_Banca_Mun=BD_Uso_Banca_Mun.drop(0) # Borra la primera fila
  BD_Uso_Banca_Mun.head()

  print("Fin descarga 3")

    
  BD_Uso_Banca_Edo=pd.read_excel(url,sheet_name="BD Uso Banca Edo", skiprows=10, usecols="C:AQ") # Selecciona desde la fila 10
  BD_Uso_Banca_Edo.columns=BD_Uso_Banca_Edo.iloc[0].values # Pone los encabezados
  BD_Uso_Banca_Edo=BD_Uso_Banca_Edo.drop(0) # Borra la primera fila
  BD_Uso_Banca_Edo.head()

  print("Fin descarga 4")



  print("-------------------------------Done!-------------------------------") 
  end_time=time.time()

  time_in_minutes = float(end_time-start_time)/60
  print("Tiempo transcurrido en minutos: ", time_in_minutes)

  
  
  
  # Si el año es 2018 y el mes es marzo
  elif ano=="2018" and mes=="03":
  
  url="https://www.cnbv.gob.mx/Inclusi%C3%B3n/BasesDeDatos/Base%20de%20Datos%20de%20Inclusion%20Financiera%20"+ano+mes +".xlsm"
  
  
  # Descarga esas hojas y hace un proceso de limpieza
  BD_Acceso_Mun=pd.read_excel(url,sheet_name="BD Acceso Mun", skiprows=10, usecols="B:AG") # Selecciona desde la fila 10
  BD_Acceso_Mun.columns=BD_Acceso_Mun.iloc[0].values # Pone los encabezados
  BD_Acceso_Mun=BD_Acceso_Mun.drop(0) # Borra la primera fila
  BD_Acceso_Mun.head()
  
  print("Fin descarga 1")

  
  BD_Acceso_Edo=pd.read_excel(url,sheet_name="BD Acceso Edo", skiprows=10, usecols="C:AG") # Selecciona desde la fila 10
  BD_Acceso_Edo.columns=BD_Acceso_Edo.iloc[0].values # Pone los encabezados
  BD_Acceso_Edo=BD_Acceso_Edo.drop(0) # Borra la primera fila
  BD_Acceso_Edo.head()
  
  print("Fin descarga 2")

  
  BD_Uso_Banca_Mun=pd.read_excel(url,sheet_name="BD Uso Banca Mun", skiprows=10, usecols="B:AQ") # Selecciona desde la fila 10
  BD_Uso_Banca_Mun.columns=BD_Uso_Banca_Mun.iloc[0].values # Pone los encabezados
  BD_Uso_Banca_Mun=BD_Uso_Banca_Mun.drop(0) # Borra la primera fila
  BD_Uso_Banca_Mun.head()

  print("Fin descarga 3")

    
  BD_Uso_Banca_Edo=pd.read_excel(url,sheet_name="BD Uso Banca Edo", skiprows=10, usecols="C:AQ") # Selecciona desde la fila 10
  BD_Uso_Banca_Edo.columns=BD_Uso_Banca_Edo.iloc[0].values # Pone los encabezados
  BD_Uso_Banca_Edo=BD_Uso_Banca_Edo.drop(0) # Borra la primera fila
  BD_Uso_Banca_Edo.head()

  print("Fin descarga 4")



  print("-------------------------------Done!-------------------------------") 
  end_time=time.time()

  time_in_minutes = float(end_time-start_time)/60
  print("Tiempo transcurrido en minutos: ", time_in_minutes)
  
  