# Preguntar cuánto recibiste de sueldo
sueldo = float(input("¿Cuánto recibiste de sueldo, Sergio? "))

# Mostrar el sueldo total recibido
print(f"\nRecibiste en total: ${sueldo:.2f}\n")

# Calcular la distribución del sueldo
ahorro = sueldo * 0.50
casa = sueldo * 0.10
comida = sueldo * 0.20
personal = sueldo * 0.20

# Mostrar la distribución del sueldo de manera más clara
print("Distribución del sueldo:")
print(f"  Ahorro:           ${ahorro:.2f}")
print(f"  Gastos Casa:      ${casa:.2f}")
print(f"  Comida Semana:    ${comida:.2f}")
print(f"  Gastos Personales: ${personal:.2f}")

input("\nPresiona Enter para salir...")