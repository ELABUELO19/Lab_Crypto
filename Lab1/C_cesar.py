import sys

def cifrar_cesar(texto, desplazamiento):
    texto_cifrado = ""
    for caracter in texto:
        # Verifica si el caracter es una letra
        if caracter.isalpha():
            # Obtiene el valor ASCII del caracter
            valor = ord(caracter)
            # Calcula el desplazamiento aplicado al valor ASCII
            nuevo_valor = valor + desplazamiento
            # Verifica si el nuevo valor está fuera del rango de letras en ASCII
            if caracter.islower():
                if nuevo_valor > ord('z'):
                    nuevo_valor -= 26
                elif nuevo_valor < ord('a'):
                    nuevo_valor += 26
            elif caracter.isupper():
                if nuevo_valor > ord('Z'):
                    nuevo_valor -= 26
                elif nuevo_valor < ord('A'):
                    nuevo_valor += 26
            # Agrega el caracter cifrado al texto cifrado
            texto_cifrado += chr(nuevo_valor)
        else:
            # Si el caracter no es una letra, se agrega tal cual al texto cifrado
            texto_cifrado += caracter
    return texto_cifrado

if __name__ == "__main__":
    # Verifica si se proporcionaron los argumentos adecuados
    if len(sys.argv) != 3:
        print("Uso: sudo python3 programa.py 'String a cifrar' <desplazamiento>")
        sys.exit(1)
    
    # Obtener el texto y el desplazamiento de los argumentos de línea de comandos
    texto = sys.argv[1]
    desplazamiento = int(sys.argv[2])
    
    # Cifra el texto utilizando el cifrado César
    texto_cifrado = cifrar_cesar(texto, desplazamiento)
    
    # Imprime el texto cifrado
    print("Texto cifrado:", texto_cifrado)

    	

