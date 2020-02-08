#!/usr/bin/env python
# coding: utf-8

import random

#Definimos los elementos y el objetivo aleatoriamente
def setItems(num):
    items = []
    totalSum = 0
    minor = float("inf")

    for i in range(num):
        rnd = random.randint(1,200)
        items.append(rnd)
        if rnd < minor:
            minor = rnd
        totalSum = totalSum + rnd

    #El objetivo se define entre el mínimo valor de la lista y la máxima suma
    target = random.randint(minor,totalSum)
    
    return items,target

#Eliminamos elementos muy cercanos (dependiendo de delta), pero aún representativos de la lista
def trim(lista,delta):
    trimmed = [lista[0]]
    last = lista[0]
    
    for i in range(1,len(lista)):
        actual = lista[i]
        if actual > last*(1+delta):
            trimmed.append(actual)
            last = actual
    return trimmed

#Mezclamos dos listas ordenadas en otra ordenada
def merge_lists(lista1,lista2):
    lista_unida = []
    e1 = 0
    e2 = 0
    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        e1 = lista1[i]
        e2 = lista2[j]
        if e1 < e2:
            elem = e1
            i+=1
        else:
            elem = e2
            j+=1
        lista_unida.append(elem)
    if i < len(lista1):
        lista_unida = lista_unida + lista1[i:len(lista1)]
    else:
        lista_unida = lista_unida + lista2[j:len(lista2)]
    return lista_unida

#Algoritmo APPROX-SUBSET-SUM
def aprox_subset_sum(lista,t,eps):
    lista_a = [0]
    lista_b = []
    n = len(lista)
    
    for i in range(1,n):
        lista_b = merge_lists(lista_a, list(map(lambda x: lista[i] + x,lista_a)))
        lista_b = trim(lista_b,eps/(2*n))
        lista_b = list(filter(lambda x: x <= t,lista_b))
        lista_a = lista_b
    return max(lista_a)

if __name__ == "__main__":
    items,target = setItems(15)
    print('Items: ' + str(items))
    print('Target: ' + str(target) + '\n')
    
    epsilons = []
    
    #Creación de epsilons
    for i in range(3):
        rnd = 0
        while rnd == 0:
            rnd = random.random()
        epsilons.append(rnd)
        
    #Ejecuciones
    for j in range(3):
        ep = epsilons[j]
        res = aprox_subset_sum(items,target,ep)
        print('Epsilon actual: ' + str(ep))
        print('Resultado del algoritmo: ' + str(res) + '\n')
