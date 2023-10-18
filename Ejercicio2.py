from pyfiglet import Figlet
import random

def obtener_fuente_aleatoria():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()
    return random.choice(fuentes_disponibles)

def main():
    
    fuente_a_usuar = input("Ingrese el nombre de la fuente o presione ENTER para obtener una aleatoria: ")
    fuente_seleccionada = fuente_a_usuar if fuente_a_usuar else obtener_fuente_aleatoria()

    figlet = Figlet()
    figlet.setFont(font=fuente_seleccionada)

    # Solicitar al usuario un texto
    texto_imprimir = input("Ingrese el texto a imprimir: ")

    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()
