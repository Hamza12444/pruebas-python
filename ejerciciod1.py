"""
Programa Menu de opciones con patrones
Hamza Hanini Moujoud
1ºDAW
"""


CENTINELA = 5
contador = 0
acumulador = 0
mayor = None
menor = None

# Mostrar menú inicial y solicitar la primera opción al usuario
print("Elige 1 para introducir una nota, 2 para ver el numero de notas introducidas, 3 para ver la media y 4 para ver la nota mas alta y baja, 5 es para salir")

opciones = int(input("Introduce una de las opciones: "))

# 2. BUCLE PRINCIPAL DEL MENÚ
while opciones != CENTINELA:
# Opción 1: Entrada, validación de notas [0-10] y actualización de patrones
    if opciones == 1:
        nota = float(input("Introduce una nota: ")) 
        if  nota >= 0 and nota <= 10:
            contador += 1
            acumulador += nota
            # Actualizar nota máxima
            if mayor is None or nota > mayor:
                mayor = nota
            # Actualizar nota mínima
            if menor is None or nota < menor:
                menor = nota
    # Opción 2: Mostrar el total de notas introducidas
    if opciones == 2:
        print(contador)
    # Opción 3: Calcular y mostrar la media (con validación de división por cero)
    if opciones == 3:
        if contador > 0:
            print(f"La media es {acumulador / contador}")
        else:
            print("Debes de introducir una nota")
    # Opción 4: Mostrar la nota más alta y la más baja registradas
    if opciones == 4:
       print(f"Tu nota mas alta es {mayor} y la menor es {menor}")
    # Solicitar nueva opción para continuar o salir del bucle
    opciones = int(input("Introduce una de las opciones: "))