with open("nombres.txt","w") as archivo:
    for numero in range(1,6):
        nombre=input(f"Escribe el nombre {numero}: ")
        archivo.write(nombre + "\n")