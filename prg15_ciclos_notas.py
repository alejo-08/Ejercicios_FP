# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:44:28 2021

@author: cebal
"""


print("SISTEMA DE NOTAS DE UN CURSO DE PROGRAMACION")
#Entrada

numeroEstudiantes=int(input("Digite la cantidad de estudiantes en el grupo: "))

# Declarar la variable que controla el ciclo 
contadorRepeticiones = 0
cantidadEstudiantesAprobaron=0
cantidadEstudiantesReprobaron=0
sumaDefinitivaEstudiantes=0
sumaDefinitivaEstudiantesAprobaron=0
sumaDefinitivaEstudiantesReprobaron=0
promedioDefinitivaEstudiantes=0.0
promedioDefinitivaEstudiantesAprobaron=0
promedioDefinitivaEstudiantesReprobaron=0
# Proceso 
# Iniciar el ciclo

while contadorRepeticiones< numeroEstudiantes:
    # Lectura de las notas de cada estudiante 
    nombreEstudiante = (input("Digite nombre del estudiante: "))
    notaUnoEstudiante = float(input("Digite la nota del primer parcial del estudiante: "))
    notaDosEstudiante = float(input("Digite la nota del segundo parcial del estudiante: "))
    notaTresEstudiante = float(input("Digite la nota del tercer parcial del estudiante: "))
    # Calcular la definitiva de cada estudiante 
    notaDefinitiva = (notaUnoEstudiante+notaDosEstudiante+notaTresEstudiante)/3
    # Sumar las definitivas de loa estudiantes para calcular el promedio
    sumaDefinitivaEstudiantes=sumaDefinitivaEstudiantes+notaDefinitiva
    print(f"1. La definitiva es: {notaDefinitiva}")
    
    if(notaDefinitiva>=3.0):
        cantidadEstudiantesAprobaron=cantidadEstudiantesAprobaron+1
        # Sumar las notas estudiantes que aprobaron 
        sumaDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesAprobaron+notaDefinitiva 
    else:
        cantidadEstudiantesReprobaron=cantidadEstudiantesReprobaron+1
        # Sumar las notas estudiantes que reprobaron
        sumaDefinitivaEstudiantesReprobaron=sumaDefinitivaEstudiantesReprobaron+notaDefinitiva
     
    # Incrementar la variable que controla el ciclo 
    contadorRepeticiones = contadorRepeticiones+1
    
    # Fin del ciclo 
# Calcular el promedio del grupo 
promedioDefinitivaEstudiantes=sumaDefinitivaEstudiantes/numeroEstudiantes

if(cantidadEstudiantesAprobaron>0):
   promedioDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesAprobaron/cantidadEstudiantesAprobaron
if(cantidadEstudiantesReprobaron>0):
   promedioDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesReprobaron/cantidadEstudiantesReprobaron
print("OTROS CALCULOS")
print(f"2.  Cantidad de estudiantes que aprobaron: {cantidadEstudiantesAprobaron}")
print(f"3.  Cantidad de estudiantes que reprobaron: {cantidadEstudiantesReprobaron}")
print(f"4.  Promedio del grupo: {promedioDefinitivaEstudiantes}")
print(f"5.  Promedio estudiantes que aprobaron: {promedioDefinitivaEstudiantesAprobaron:.2f}")
print(f"6.  Promedio estudiantes que reprobaron: {promedioDefinitivaEstudiantesReprobaron:.2f}")



