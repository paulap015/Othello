from Othello import Othello
t = Othello(8)
t.print_border()

print()
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
# t.print_border()
testBoard()

def ia(mov):
    pos = int(input("POS IA "+mov + " :"))
    t.insert_move(pos, mov)


def human(mov):
    pos = int(input("POS Human " +mov + " :"))
    t.insert_move(pos, mov)


movHuman = 'O' #Negro
movIa = 'X' #Blanco
while t.fullBoard() == False:
    human(movHuman)
    ia(movIa)
    testBoard()
