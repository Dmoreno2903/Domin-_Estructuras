
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
        
    def getGanador(self):
        return self._ganador
    
    def mostrarTablero(self, fichas):
        arr_salida = []
        for ind in range(len(fichas)):
            if ind == (len(fichas) - 1): #Ultima ficha
                fichaA, fichaB = fichas[ind - 1], fichas[ind]
                if fichaB.getA() == fichaA.getA() or fichaB.getA() == fichaA.getB():
                    arr_salida.append("[" + str(fichaB.getA()) + "|" + str(fichaB.getB()) + "]")
                else:
                    arr_salida.append("[" + str(fichaB.getB()) + "|" + str(fichaB.getA()) + "]")
            else:
                fichaA, fichaB = fichas[ind], fichas[ind + 1]
                if fichaA.getA() == fichaB.getA() or fichaA.getA() == fichaB.getB():
                    arr_salida.append("[" + str(fichaA.getB()) + "|" + str(fichaA.getA()) + "]")
                else:
                    arr_salida.append("[" + str(fichaA.getA()) + "|" + str(fichaA.getB()) + "]")
        print("\n", "-"*(((len(arr_salida)*5)-3)//2), "TABLERO", "-"*(((len(arr_salida)*5)-3)//2), sep="")
        print("|", " "*((len(arr_salida)*5)+2), "|", sep="")
        print("|", "".join(arr_salida), "|")
        print("|", " "*((len(arr_salida)*5)+2), "|", sep="")
        print("-"*((len(arr_salida)*5)+4),"\n")


        



    


