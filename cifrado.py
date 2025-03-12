"""
Implementación del Cifrado César en Python.
Este programa permite cifrar y descifrar textos utilizando un desplazamiento definido por el usuario.
"""

def cifrar_cesar(texto, clave):
    """
    Cifra un texto utilizando el Cifrado César.
    
    :param texto: str - Texto a cifrar.
    :param clave: int - Número de posiciones a desplazar en el alfabeto.
    :return: str - Texto cifrado.
    """
    texto_cifrado = ""  # Inicializa una cadena vacía para el texto cifrado
    
    for caracter in texto:
        if caracter.isalpha():  # Verifica si es una letra (ignora números y símbolos)
            mayuscula = caracter.isupper()  # Comprueba si es mayúscula
            caracter = caracter.lower()  # Convierte la letra a minúscula para el cálculo ASCII
            
            # Obtiene el valor ASCII y aplica la fórmula de desplazamiento
            ascii_valor = ord(caracter)
            nuevo_ascii = ((ascii_valor - 97 + clave) % 26) + 97  # 'a' = 97 en ASCII
            
            nuevo_caracter = chr(nuevo_ascii)  # Convierte el nuevo ASCII a carácter
            if mayuscula:
                nuevo_caracter = nuevo_caracter.upper()  # Si era mayúscula, la vuelve mayúscula
            
            texto_cifrado += nuevo_caracter  # Agrega el carácter cifrado al resultado
        else:
            texto_cifrado += caracter  # Mantiene espacios y otros caracteres sin modificar

    return texto_cifrado

def descifrar_cesar(texto_cifrado, clave):
    """
    Descifra un texto cifrado con el Cifrado César.
    
    :param texto_cifrado: str - Texto cifrado.
    :param clave: int - Número de posiciones con las que se cifró el texto.
    :return: str - Texto descifrado.
    """
    return cifrar_cesar(texto_cifrado, -clave)  # Invierte el desplazamiento para descifrar

# === Interacción con el usuario ===
texto_original = input("Ingrese el texto que desea cifrar: ")
clave = int(input("Ingrese la clave para cifrar (un número entero): "))

# Cifrar el texto ingresado
texto_cifrado = cifrar_cesar(texto_original, clave)
print("Texto cifrado:", texto_cifrado)

# Descifrar el texto cifrado
texto_descifrado = descifrar_cesar(texto_cifrado, clave)
print("Texto descifrado:", texto_descifrado)



# Instrucciones para correr el código

# 1. Copia el código a un editor de texto.

# 2. Escribe el texto o la frase que deseas cifrar en la variable "texto".

# 3. Escribe la clave para realizar el cifrado en la variable "clave".

# 4. Ejecuta el código con Ctrl + Enter.

# Nota: Este código puede ser modificado para cifrar o descifrar textos en otros alfabéticos, como el español, o incluso en otros idiomas. En ese caso, debes cambiar la variable "ascii_valor" y el código que calcula el valor ASCII del carácter.

