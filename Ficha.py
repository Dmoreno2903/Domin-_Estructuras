
#---------------------------------------
# Clase Ficha
# Contine todas las 28 fichas almacenadas en un array
#---------------------------------------

class Ficha:
    all_fichas = []

    def __init__(self, cara_A, cara_B):
        self._disponible = None
        self._cara_A = cara_A # Primer lado 
        self._cara_B = cara_B # Segundo lado
        self.all_fichas.append(self) #Se almacena cada instancia en el array

    def getA(self):
        return self._cara_A
    
    def getB(self):
        return self._cara_B
    
    def setDisponible(self, disponible):
        self._disponible = disponible
    
    def getDisponible(self):
        return self._disponible
        
    @classmethod
    def getFichas(cls):
        return cls.all_fichas
    
