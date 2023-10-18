import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # Extrae el precio de Bitcoin del objeto JSON
        data = response.json()
        precio_bitcoin = float(data["bpi"]["USD"]["rate"].replace(",", ""))  
        
        return precio_bitcoin
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def main():
    try:
        cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))

        precio_bitcoin = obtener_precio_bitcoin()

        if precio_bitcoin is not None:

            costo_en_dolares = cantidad_bitcoins * precio_bitcoin

            print(f"El costo actual de {cantidad_bitcoins} Bitcoins es: ${costo_en_dolares:,.4f}")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()