import os
directorio=os.path.dirname(os.path.abspath(__file__))
archivo=os.path.join(directorio,"saludo.txt")
with open(archivo,"r") as lista:
    contenido=lista.read()
    print(contenido)