import tkinter as tk
from tkinter import ttk, messagebox
import hashlib  # Nueva importación para MD5

# === Funciones de Cifrado César ===

def cifrar_cesar(texto, clave):
    texto_cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            mayuscula = caracter.isupper()
            caracter = caracter.lower()

            ascii_valor = ord(caracter)
            nuevo_ascii = ((ascii_valor - 97 + clave) % 26) + 97

            nuevo_caracter = chr(nuevo_ascii)
            if mayuscula:
                nuevo_caracter = nuevo_caracter.upper()

            texto_cifrado += nuevo_caracter
        else:
            texto_cifrado += caracter

    return texto_cifrado

def descifrar_cesar(texto_cifrado, clave):
    return cifrar_cesar(texto_cifrado, -clave)

# === Funciones de Cifrado MD5 ===

def cifrar_md5(texto):
    if texto == "":
        messagebox.showwarning("Advertencia", "Por favor, ingresa un texto para obtener su hash MD5.")
        return

    hash_obj = hashlib.md5(texto.encode())
    hash_md5 = hash_obj.hexdigest()

    salida_md5.config(state="normal")
    salida_md5.delete(0, tk.END)
    salida_md5.insert(0, hash_md5)
    salida_md5.config(state="readonly")

# === Funciones para la Interfaz ===

def encriptar():
    texto = entrada_encriptar.get()
    try:
        clave = int(entrada_clave_encriptar.get())
        if texto == "":
            messagebox.showwarning("Advertencia", "Por favor, ingresa un texto para encriptar.")
            return

        # Encriptar
        resultado_encriptado = cifrar_cesar(texto, clave)

        # Mostrar texto encriptado
        salida_encriptado.config(state="normal")
        salida_encriptado.delete(0, tk.END)
        salida_encriptado.insert(0, resultado_encriptado)
        salida_encriptado.config(state="readonly")

        # Desencriptar automáticamente
        resultado_desencriptado = descifrar_cesar(resultado_encriptado, clave)

        salida_desencriptado_auto.config(state="normal")
        salida_desencriptado_auto.delete(0, tk.END)
        salida_desencriptado_auto.insert(0, resultado_desencriptado)
        salida_desencriptado_auto.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "La clave debe ser un número entero.")

def desencriptar():
    texto = entrada_desencriptar.get()
    try:
        clave = int(entrada_clave_desencriptar.get())
        if texto == "":
            messagebox.showwarning("Advertencia", "Por favor, ingresa un texto para desencriptar.")
            return

        resultado = descifrar_cesar(texto, clave)
        salida_desencriptado.config(state="normal")
        salida_desencriptado.delete(0, tk.END)
        salida_desencriptado.insert(0, resultado)
        salida_desencriptado.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "La clave debe ser un número entero.")

# === Crear la Ventana Principal ===

ventana = tk.Tk()
ventana.title("🔐 Encriptador de Claves - César y MD5")
ventana.geometry("500x450")
ventana.resizable(False, False)

# === Crear las Pestañas ===

pestanas = ttk.Notebook(ventana)
pestana_encriptar = ttk.Frame(pestanas)
pestana_desencriptar = ttk.Frame(pestanas)
pestana_md5 = ttk.Frame(pestanas)  # Nueva pestaña para MD5

pestanas.add(pestana_encriptar, text="Encriptar César")
pestanas.add(pestana_desencriptar, text="Desencriptar César")
pestanas.add(pestana_md5, text="Hash MD5")  # Nueva pestaña
pestanas.pack(expand=1, fill="both")

# === Contenido de la Pestaña Encriptar César ===

tk.Label(pestana_encriptar, text="Texto a Encriptar:", font=("Arial", 12)).pack(pady=10)
entrada_encriptar = tk.Entry(pestana_encriptar, width=40, font=("Arial", 12))
entrada_encriptar.pack()

tk.Label(pestana_encriptar, text="Clave Numérica (desplazamiento):", font=("Arial", 12)).pack(pady=10)
entrada_clave_encriptar = tk.Entry(pestana_encriptar, width=10, font=("Arial", 12))
entrada_clave_encriptar.pack()

btn_encriptar = tk.Button(pestana_encriptar, text="Encriptar 🔐", command=encriptar, bg="#4CAF50", fg="white", font=("Arial", 12))
btn_encriptar.pack(pady=15)

tk.Label(pestana_encriptar, text="Texto Encriptado:", font=("Arial", 12)).pack()
salida_encriptado = tk.Entry(pestana_encriptar, width=40, font=("Arial", 12), state="readonly")
salida_encriptado.pack()

tk.Label(pestana_encriptar, text="Texto Desencriptado (verificación):", font=("Arial", 12)).pack(pady=10)
salida_desencriptado_auto = tk.Entry(pestana_encriptar, width=40, font=("Arial", 12), state="readonly")
salida_desencriptado_auto.pack()

# === Contenido de la Pestaña Desencriptar César ===

tk.Label(pestana_desencriptar, text="Texto Encriptado:", font=("Arial", 12)).pack(pady=10)
entrada_desencriptar = tk.Entry(pestana_desencriptar, width=40, font=("Arial", 12))
entrada_desencriptar.pack()

tk.Label(pestana_desencriptar, text="Clave Numérica (desplazamiento):", font=("Arial", 12)).pack(pady=10)
entrada_clave_desencriptar = tk.Entry(pestana_desencriptar, width=10, font=("Arial", 12))
entrada_clave_desencriptar.pack()

btn_desencriptar = tk.Button(pestana_desencriptar, text="Desencriptar 🔓", command=desencriptar, bg="#F44336", fg="white", font=("Arial", 12))
btn_desencriptar.pack(pady=15)

tk.Label(pestana_desencriptar, text="Texto Desencriptado:", font=("Arial", 12)).pack()
salida_desencriptado = tk.Entry(pestana_desencriptar, width=40, font=("Arial", 12), state="readonly")
salida_desencriptado.pack()

# === Contenido de la Pestaña MD5 ===

tk.Label(pestana_md5, text="Texto para generar Hash MD5:", font=("Arial", 12)).pack(pady=10)
entrada_md5 = tk.Entry(pestana_md5, width=40, font=("Arial", 12))
entrada_md5.pack()

btn_md5 = tk.Button(pestana_md5, text="Generar MD5 🔐", command=lambda: cifrar_md5(entrada_md5.get()), bg="#2196F3", fg="white", font=("Arial", 12))
btn_md5.pack(pady=15)

tk.Label(pestana_md5, text="Hash MD5:", font=("Arial", 12)).pack()
salida_md5 = tk.Entry(pestana_md5, width=40, font=("Arial", 12), state="readonly")
salida_md5.pack()

# === Ejecutar la App ===
ventana.mainloop()
