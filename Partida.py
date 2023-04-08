
from random import sample
from .Ficha import Ficha
from .Player import Player

#---------------------------------------
# Clase Partida
# Pide las 28 fichas de la partida
# Reparte a cada jugador un número de 7 fichas
#---------------------------------------

class Partida:

    def __init__(self):
        self._players = Player.getPlayers() #Array de jugadores
        self._fichas = Ficha.getFichas() #Array de fichas
        self._tablero = []

    def repartirFichas(self):
        for player in self._players:
            fichas_selec = sample(self._fichas, 7)
            self._fichas = list(filter(lambda x: x not in fichas_selec, self._fichas))
            player.setFichas(fichas_selec)

    




    


