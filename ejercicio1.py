voltaje1 = float(input("ingrese voltaje: "))
voltaje2 = float(input("ingrese voltaje: "))
voltaje3 = float(input("ingrese voltaje: "))
voltaje4 = float(input("ingrese voltaje: "))
voltaje5 = float(input("ingrese voltaje: "))

promedio = (voltaje1 + voltaje2 + voltaje3 + voltaje4 + voltaje5) / 5
print("promedio: ", promedio)

if promedio > 220:
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")
