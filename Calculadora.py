num1 = float(input("Digite un numero: "))
num2 = float(input("Digite un numero: "))

operacion = input("Digite la inicial de la operacion: ").upper()

if operacion=='S':
    suma = num1+num2
    print(f"\nLa suma es: {suma}")
elif operacion == 'R':
    resta = num1-num2
    print(f"\nLa resta es: {resta}")
elif operacion =='M' or operacion== 'P':
    mult = num1*num2
    print(f"\nLa multiplicacion es: {mult}")
elif operacion =='D':
    div = num1/num2
    print(f"\nLa division es: {div:.2f}")
else:
    print("\nSe equivoco de operacion ")
    
 
