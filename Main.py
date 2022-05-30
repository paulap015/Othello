from Othello import Othello
from IA import IA
import copy
import random
t = Othello(8)
movHuman = 'O'  # Negro
movIa = 'X'  # Blanco
def testBoard():
    for i in range(1, 65):
        if(i == 28 or i == 37):
            print("|{:>3}|".format('X'), end=' ')
            continue
        if(i == 29 or i == 36):
            print("|{:>3}|".format('O'), end=' ')
            continue
        print("|{:>3}|".format(i), end=' ')
        if i % 8 == 0:
            print()


def human(mov):
    if(len(t.generate_possible_moves(mov, t.getBoard())) > 0):
        print("Movimientos posibles: ",  t.generate_possible_moves(mov, t.getBoard()))
        pos = int(input("Human: " + mov + " :"))
        while t.insert_move(pos, mov, False) == False:
            pos = int(input("Human: " + mov + " :"))
    else:
        print("Ups, No tienes movimientos")

def main():  
    ia = IA(t)
    t.print_board()
    while True:
        print()
        if t.fullBoard() == True:
            break
        human(movHuman)
        if t.fullBoard() == True:
            break
        ia.ia(movIa)
    # ¿Quién ganó?
    fichasIa = t.contarFichas(ficha=movIa)
    fichasHuman = t.contarFichas(ficha=movHuman)
    print("Ganó el jugador " + str(movHuman) + " con", str(fichasHuman) +
          " fichas") if fichasHuman > fichasIa else print("Ganó el jugador " + movIa + " con", str(fichasIa) + " fichas")
    print("Empate") if fichasHuman == fichasIa else print("")


if __name__ == '__main__':
    main()
