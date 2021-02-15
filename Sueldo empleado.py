
horas_trabajadas = int(input("Ingrese el numero de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por cada hora: "))

sueldo_inicial = horas_trabajadas * valor_hora

bonificacion = sueldo_inicial * (2/100)

t_ingresos= sueldo_inicial+bonificacion

seguro_social= t_ingresos * (9.35/100)

sueldo_total= t_ingresos - seguro_social
print (f"\nEl sueldo del empleado es: {sueldo_total:.2f}")
