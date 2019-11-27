# 7.	Áreas geoestadísticas municipales:
# a.	Periodicidad: Variable
# b.	Liga: http://conabio.gob.mx/informacion/metadata/gis/muni_2012gw.xml?_xsl=/db/metadata/xsl/fgdc_html.xsl&_indent=no


# Librerias
!pip install geopandas
import geopandas as gpd 
import time
import matplotlib.pyplot as plt

# ANEXO ESTADÍSTICO DE POBREZA A NIVEL MUNICIPIO 2010 Y 2015
# Estableciendo conexion ej: https://www.coneval.org.mx/Medicion/Paginas/AE_pobreza_municipal.aspx

# Inicio del tiempo
start_time=time.time()

# Fuente:
url = "http://www.conabio.gob.mx/informacion/gis/maps/geo/muni_2012gw.zip"

data=pd.DataFrame([])

r = requests.get(url)
print("El estado de la respuesta es:", r.status_code) # Debe ser 200
z = zipfile.ZipFile(io.BytesIO(r.content))                      
z.extractall() # Descomprime todo
print("Directorios: ", os.listdir())

files=os.listdir(os.getcwd())

# con_mun = pd.read_excel("Concentrado, indicadores de pobreza.xlsx", sheet_name="Concentrado municipal")
# con_est = pd.read_excel("Concentrado, indicadores de pobreza.xlsx", sheet_name="Concentrado estatal")

data = gpd.read_file("Muni_2012gw.shp")

print("-------------------------------Done!-------------------------------") 
# Fin del tiempo
end_time=time.time()

time_in_minutes = float(end_time-start_time)/60
print("Tiempo transcurrido en minutos: ", time_in_minutes)

# Encabezado de los datos
data.head()

# Columnas
data.columns

# Informacion
data.info()


# MAPA

fig, ax = plt.subplots(figsize=(15,15))
data.plot(column='cov_', cmap='plasma',ax=ax, legend=True)
ax.set(xticks=[], yticks=[]) #removes axes
ax.set_title("México", fontsize='large')
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')


#add the legend and specify its location
leg = ax.get_legend()