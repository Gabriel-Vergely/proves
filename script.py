# ejemplo_inseguro.py
import os

# ⚠️ Este es un ejemplo educativo para probar herramientas de análisis
def eliminar_archivo(nombre_archivo):
    # Vulnerable a inyección de comandos si se usa con input de usuario
    os.system(f"rm {nombre_archivo}")

def funcion_vacia():
