
import math 

a = float(input("Ingrese valor del coeficiente a: "))
b = float(input("Ingrese valor del coeficiente b: "))
c = float(input("Ingrese valor del coeficiente c: "))

x1= (-b + (b*b - 4*a*c)**(1/2))/(2*a)
x2= (-b - (b*b - 4*a*c)**(1/2))/(2*a)

print(f"\nLa raiz cuadratica de x1 es: {x1:.3f}")
print(f"La raiz cuadratica de x2 es: {x2:.3f}")
