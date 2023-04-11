
from Partida import *
from Ficha import *

#---------------------------------------
# Clase Jugador
# Contine sus fichas de juego y un nombre
#---------------------------------------

class Player:
    all_players = []

    def __init__(self,nombre = None, bot = True):
        self._fichas = [] #Array con fichas
        self._nombre = nombre if nombre else "" #Los virtuales tienen nombres predefinidos
        self._turno = False #Cambia a True si es su turno
        self.all_players.append(self) #Se agrega cada jugador creado
        self._bot = bot

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
    
    def getBot(self):
        return self._bot
    
    def inteligenciaBot(self, partida):
        A, B = partida.getPosibles()
        posA = list(filter(lambda x: x.getA() == A or x.getB() == A, self._fichas))
        posB = list(filter(lambda x: x.getA() == B or x.getB() == B, self._fichas))
        if len(posA) != 0 or len(posB) != 0:
            if len(posA) >= len(posB): 
                ficha = posA[-1]
                ficha.setDisponible(ficha.getB()) if ficha.getA() == A else ficha.setDisponible(ficha.getA())
                partida.fichaIzquierda(ficha), self._fichas.remove(ficha)
            else:
                ficha:Ficha = posB[-1]
                ficha.setDisponible(ficha.getA()) if ficha.getB() == B else ficha.setDisponible(ficha.getB())
                partida.fichaDerecha(ficha); self._fichas.remove(ficha)
        else:
            
    
    @classmethod
    def getPlayers(cls):
        return cls.all_players
    

