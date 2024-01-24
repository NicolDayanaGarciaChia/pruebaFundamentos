base = float(input("ingresa el lado del triangulo: "))
altura = float(input("Ingresa el lado del triangulo: "))

area = (base * altura) / 2
print("el area del triangulo es: ", area)

if area > 1000:
    print("DATOS NO VALIDOS")


