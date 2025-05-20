import os
import subprocess

def eliminar_archivo(nombre_archivo):
    try:
        os.remove(nombre_archivo)
    except FileNotFoundError:
        print("Archivo no encontrado.")

