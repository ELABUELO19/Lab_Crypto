import sys
from scapy.all import *

def enviar_paquete_icmp(caracter, secuencia, identificacion):
    # Crea un paquete ICMP con el caracter en el campo de datos
    paquete = IP(dst="127.0.0.1") / ICMP(type="echo-request", id=identificacion, seq=secuencia) / bytes(caracter, 'utf-8')
    # Envía el paquete ICMP
    send(paquete, verbose=True)

if __name__ == "__main__":
    # Verifica si se proporcionó el argumento adecuado
    if len(sys.argv) != 2:
        print("Uso: sudo python3 archivo.py 'texto cifrado'")
        sys.exit(1)
    
    # Obtener el texto cifrado de los argumentos de línea de comandos
    texto_cifrado = sys.argv[1]
    
    # Genera secuencia e ID diferentes para cada paquete ICMP
    secuencia = 1
    identificacion = 1
    
    # Envía cada caracter del texto cifrado en un paquete ICMP
    for caracter in texto_cifrado:
        enviar_paquete_icmp(caracter, secuencia, identificacion)
        secuencia += 1
        identificacion += 1

