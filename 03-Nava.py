import os
directorio = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.join(directorio, "nombres.txt")

with open(archivo, "r") as lista_nombres:
    numero_nombres = len(lista_nombres.readlines())
    print(f"En la lista hay: {numero_nombres}")
    for nombre in lista_nombres:
        print(nombre.strip())