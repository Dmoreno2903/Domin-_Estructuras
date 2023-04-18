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

def tapicu(fichas, partida,indice_1, indice_2):
    for ficha in fichas:
        fichas_dobles = list(filter(lambda x: x.getA() == x.getB(), fichas))
        A, B = partida.getPosibles()
        fichas_posibles = list(filter(lambda x: x.getA() == A or x.getA() == B, fichas_dobles))
    if len(fichas_posibles) >= 2:
        for i in range(0, len(fichas_posibles)):
            if fichas[indice_1]== fichas_posibles[i]:
                for j in range(0, len(fichas_posibles)):
                    if fichas[indice_2]== fichas_posibles[j]:
                        A, B = partida.getPosibles()
                        fichas_dobles = list(filter(lambda x: x.getA() == x.getB(), fichas))
                        fichasIz = list(filter(lambda x: x.getA()  == A, fichas_dobles))
                        fichasDe = list(filter(lambda x: x.getA() == B, fichas_dobles))
                        if len(fichasIz) == 1 and len(fichasDe) == 1:
                            fichaIz = fichasIz[0]
                            fichasDer = fichasDe[0]
                            partida.fichaIzquierda(fichaIz), fichas.remove(fichaIz)
                            partida.fichaDerecha(fichasDer), fichas.remove(fichasDer)
                            print("-- Tapicú --")
    else:
        print("-"*100)
        print("Jugada inválida, pierdes turno")
        print("-"*100)

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
        print(f"{cont}. Tapicu")    
        print("\n", "-"*100, sep="")
        indice= int(input("\n-> Selecione una ficha a jugar: "))-1
        print("\n", "-"*100, sep="")
        if indice<len(fichas) and indice>=0:
            print("-- Seleccione D para poner la ficha en el lado derecho del tablero --")
            print("-- Seleccione I para poner la ficha en el lado izquierdo del tablero --")
            print("-"*100, "\n", sep="")
            lado= input("-> Seleccione lado: ")
            print("\n", "-"*100, sep="")
            validarJugada(fichas, indice, lado, partida)
        elif indice == len(fichas):
            print("\n", "-"*100, sep="")
            indice_1= int(input("\n-> Seleciona la ficha 1: "))-1
            print("\n", "-"*100, sep="")
            if indice_1<len(fichas) and indice_1>=0:
                print("-- Seleccione D para poner la ficha en el lado derecho del tablero --")
                print("-- Seleccione I para poner la ficha en el lado izquierdo del tablero --")
                print("-"*100, "\n", sep="")
                lado= input("-> Seleccione lado: ")
                print("\n", "-"*100, sep="")
            print("\n", "-"*100, sep="")
            indice_2= int(input("\n-> Seleciona la ficha 2: "))-1
            print("\n", "-"*100, sep="")
            if indice_2<len(fichas) and indice_2>=0:
                print("-- Seleccione D para poner la ficha en el lado derecho del tablero --")
                print("-- Seleccione I para poner la ficha en el lado izquierdo del tablero --")
                print("-"*100, "\n", sep="")
                lado= input("-> Seleccione lado: ")
                print("\n", "-"*100, sep="")

                tapicu(fichas, partida,indice_1, indice_2)
                
    
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
    Player("Bot 1", True)
    Player("Bot 2", True)
    Player("Bot 3", True)
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
            print(f"\n-- Gana el jugador: {ganador} --")
            break
    print("\n-- JUEGO TERMINADO --")

        



    
    