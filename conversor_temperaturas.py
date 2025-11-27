print("=== Sistema de Conversión de Temperaturas ===")

print("""
Elige la opción que necesites:
1. Convertir de Celsius a Fahrenheit
2. Convertir de Fahrenheit a Celsius
""")

opcion = int(input("Ingresa una opción: "))

if opcion == 1:
    temperatura = float(input("Ingresa la temperatura en °C: "))
    conversion = (temperatura * 1.8) + 32
    print(f"{temperatura}°C equivalen a {conversion}°F")

elif opcion == 2:
    temperatura = float(input("Ingresa la temperatura en °F: "))
    conversion = (temperatura - 32) / 1.8
    print(f"{temperatura}°F equivalen a {conversion}°C")

else:
    print("Opción no válida.")
