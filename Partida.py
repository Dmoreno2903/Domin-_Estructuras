
from .Ficha import Ficha
from .Player import Player

#---------------------------------------
# Clase Partida
# Genera las 28 fichas de la partida
# Reparte a cada jugador un número de 7 fichas
#---------------------------------------

class Partida:

    def __init__(self, players, fichas):
        self._players = players #Array de jugadores
        self._fichas = fichas #Array de fichas
        self._tablero = []
        

    

    