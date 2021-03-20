# Leer 3 numeros y leer el tipo de ordenamiento que quiero, e imprimirlos.
# 1. Mayor a menor o 2. Menor a mayor.
tipo = int(input('\n1.- Mayor a menor \n2.- Menor a mayor \nEscoja que tipo de ordenamiento quiere: '))
n1 = int(input('Ingresar número 1: '))
n2 = int(input('Ingresar número 2: '))
n3 = int(input('Ingresar número 3: '))

if tipo == 1:
    if n1 == n2 or n2 == n3 or n1 == n3:
        if n1 == n2 and n2 == n3:
            print('No se puede ordenar, todos los números son iguales')
        else:
            print('No se puede ordenar, dos números son iguales')

    elif n1 >= n2 and n1 >= n3:
        ord1 = n1
        if n2 >= n3:
            ord2 = n2
            ord3 = n3
            print(f'{ord1} - {ord2} - {ord3}')
        else:
            ord2 = n3
            ord3 = n2
            print(f'{ord1} - {ord2} - {ord3}')
    elif n2 >= n1 and n2 >= n3:
        ord1 = n2
        if n1 >= n3:
            ord2 = n1
            ord3 = n3
            print(f'{ord1} - {ord2} - {ord3}')
        else:
            ord2 = n3
            ord3 = n1
            print(f'{ord1} - {ord2} - {ord3}')
    elif n3 >= n1 and n3 >= n2:
        ord1 = n3
        if n1 >= n2:
            ord2 = n1
            ord3 = n2
            print(f'{ord1} - {ord2} - {ord3}')
        else:
            ord2 = n2
            ord3 = n1
            print(f'{ord1} - {ord2} - {ord3}')
elif tipo == 2:
    if n1 == n2 or n2 == n3 or n1 == n3:
        if n1 == n2 and n2 == n3:
            print('No se puede ordenar, todos los números son iguales')
        else:
            print('No se puede ordenar, dos números son iguales')
    elif n1 >= n2 and n1 >= n3:
        ord3 = n1
        if n2 >= n3:
            ord2 = n2
            ord1 = n3
            print(f'{ord1} - {ord2} - {ord3}')
        else:
            ord2 = n3
            ord1 = n2
            print(f'{ord1} - {ord2} - {ord3}')
    elif n2 >= n1 and n2 >= n3:
        ord3 = n2
        if n1 >= n3:
            ord2 = n1
            ord1 = n3
            print(f'{ord1} - {ord2} - {ord3}')
        else:
            ord2 = n3
            ord1 = n1
            print(f'{ord1} - {ord2} - {ord3}')
    elif n3 >= n1 and n3 >= n2:
        ord3 = n3
        if n1 >= n2:
            ord2 = n1
            ord1 = n2
            print(f'{ord1} - {ord2} - {ord3}')
        else:
            ord2 = n2
            ord1 = n1
            print(f'{ord1} - {ord2} - {ord3}')