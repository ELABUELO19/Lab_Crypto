import sys
import time
from scapy.all import *

def enviar_paquete_icmp(caracter, seq_num, ident, payload_inicial, payload_final):
    # Obtener el timestamp actual en milisegundos
    timestamp = int(time.time() * 1000) % (2**32)
    timestamp_bytes = timestamp.to_bytes(4, 'big')

    # Construir el paquete IP/ICMP con la dirección de destino específica
    paquete = (
        IP(dst="8.8.8.8") /  # Dirección de destino fija
        ICMP(type="echo-request", id=ident, seq=seq_num) /
        (timestamp_bytes + payload_inicial + bytes(caracter, 'utf-8') + payload_final)
    )
    
    # Envía el paquete ICMP
    send(paquete, verbose=True)
    time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: sudo python3 archivo.py 'texto cifrado'")
        sys.exit(1)
    
    texto_cifrado = sys.argv[1]
    
    # Define los valores manualmente
    ident = 0x0009  # Ejemplo de ID coherente
    seq_num_inicial = 1  # Ejemplo de secuencia inicial
    
    # Define los segmentos del payload que deben mantenerse
    payload_inicial = bytes([0x70, 0x6f, 0x55, 0x4e, 0x53, 0x4e, 0x45, 0x41]) 
    payload_final = bytes([0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b, 0x2c, 0x2d, 0x2e, 0x2f, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37])
    
    # Enviar cada caracter como un paquete ICMP a la IP de destino específica
    seq_num = seq_num_inicial
    cont = 0
    for caracter in texto_cifrado:
        cont += 1
        enviar_paquete_icmp(caracter, seq_num, ident, payload_inicial, payload_final)
        seq_num += 1  # Incrementar número de secuencia para coherencia
        if cont%3 == 0:
            ident += 0x0001
        





