from Crypto.Cipher import DES, DES3, AES
from Crypto.Random import get_random_bytes

def ajustar_clave(clave, tamano_requerido):
    if len(clave) < tamano_requerido:
        clave += get_random_bytes(tamano_requerido - len(clave))
    elif len(clave) > tamano_requerido:
        clave = clave[:tamano_requerido]
    print(f"Clave ajustada: {clave.hex()}")
    return clave

def cifrar_y_descifrar(algoritmo, clave, iv, texto):
    texto_bytes = texto.encode('utf-8')
    texto_padded = texto_bytes.ljust((len(texto_bytes) + 7) // 8 * 8)  # ajustar tamaño para el bloque
    
    # Crear el objeto de cifrado y cifrar
    if algoritmo == "DES":
        cipher = DES.new(clave, DES.MODE_CBC, iv)
    elif algoritmo == "3DES":
        cipher = DES3.new(clave, DES3.MODE_CBC, iv)
    elif algoritmo == "AES-256":
        cipher = AES.new(clave, AES.MODE_CBC, iv)
    
    cifrado = cipher.encrypt(texto_padded)
    print(f"Texto cifrado: {cifrado.hex()}")
    
    # Crear un nuevo objeto para descifrar
    if algoritmo == "DES":
        cipher = DES.new(clave, DES.MODE_CBC, iv)
    elif algoritmo == "3DES":
        cipher = DES3.new(clave, DES3.MODE_CBC, iv)
    elif algoritmo == "AES-256":
        cipher = AES.new(clave, AES.MODE_CBC, iv)
        
    descifrado = cipher.decrypt(cifrado).strip()
    print(f"Texto descifrado: {descifrado.decode('utf-8')}\n")

def main():
    texto = input("Ingrese el texto a cifrar: ")
    
    # DES
    clave_des = input("Ingrese la clave para DES (8 bytes): ").encode('utf-8')
    clave_des = ajustar_clave(clave_des, 8)
    iv_des = bytes.fromhex(input("Ingrese el IV en hexadecimal para DES (8 bytes): "))
    cifrar_y_descifrar("DES", clave_des, iv_des, texto)

    # 3DES
    clave_3des = input("Ingrese la clave para 3DES (16 o 24 bytes): ").encode('utf-8')
    clave_3des = ajustar_clave(clave_3des, 24)
    iv_3des = bytes.fromhex(input("Ingrese el IV en hexadecimal para 3DES (8 bytes): "))
    cifrar_y_descifrar("3DES", clave_3des, iv_3des, texto)

    # AES-256
    clave_aes = input("Ingrese la clave para AES-256 (32 bytes): ").encode('utf-8')
    clave_aes = ajustar_clave(clave_aes, 32)
    iv_aes = bytes.fromhex(input("Ingrese el IV en hexadecimal para AES-256 (16 bytes): "))
    cifrar_y_descifrar("AES-256", clave_aes, iv_aes, texto)

if __name__ == "__main__":
    main()
