from Ejemplar import Ejemplar
from Poblacion import Poblacion
from Individuo import Individuo
import random

NUM_GENERACIONES = 1000

NUM_GENERACIONES_MISMO_OPTIMO = 400

NUM_INDIVIDUOS = 50

NUM_MAX_MUTACION = 0.2


def main():
    #Generamos ejemplar aleatoriamente
    ejemplar = Ejemplar()
    poblacion = Poblacion(NUM_INDIVIDUOS,ejemplar)
    #Generamos población inicial
    poblacion.poblacionInicial()
    
    optimo = poblacion.getOptimo()
    
    generacion = 0
    
    mismo_optimo = 0
    
    print("Ejemplar del problema: ")
    print(ejemplar)
    
    print("Encontrando la asignación de verdad óptima:")
    
    while generacion < NUM_GENERACIONES and mismo_optimo < NUM_GENERACIONES_MISMO_OPTIMO:
        if optimo.aptitud == ejemplar.clausulas:
            break
        
        if generacion % 50 == 0:
            print("Generación: " + str(generacion))
            print("Individuo óptimo: " + str(optimo))
            
        nOptimo = poblacion.getOptimo()
        
        if optimo.aptitud == nOptimo.aptitud:
            mismo_optimo = mismo_optimo + 1
        
        nuevaPoblacion = Poblacion(NUM_INDIVIDUOS,ejemplar)
        sujetos = []
        #Reproducimos individuos de la población actual
        listaBebes = poblacion.reproduccion(10,NUM_MAX_MUTACION) # 20
        
        #Lista de los mejores individuos de la población
        mejores = poblacion.conjunto[:13] #13
        
        #Lista de los peores individuos de la población
        peores = poblacion.conjunto[len(poblacion.conjunto)-7:] #7
        
        #Lista de ejemplares promedio de la población
        promedio = poblacion.conjunto[21:26] #5
        
        #Ejemplares creados aleatoriamente
        individuo1 = Individuo(ejemplar.ejemplar)
        individuo1.sujetoInicial(0,ejemplar.variables)
        sujetos.append(individuo1)
        
        individuo2 = Individuo(ejemplar.ejemplar)
        individuo2.sujetoInicial(1,ejemplar.variables)
        sujetos.append(individuo2)
        
        individuo3 = Individuo(ejemplar.ejemplar)
        individuo3.sujetoInicial(2,ejemplar.variables)
        sujetos.append(individuo3)
        
        individuo4 = Individuo(ejemplar.ejemplar)
        individuo4.sujetoInicial(3,ejemplar.variables)
        sujetos.append(individuo4)
        
        individuo5 = Individuo(ejemplar.ejemplar)
        individuo5.sujetoInicial(4,ejemplar.variables)
        sujetos.append(individuo5)
        
        sujetos = sujetos + listaBebes + mejores + peores + promedio
        
        nuevaPoblacion.conjunto = sujetos
        nuevaPoblacion.ordenarIndividuos()
        
        optimo = nOptimo
        poblacion = nuevaPoblacion
        
        generacion = generacion + 1
    
    
    print("Mejor individuo encontrado en la generación: " + str(generacion))
    print(optimo)


if __name__ == "__main__":
    main()
