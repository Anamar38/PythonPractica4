import requests
import json
from datetime import datetime

def obtener_precio_bitcoin():
   
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos["bpi"]["USD"]["rate"]

def guardar_datos_en_archivo(precio, archivo="datos_bitcoin.txt"):
   
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    datos_a_almacenar = f"{fecha_hora_actual} - Precio de Bitcoin: {precio} USD\n"

    # Guardar los datos en el archivo
    with open(archivo, "a") as archivo_txt:
        archivo_txt.write(datos_a_almacenar)

if __name__ == "__main__":
  
    precio_bitcoin = obtener_precio_bitcoin()

    # Guardar los datos en el archivo
    guardar_datos_en_archivo(precio_bitcoin)

    print(f"Datos almacenados en datos_bitcoin.txt")