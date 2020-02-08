import random
    
class Ejemplar:
    def __init__(self):
        #Almacenamiento del ejemplar
        self.__ejemplar = []
        #Representación en cadena del ejemplar
        self.__cadena = ""
        #Njúmero de cláusulas del ejemplar
        self.__clausulas = 0
        #Número total de variables 
        self.__variables = 0
        self.makeEjemplar()
        
    @property
    def ejemplar(self):
        return self.__ejemplar
    
    @ejemplar.setter
    def ejemplar(self,newEjemplar):
        self.__ejemplar = newEjemplar
        
    @property
    def cadena(self):
        return self.__cadena
    
    @cadena.setter
    def cadena(self,newCadena):
        self.__cadena = newCadena
        
    @property
    def clausulas(self):
        return self.__clausulas
    
    @clausulas.setter
    def clausulas(self,nClausulas):
        self.__clausulas = nClausulas
    
    @property
    def variables(self):
        return self.__variables
    
    @variables.setter
    def variables(self,nVariables):
        self.__variables = nVariables
        
    #Genera un ejemplar aleatoriamente
    def makeEjemplar(self):
        self.variables = random.randint(100,10000)
        self.clausulas = random.randint(50,60)
        self.cadena = "Número de cláusulas: " + str(self.clausulas) + "\n"
        self.cadena = self.cadena + "Número de variables en total: " + str(self.variables) + "\nEjemplar: \n"
        self.cadena = self.cadena + "["
        for i in range(0,self.clausulas):
            tamano_clau = random.randint(3,5)
            clausula = []
            j = 0
            k = 0
            self.cadena = self.cadena + "["
            while j < self.variables and k < tamano_clau:
                var = random.randint(-1,1)
                clausula.append(var)
                if var >= 0:
                    k = k + 1
                    if var == 0:
                        self.cadena = self.cadena + "-x" + str(j)+ ","
                    else:
                        self.cadena = self.cadena + "x" + str(j)+ ","
                j = j + 1
            while j < self.variables:
                clausula.append(-1)
                j = j + 1
            self.cadena = self.cadena[:-1]
            self.cadena = self.cadena + "]\n"
            self.ejemplar.append(clausula)
        self.cadena = self.cadena[:-1]
        self.cadena = self.cadena + "]\n"
        return self.ejemplar
    
    def __str__(self):
        return self.cadena
