from Othello import Othello
t = Othello(8)
t.print_border()
t.print_board()


print()
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
t.insert_move(51, 'O')
