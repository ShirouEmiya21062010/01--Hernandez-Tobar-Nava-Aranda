import os
 
directorio = os.path.dirname(os.path.abspath(__file__))
archivo_numeros = os.path.join(directorio, "numeros.txt")
archivo_resultado = os.path.join(directorio, "resultado.txt")
 
# Numero linea por linea 
numeros = [12, 7, 25, 3, 18, 9, 30, 14, 21, 5]
with open(archivo_numeros, "w") as f:
    for n in numeros:
        f.write(f"{n}\n")
 
# Leer el archivo y calcular el promedio
with open(archivo_numeros, "r") as f:
    valores = [float(linea.strip()) for linea in f if linea.strip()]
 
promedio = sum(valores) / len(valores)
 
# Guardar el resultado en resultado.txt
with open(archivo_resultado, "w") as f:
    f.write(f"El promedio es: {promedio}\n")
 
print(f"Promedio calculado: {promedio}")
print(f"Resultado guardado en: {archivo_resultado}")