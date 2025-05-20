import os

def eliminar_archivo(nombre_archivo):
    # ⚠️ Código inseguro: vulnerable a inyección de comandos
    comando = f"rm {nombre_archivo}"
    os.system(comando)
