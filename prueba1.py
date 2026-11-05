CENTINELA = -1
acumulador = 0
contador = 0
contador_aprobados = 0
mayor = None

notas = float(input("Introduce la nota: "))

while notas != CENTINELA:
    acumulador += notas
    contador += 1

    if notas >= 5:
        contador_aprobados += 1
    else:
        print("Estas suspendido")

    if mayor is None or notas > mayor:
        mayor = notas
   
    notas = int(input("Introduce la nota: "))


if contador > 0:
    porcentaje = contador_aprobados / contador * 100
    media = acumulador / contador

    print(f"La media es {media}, el porcentaje es {porcentaje}, el numero de aprobados es {contador_aprobados} y la nota mayor es {mayor}")
else:
    print("No se introdujo nota")
