nombre: str = input("Ingrese su nombre: ")
horas_trabajadas: int = int(input("Ingrese la cantidad de horas que ha trabajado: "))
salario_hora: float = float(input("Ingrese el salario básico por hora: "))
salario_neto: float = salario_hora * horas_trabajadas
bonificacion: float = (salario_neto * 10) / 100
salario_total: float = salario_neto + bonificacion

print("-------------------------------------")
print("Datos del empleado:")
print(f"Nombre: {nombre}")
print(f"Horas trabajadas: {horas_trabajadas}")
print(f"Salario por hora: ${salario_hora}")
print(f"Salario neto: ${salario_neto}")
print(f"Bonificación (10%): ${bonificacion}")
print("-------------------------------------")
print(f"Salario total: ${salario_total}")
