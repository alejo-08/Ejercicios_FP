# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:08:32 2021

@author: cebal
"""
#Ejercicio5
print("")
print(" NÚMEROS PRIMOS ENTRE 1 Y 1000: ")
print("")
#Constantes 
primero=2
limite=1000
#Inicializando
cont=0
#Proceso
for i in range(primero,limite):
    primo= True
    j= 2
    
    while (i>j) and (primo== True ):
        if i%j == 0:
            #como no se considera el numero (i) y el 1 
            #si otro numero dive a i entonces ya tendria 
            #tres divisores. por lo tanto, no es primo
            primo = False
            break #por tal motivo se rompe el ciclo
        else: 
            j = j+1
            
    if primo== True:
         print(i, "Es primo.")
         cont = cont+1
#salida
print("\nSALIDA: ")
print("")
print("Entre", primero, "y", limite, "hay", cont, "#_primos")