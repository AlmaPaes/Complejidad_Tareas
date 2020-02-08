#!/usr/bin/env python
# coding: utf-8

from decimal import Decimal
import random 

items = []
packages = [0]

archivo = input()

#Números aleatorios
if archivo == '':
    #print("auch")
    for i in range(20):
        items.append(random.uniform(0.1,0.9))
        items = list(map(lambda x: round(Decimal(x),5),items))

#Por archivo
else:
    f = open(archivo, "r")
    for x in f:
        items = items + list(map(Decimal,x.split()))
    
#Ordenar items de forma descendente
items.sort(reverse=True)
print('\nItems ordenados:')
print(items)
print()

#Bin packing 
for i in items:
    encaje = False
    for j in range(len(packages)):
        if 1-packages[j] >= i:
            packages[j] = packages[j] + i
            encaje = True
            break
    if encaje == False:
        packages.append(i)

        
#Resultado        
print('Número de paquetes: ' + str(len(packages)) + '\n')
print('Packing:')
print(packages)
