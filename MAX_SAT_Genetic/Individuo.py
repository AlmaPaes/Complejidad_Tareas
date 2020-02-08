import random
    
class Individuo:
    def __init__(self,ejemplar):
        #Arreglo de valores de verdad para las variables de un ejemplar
        self.__sujeto = []
        #Ejemplar a partir del cual se calculará la aptitud del individuo
        self.__ejemplar = ejemplar
        #Aptitud del individuo
        self.__aptitud = 0
        
    @property
    def sujeto(self):
        return self.__sujeto
    
    @sujeto.setter
    def sujeto(self,nSujeto):
        self.__sujeto = nSujeto
        
    @property
    def ejemplar(self):
        return self.__ejemplar
    
    @ejemplar.setter
    def ejemplar(self,nEjemplar):
        self.__ejemplar = nEjemplar
        
    @property
    def aptitud(self):
        return self.__aptitud
    
    @aptitud.setter
    def aptitud(self,nAptitud):
        self.__aptitud = nAptitud
        
    #Genera una asignación de verdad aleatoria para las variables del ejemplar
    def makeSujeto(self,pos,longit):
        for i in range(0,longit):
            if i == pos:
                self.sujeto.append(1)
            else:
                self.sujeto.append(random.randint(0,1))
    
    #Crea un sujeto inicial, y determina su aptitud
    def sujetoInicial(self,pos,longit):
        self.makeSujeto(pos,longit)
        self.aptitud = self.setAptitud()
    
    #Calcula la aptitud del individuo actual
    def setAptitud(self):
        cumplidas = 0
        for i in range(0,len(self.ejemplar)):
            clausula_actual = self.ejemplar[i]
            max_var_clausula = 0
            for j in range(0,len(clausula_actual)):
                if max_var_clausula >= 6:
                    break
                if clausula_actual[j] != -1:
                    if clausula_actual[j] == self.sujeto[j]:
                        cumplidas = cumplidas + 1
                        break
                    max_var_clausula = max_var_clausula + 1
        return cumplidas
    
    #Implelentación del operador de mutación Displacement Mutation
    def displacementMut(self):
        lista1 = self.sujeto
        puntoInicio = random.randint(1,len(lista1)-1)
        puntoFinal = random.randint(puntoInicio+1,len(lista1))

        corte = lista1[puntoInicio:puntoFinal+1]
        lugar = random.randint(0,len(lista1) - len(corte))
    
        inicio = lista1[0:lugar]
        final = lista1[lugar+len(corte) : len(lista1)]

        self.sujeto = inicio + corte + final
        
        self.aptitud = self.setAptitud()
        
    #Implementación del operador de mutación Exchange Mutation
    def exchangeMut(self):
        lista1 = self.sujeto
        puntoInicio = random.randint(1,len(lista1)-1)
        puntoFinal = random.randint(puntoInicio+1,len(lista1))

        corte = lista1[puntoInicio:puntoFinal+1]
        self.sujeto = lista1[0:puntoInicio] + corte[::-1] + lista1[puntoFinal+1:len(lista1)]
        
        self.aptitud = self.setAptitud()
    
    #Mutación del individuo
    def mutar(self):
        eleccion = random.random()
        if eleccion < 0.5:
            self.displacementMut()
        else:
            self.exchangeMut()
    
    #Representación en cadena del individuo
    def __str__(self):
        cadena = "Individuo: " + str(self.sujeto) + "\nAptitud: " + str(self.aptitud) + "\n"
        return cadena
