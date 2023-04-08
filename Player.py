
#---------------------------------------
# Clase Jugador
# Contine sus fichas de juego y un nombre
#---------------------------------------

class Player:
    
    def __init__(self, fichas, nombre):
        self._fichas = fichas #Array con fichas
        self._nombre = nombre #Los virtuales tienen nombres predefinidos
        self._turno = False
        self._numero_fichas = 0

    def getFichas(self):
        return self._fichas
    
    def setFichas(self, fichas):
        self._fichas = fichas
        
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getTurno(self):
        return self._fichas
    
    def setTurno(self, turno):
        self._turno = turno

    def getNumero_Fichas(self):
        return len(self._fichas)
    

