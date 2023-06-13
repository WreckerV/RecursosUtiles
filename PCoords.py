#Hola! Apoyandome en la libreria pyproj, hice un código de python que te 
# Permite pasar de coordenadas de latitud y longitud en coordenadas UTM 




import pyproj
import pandas as pd

columnas_deseadas = ['Latitud', 'Longitud']
df = pd.read_csv('AquiVaTuArchivo.csv', usecols=columnas_deseadas)

def convertir_a_utm(latitud, longitud):
    # Definir los sistemas de referencia
    sistema_geografico = pyproj.Proj(proj='latlong', datum='WGS84')
    sistema_utm = pyproj.Proj(proj='utm', zone=14, datum='WGS84')  # Ajusta la zona UTM según tu ubicación

    # Convertir las coordenadas
    easting, northing = pyproj.transform(sistema_geografico, sistema_utm, longitud, latitud)

    return easting, northing

# Aplicar la conversión a cada fila del DataFrame
df['Easting'], df['Northing'] = zip(*df.apply(lambda row: convertir_a_utm(row['Latitud'], row['Longitud']), axis=1))

# Guardar el DataFrame con los resultados en un archivo Excel
archivo_excel = 'AquiElNombreDelArchivoNuevo.xlsx'
df.to_excel(archivo_excel, index=False)

print("Resultados exportados exitosamente a un archivo Excel.")




#-----------------------------------Created for BrianDJV------------------------



