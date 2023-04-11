
from random import sample
from Ficha import *
from Player import *
from collections import deque

#---------------------------------------
# Clase Partida
# Pide las 28 fichas de la partida
# Reparte a cada jugador un número de 7 fichas
#---------------------------------------

class Partida:

    def __init__(self, jugadores, fichas):
        self._players = jugadores #Array de jugadores
        self._fichas = fichas #Array de fichas
        self._tablero = deque([])
        self._ganador = None

    def repartirFichas(self):
        for player in self._players:
            fichas_selec = sample(self._fichas, 7)
            self._fichas = list(filter(lambda x: x not in fichas_selec, self._fichas))
            player.setFichas(fichas_selec)

    def comprobarGanador(self, player):
        if player.contarFichas() == 0:
            self._ganador = player

    def fichaDerecha(self, ficha):
        self._tablero.append(ficha)

    def fichaIzquierda(self, ficha):
        self._tablero.appendleft(ficha)

    def getPosibles(self):
        return self._tablero[0].getDisponible(), self._tablero[-1].getDisponible()
    
    def getFichas(self):
        return self._fichas
    
    def getTablero(self):
        return self._tablero
    
    def agregarFicha(self, ficha):
        self._tablero.append(ficha)




    


