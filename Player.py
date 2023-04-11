
from .Partida import Partida

#---------------------------------------
# Clase Jugador
# Contine sus fichas de juego y un nombre
#---------------------------------------

class Player:

    def __init__(self,nombre = None):
        self._fichas = [] #Array con fichas
        self._nombre = nombre if nombre else "" #Los virtuales tienen nombres predefinidos
        self._turno = False #Cambia a True si es su turno

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

    def contarFichas(self):
        return len(self._fichas)
    
    def inteligenciaBot(self, partida:Partida):
        A, B = partida.getPosibles()
        
    
    @classmethod
    def getPlayers(cls):
        return cls.getPlayers
    

