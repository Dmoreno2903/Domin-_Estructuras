
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
        fichas_posibles = list(filter(lambda x: x.getA() == A or x.getA() == B, fichas_dobles))
        if len(fichas_posibles) >= 2: return True
        else: return False
    
    def inteligenciaBot(self, partida):
        bool_tapicu = self.tapicu(partida)
        if bool_tapicu == False:
            A, B = partida.getPosibles()
            posA = list(filter(lambda x: x.getA() == A or x.getB() == A, self._fichas))
            posB = list(filter(lambda x: x.getA() == B or x.getB() == B, self._fichas))
            if len(posA) != 0 or len(posB) != 0:
                if len(posA) >= len(posB): 
                    ficha:Ficha = posA[-1]
                    ficha.setDisponible(ficha.getB()) if ficha.getA() == A else ficha.setDisponible(ficha.getA())
                    partida.fichaIzquierda(ficha); self._fichas.remove(ficha)
                else:
                    ficha:Ficha = posB[-1]
                    ficha.setDisponible(ficha.getA()) if ficha.getB() == B else ficha.setDisponible(ficha.getB())
                    partida.fichaDerecha(ficha); self._fichas.remove(ficha)
            else:
                print("-- Pasa de turno --")
        else:
            A, B = partida.getPosibles()
            fichas_dobles = list(filter(lambda x: x.getA() == x.getB(), self._fichas))
            fichasIz = list(filter(lambda x: x.getA()  == A, fichas_dobles))
            fichasDe = list(filter(lambda x: x.getA() == B, fichas_dobles))
            if len(fichasIz) == 1 and len(fichasDe) == 1:
                fichaIz = fichasIz[0]
                fichasDer = fichasDe[0]
                partida.fichaIzquierda(fichaIz), self._fichas.remove(fichaIz)
                partida.fichaDerecha(fichasDer), self._fichas.remove(fichasDer)
                print("-- Tapicú --")
            else:
                A, B = partida.getPosibles()
                posA = list(filter(lambda x: x.getA() == A or x.getB() == A, self._fichas))
                posB = list(filter(lambda x: x.getA() == B or x.getB() == B, self._fichas))
                if len(posA) != 0 or len(posB) != 0:
                    if len(posA) >= len(posB): 
                        ficha:Ficha = posA[-1]
                        ficha.setDisponible(ficha.getB()) if ficha.getA() == A else ficha.setDisponible(ficha.getA())
                        partida.fichaIzquierda(ficha); self._fichas.remove(ficha)
                    else:
                        ficha:Ficha = posB[-1]
                        ficha.setDisponible(ficha.getA()) if ficha.getB() == B else ficha.setDisponible(ficha.getB())
                        partida.fichaDerecha(ficha); self._fichas.remove(ficha)
                else:
                    print("-- Pasa de turno --")

    @classmethod
    def getPlayers(cls):
        return cls.all_players
    

