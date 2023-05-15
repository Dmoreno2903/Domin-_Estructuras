
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
        self._nombre = nombre if nombre else "Bot" #Los virtuales tienen nombres predefinidos
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
        a = len(self._fichas)
        return len(self._fichas)
    
    def getBot(self):
        return self._bot
    
    def tapicu(self, partida):
        fichas_dobles = list(filter(lambda x: x.getA() == x.getB(), self._fichas))
        A, B = partida.getPosibles()
        fichasIz = list(filter(lambda x: x.getA()  == A, fichas_dobles))
        fichasDe = list(filter(lambda x: x.getA() == B, fichas_dobles))
        if len(fichasIz) >=1 and len(fichasDe) >= 1:
            return [True, fichasIz, fichasDe]
        else: 
            return [False, fichasIz, fichasDe]
    
    def inteligenciaBot(self, partida): #Movimientos realizados por los bots
        tapicu = self.tapicu(partida) # [Bool, fichasIz, fichasDe]
        A, B = partida.getPosibles()

        if tapicu[0] == True: #Se puede
            fichaIz:Ficha = tapicu[1][0]; fichaDe:Ficha = tapicu[2][0]
            #Se agregan las dos fichas al tablero
            fichaIz.setDisponible(fichaIz.getA()); fichaDe.setDisponible(fichaDe.getA())
            partida.fichaIzquierda(fichaIz); partida.fichaDerecha(fichaDe) 
            #Se eliminan las dos fichas de las fichas del bot
            self._fichas.remove(fichaIz); self._fichas.remove(fichaDe)
            print("-- Tapicú --")

        else:
            #Fichas posibles a colocar por la izquierda
            posiblesIz = list(filter(lambda x: x.getA() == A or x.getB() == A, self._fichas)) 
            #Fichas posibles a colocar por la derecha
            posiblesDe = list(filter(lambda x: x.getA() == B or x.getB() == B, self._fichas))

            #Nos aseguramos que exista al menos una ficha
            if len(posiblesIz) != 0 or len(posiblesDe) != 0:
                if  len(posiblesIz) >= len(posiblesDe):
                    #Agregamos la ficha al lado izquierdo
                    ficha: Ficha = posiblesIz[0]
                    ficha.setDisponible(ficha.getB()) if ficha.getA() == A else ficha.setDisponible(ficha.getA())
                    partida.fichaIzquierda(ficha); self._fichas.remove(ficha)
                else: 
                    #Agregamos la ficha al lado derecho
                    ficha: Ficha = posiblesDe[0]
                    ficha.setDisponible(ficha.getA()) if ficha.getB() == B else ficha.setDisponible(ficha.getB())
                    partida.fichaDerecha(ficha); self._fichas.remove(ficha)
            else: print("-- Pasa de turno --")

    @classmethod
    def getPlayers(cls):
        return cls.all_players
    

