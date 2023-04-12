from Ficha import *
from Player import *
from Partida import *
from random import sample

def llenarFichas():
    """llena una a una las 28 fichas"""
    for i in range(7):
        for j in range(i,7):
            Ficha(i,j)

def repartirFichas(fichas,arr=[]):
    """reparte 7 fichas para cada jugador que viene en el array arr"""
    players = []
    for player in arr:
        fichas_selec = sample(fichas, 7)
        fichas = list(filter(lambda x: x not in fichas_selec,fichas))
        player.setFichas(fichas_selec)
        players.append(player)
    return players

def verificarSeis(arr,partida):
    for i in range(len(arr)):
        j=0
        fichas = arr[i].getFichas()
        for ficha in fichas:
            if ficha.getA()+ficha.getB() == 12:
                ficha.setDisponible(6)
                partida.fichaDerecha(fichas.pop(j))
                return i
            j+=1
            
def validarJugada(fichas,indice,lado,partida):
    ficha = fichas[indice]
    A, B = partida.getPosibles()
    caraA,caraB = ficha.getA(),ficha.getB()
    if (caraA == A or caraB == A) and lado.lower() == "i":
        ficha.setDisponible(caraA if caraB==A else caraB)
        partida.fichaIzquierda(fichas.pop(indice))
    elif (caraA == B or caraB == B) and lado.lower() == "d":
        ficha.setDisponible(caraA if caraB==B else caraB)
        partida.fichaDerecha(fichas.pop(indice))
    else:
        print("Jugada inválida. NO puedes colocar esa ficha")
        print("¡Pierdes turno!")
        print("-"*100)
        input("-- Presiona enter --")
        print("-"*100)

def jugada(player,turno,partida):
    if player.getBot():
        print(f"\n-- Turno de {player.getNombre()} --")
        player.inteligenciaBot(partida)
        tablero = partida.getTablero()
        partida.mostrarTablero(tablero)
        print(f'-- Fichas restantes: {player.contarFichas()} --\n')
        print("-"*100)
        input("-- Presiona enter --")
        print("-"*100)
    else:
        tablero = partida.getTablero()
        print("-"*100)
        print(f"\n-- Tu turno {player.getNombre()} --")
        partida.mostrarTablero(tablero)
        fichas = player.getFichas()
        cont = 1
        print("-- Tus fichas --\n")
        print(f"0. Pasar")
        for ficha in fichas:
            print(f"{cont}. [{ficha.getA()}|{ficha.getB()}]")
            cont+=1
        print("\n", "-"*100, sep="")
        indice= int(input("\n-> Selecione una ficha a jugar: "))-1
        print("\n", "-"*100, sep="")
        if indice<len(fichas) and indice>=0:
            print("-- Seleccione D para poner la ficha en el lado derecho del tablero --")
            print("-- seleccione I para poner la ficha en el lado izquierdo del tablero --")
            print("-"*100, "\n", sep="")
            lado= input("-> Seleccione lado: ")
            print("\n", "-"*100, sep="")
            validarJugada(fichas,indice,lado,partida)
        else:
            if indice == -1:
                print("¡Pasaste de turno!")
                print("-"*100)
                input("-- Presiona enter --")
                print("-"*100)
            else:
                print("Jugada inválida. ¡Pierdes turno!")
                print("-"*100)
                input("-- Presiona enter --")
                print("-"*100)


"""main: se lleva a cabo la partida"""
if __name__ == "__main__":
    llenarFichas()
    Player()
    Player()
    Player()
    Player(input("Ingrese su nombre: "),False)
    players = Player.getPlayers()
    fichas = Ficha.getFichas()
    partida = Partida(players,fichas)
    partida.repartirFichas()
    turno  = verificarSeis(players,partida)
    tablero = partida.getTablero()
    while True:
        turno=turno+1 if turno!=3 else 0
        jugada(players[turno],turno,partida)
        partida.comprobarGanador(players[turno])
        ganador = partida.getGanador()
        if(ganador):
            ganador = ganador.getNombre() if ganador.getNombre() else f"virtual {turno+1}"
            print(f"-- Gana el jugador: {ganador} --")
            break
    print("n-- JUEGO TERMINADO --")

        



    
    