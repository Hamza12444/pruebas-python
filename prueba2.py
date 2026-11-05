palabra_invertida = ""

palabra = (input("Introduce la palabra: "))

for letra in palabra:
    palabra_invertida = letra + palabra_invertida

if palabra == palabra_invertida:
    print("Es un palindromo")
else:
    print("No es un palindromo")