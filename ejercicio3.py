voltaje1 = float(input("Ingresa el voltaje: "))
voltaje2 = float(input("Ingresa el voltaje: "))
voltaje3 = float(input("Ingresa el voltaje: "))

promedio = (voltaje1 + voltaje2 + voltaje3) / 3
print("El promedio es de: ", promedio)

if promedio < 115:
    print("VOLTAJE CORRECTO")

if  (promedio > 115) and (promedio < 220):
    print("ALTO VOLTAJE")

if (promedio > 220):
    print("PELIGRO")

