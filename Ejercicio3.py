import requests
from PIL import Image
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as f:
            f.write(response.content)
        print(f"Imagen descargada con éxito como {nombre_archivo}")
    else:
        print(f"Error al descargar la imagen. Código de estado: {response.status_code}")

def comprimir_zip(nombre_archivo, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        zipf.write(nombre_archivo, os.path.basename(nombre_archivo))
    print(f"Archivo comprimido como {nombre_zip}")

def descomprimir_zip(nombre_zip, carpeta_destino):
    with zipfile.ZipFile(nombre_zip, 'r') as zipf:
        zipf.extractall(carpeta_destino)
    print(f"Archivo descomprimido en {carpeta_destino}")

def main():
    # URL de la imagen
    url_imagen = "https://unsplash.com/es/fotos/fk4tiMlDFF0" 

    nombre_imagen = "perrito.jpg"
 
    descargar_imagen(url_imagen, nombre_imagen)
    
    #unzip al archivo zipeado
    nombre_zip = "imagenes.zip"

    comprimir_zip(nombre_imagen, nombre_zip)

    carpeta_destino = "imagenes_descomprimidas"

    descomprimir_zip(nombre_zip, carpeta_destino)

if __name__ == "__main__":
    main()
