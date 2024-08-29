import sys
import os
from scapy.all import *

def obtener_mensaje(pcapng_file):
    mensaje = ""
    # Lee el archivo pcapng
    for pkt in rdpcap(pcapng_file):
        # Verifica si es un paquete ICMP
        if ICMP in pkt:
            # Extrae el byte de la data del paquete ICMP y lo agrega al mensaje
            data = pkt[ICMP].load
            mensaje += chr(data[12])
    return mensaje

def descifrar_cesar(texto, desplazamiento):
    texto_descifrado = ""
    for caracter in texto:
        # Verifica si el caracter es una letra
        if caracter.isalpha():
            # Obtiene el valor ASCII del caracter
            valor = ord(caracter)
            # Calcula el desplazamiento aplicado al valor ASCII
            nuevo_valor = valor - desplazamiento
            # Ajusta el valor si se sale del rango de letras
            if caracter.islower():
                if nuevo_valor < ord('a'):
                    nuevo_valor += 26
            elif caracter.isupper():
                if nuevo_valor < ord('A'):
                    nuevo_valor += 26
            # Agrega el caracter descifrado al texto descifrado
            texto_descifrado += chr(nuevo_valor)
        else:
            # Si el caracter no es una letra, se agrega tal cual al texto descifrado
            texto_descifrado += caracter
    return texto_descifrado

def cargar_diccionario():
    # Carga un diccionario de palabras en español
    with open("Diccionario.txt", "r", encoding="utf-8") as file:
        return set(word.strip() for word in file)

def imprimir_opciones(texto_original, opciones):
    diccionario_espanol = cargar_diccionario()
    mejor_opcion = None
    max_palabras_en_diccionario = 0
    i = 0
    for opcion in opciones:
        palabras_en_diccionario = sum(1 for palabra in opcion.split() if palabra.lower() in diccionario_espanol)
        if palabras_en_diccionario > max_palabras_en_diccionario:
            mejor_opcion = opcion
            max_palabras_en_diccionario = palabras_en_diccionario

    for opcion in opciones:
        if opcion == mejor_opcion:
            print("\033[92m" + str(i) + ': '+ opcion + "\033[0m")  # Impresión en verde para la opción más probable
            i += 1
        else:
            print(str(i) + ': ' + opcion)
            i += 1

if __name__ == "__main__":
    # Verifica si se proporcionó el argumento adecuado
    if len(sys.argv) != 2:
        print("Uso: python3 programa.py archivo.pcapng")
        sys.exit(1)
    
    # Obtiene el nombre del archivo pcapng de los argumentos de línea de comandos
    archivo_pcapng = sys.argv[1]
    
    # Obtiene el mensaje transmitido del archivo pcapng
    mensaje_transmitido = obtener_mensaje(archivo_pcapng)
    print("Mensaje transmitido:", mensaje_transmitido)
    
    # Genera todas las posibles combinaciones de descifrado utilizando el cifrado César
    opciones_descifrado = []
    for i in range(26):
        opcion = descifrar_cesar(mensaje_transmitido, i)
        opciones_descifrado.append(opcion)
    
    # Imprime las opciones de descifrado, indicando la más probable en verde
    imprimir_opciones(mensaje_transmitido, opciones_descifrado)



