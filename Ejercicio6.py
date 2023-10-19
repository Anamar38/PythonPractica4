import re

def contar_lineas_codigo(archivo):
    try:
        with open(archivo, 'r') as file:
            lineas_codigo = [linea for linea in file.readlines() if es_linea_codigo(linea)]
            return len(lineas_codigo)
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def es_linea_codigo(linea):
    
    return re.search(r'\S', linea) and not linea.strip().startswith("#")

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ").strip()

    # Verificar si la ruta termina con '.py'
    if not ruta_archivo.lower().endswith('.py'):
        print("El archivo no tiene extensión .py.")
        return

    cantidad_lineas_codigo = contar_lineas_codigo(ruta_archivo)

    if cantidad_lineas_codigo is not None:
        print(f"El archivo tiene {cantidad_lineas_codigo} líneas de código (excluyendo comentarios y líneas en blanco).")

if __name__ == "__main__":
    main()
