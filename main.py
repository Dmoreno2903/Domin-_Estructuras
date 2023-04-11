from Ficha import *
from Player import *
from random import sample, randrange

def llenarFichas():
    """llena una a una las 28 fichas"""
    fichas:Ficha = []
    for i in range(7):
        for j in range(i,7):
            fichas.append(Ficha(i,j))
    return fichas

def repartirFichas(fichas,arr=[]):
    """reparte 7 fichas para cada jugador que viene en el array arr"""
    players = []
    for player in arr:
        fichas_selec = sample(fichas, 7)
        fichas = list(filter(lambda x: x not in fichas_selec,fichas))
        player.setFichas(fichas_selec)
        players.append(player)
    return players

def verificarSeis(arr):
    for i in range(len(arr)):
        j=0
        for ficha in arr[i].getFichas():
            if ficha.getA()+ficha.getB() == 12:
                return i,arr[i].getFichas().pop(j)
            j+=1

def jugada(player,turno,fichasJugadas):
    cont =1
    fichas = player.getFichas()
    for ficha in fichas:
        print(f"ficha #{cont}: {ficha.getA()}:{ficha.getB()}")
        cont+=1
    
    numFicha = int(input("elija una ficha a jugar: ")) if turno==3 else randrange(len(fichas))
    fichasJugadas.append(fichas.pop(numFicha-1))


"""main: se lleva a cabo la partida"""
if __name__ == "__main__":
    fichasJugadas =[]
    fichas = llenarFichas()
    players = [Player(),Player(),Player(),Player(input("ingrese su nombre: "))]
    players = repartirFichas(fichas, players)
    ver = verificarSeis(players)
    turno=ver[0]
    fichasJugadas.append(ver[1])
    print(fichasJugadas)
    print(f"inicia el jugador: virtual {turno+1}" if turno!=3 
          else f"inicia el jugador:{players[turno].getNombre()}" )
    while True:
        turno=turno+1 if turno!=3 else 0
        print(f"turno para jugador: virtual {turno+1}" if turno!=3 
              else f"turno para jugador: {players[turno].getNombre()}")
        jugada(players[turno],turno,fichasJugadas)
        



    
    