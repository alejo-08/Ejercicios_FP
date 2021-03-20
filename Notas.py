nota1=float(input("Ingrese nota primer parcial:"))
nota2=float(input("Ingrese nota segundo parcial:"))
nota3=float(input("Ingrese nota tercer parcial:"))
suma= nota1+nota2+nota3
promedio= suma/3
if promedio>=3:
    print("Aprobó la materia: ",promedio)
else:
    print("Reprobó la materia: ",promedio)
