from Individuo import Individuo
from Ejemplar import Ejemplar
import random
    
class Poblacion:
    def __init__(self,size,ejemplar):
        self.__size = size
        self.__ejemplar = ejemplar
        self.__conjunto = []
            
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self,newSize):
        self.__size = newSize
        
    @property
    def ejemplar(self):
        return self.__ejemplar
    
    @ejemplar.setter
    def ejemplar(self,newEjemplar):
        self.__ejemplar = newEjemplar
        
    @property
    def conjunto(self):
        return self.__conjunto
    
    @conjunto.setter
    def conjunto(self,newConjunto):
        self.__conjunto = newConjunto

        
    #Posicion de la primera variable no negada en cada cláusula
    def afirmativo(self):
        posiciones = []
        for i in range(0,len(self.ejemplar.ejemplar)):
            for j in range(0,len(self.ejemplar.ejemplar[i])):
                if self.ejemplar.ejemplar[i][j] == 1:
                    posiciones.append(j)
                    break
                if j == len(self.ejemplar.ejemplar[i])-1:
                    posiciones.append(-1)
        return posiciones
        
    #Genera una población inicial
    def poblacionInicial(self):
        #print(len(self.ejemplar.ejemplar[0]))
        noNegadas = self.afirmativo()
        maximo = -1
        for i in range(0,self.size):
            j = noNegadas[i % len(self.ejemplar.ejemplar)]
            actualInd = Individuo(self.ejemplar.ejemplar)
            actualInd.sujetoInicial(j,len(self.ejemplar.ejemplar[0]))
            self.conjunto.append(actualInd)
            self.ordenarIndividuos()
        return self.conjunto
    
    #Ordena a los individuos de la población de acuerdo a su aptitud
    def ordenarIndividuos(self):
        self.conjunto.sort(key = lambda x: x.aptitud, reverse = True)
                
    #Devuelve el individuo con mejor aptitud
    def getOptimo(self):
        return self.conjunto[0]
    
    #Implementación del algoritmo Order Crossover
    def orderCrossover(self,padre1,padre2):
        lista1 = padre1.sujeto
        lista2 = padre2.sujeto
        
        puntoInicio = random.randint(1,len(lista1)-1)
        puntoFinal = random.randint(puntoInicio+1,len(lista1))

        corte1 = lista1[puntoInicio:puntoFinal+1]
        corte2 = lista2[puntoInicio:puntoFinal+1]
        
        hijo1Arr = lista1[puntoFinal+1:len(lista1)][::-1] + corte2 + lista1[0:puntoInicio][::-1]
        hijo2Arr = lista2[puntoFinal+1:len(lista2)][::-1] + corte1 + lista2[0:puntoInicio][::-1]
        
        hijo1 = Individuo(self.ejemplar.ejemplar)
        hijo1.sujeto = hijo1Arr
        hijo1.setAptitud()
        
        hijo2 = Individuo(self.ejemplar.ejemplar)
        hijo2.sujeto = hijo2Arr
        hijo2.setAptitud()
        
        return hijo1,hijo2
    
    #Implementación del algoritmo Partially Mapped Crossover
    def mappedCrossover(self,padre1,padre2):
        lista1 = padre1.sujeto
        lista2 = padre2.sujeto
        
        puntoInicio = random.randint(1,len(lista1)-1)
        puntoFinal = random.randint(puntoInicio+1,len(lista1))

        corte1 = lista1[puntoInicio:puntoFinal+1]
        corte2 = lista2[puntoInicio:puntoFinal+1]

        hijo1Arr = lista1[0:puntoInicio] + corte2 + lista1[puntoFinal+1:len(lista1)]
        hijo2Arr = lista2[0:puntoInicio] + corte1 + lista2[puntoFinal+1:len(lista2)]
        
        hijo1 = Individuo(self.ejemplar.ejemplar)
        hijo1.sujeto = hijo1Arr
        hijo1.setAptitud()
        
        hijo2 = Individuo(self.ejemplar.ejemplar)
        hijo2.sujeto = hijo2Arr
        hijo2.setAptitud()
        
        return hijo1,hijo2
    
    #Reproducción de un número de parejas, cuyos hijos pueden mutar de acuerdo a un factor de mutación
    def reproduccion(self,numParejas,mutacion):
        listaBebes = []
        mejoresPadres = self.conjunto[:numParejas]
        peoresPadres = self.conjunto[self.size-numParejas:]
        
        for i in range(0,numParejas):
            eleccion = random.random()
            if eleccion < 0.5:
                hijo1, hijo2 = self.mappedCrossover(mejoresPadres[i],peoresPadres[i])
            else:
                hijo1, hijo2 = self.orderCrossover(mejoresPadres[i],peoresPadres[i])
                
            probMutacion = random.random()
            if probMutacion <= mutacion:
                hijo1.mutar()
                
                
            probMutacion = random.random()
            if probMutacion <= mutacion:
                hijo2.mutar()
                
            listaBebes.append(hijo1)
            listaBebes.append(hijo2)
            
        return listaBebes
