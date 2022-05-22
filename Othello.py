class Othello():
    def __init__(self, board_size):
        self.__board = {}
        self.__border = {}
        self.__board_size = board_size
        self.init_board()

    def init_board(self):
        for i in range(1, (self.__board_size*self.__board_size)+1):
            if(i == 28 or i == 37 or i == 45  or i==38 or i==39):
                self.__board[i] = 'X'
                continue
            if(i == 29 or i == 36 or i == 21 or i == 13):
                self.__board[i] = 'O'
                continue
            self.__board[i] = ' '
        # Add Border
        # Top
        top = []
        for i in range(1, self.__board_size + 1):
            top.append(i)
        self.__border["Top"] = top
        # Left
        left = [1]
        sum = 1
        for i in range(1, self.__board_size + 1):
            sum += self.__board_size
            left.append(sum)
            if sum + self.__board_size-1 == self.__board_size*self.__board_size:
                break
        self.__border["Left"] = left

        # Low
        low = [self.__board_size*self.__board_size - (self.__board_size-1)]
        sum = self.__board_size*self.__board_size - (self.__board_size-1)
        for i in range(1, self.__board_size+1):
            sum += 1
            low.append(sum)
            if sum == self.__board_size*self.__board_size:
                break
        self.__border["Low"] = low

        # Right
        right = [self.__board_size]
        sum = self.__board_size
        for i in range(self.__board_size + 1):
            sum += self.__board_size
            right.append(sum)
            if sum == self.__board_size*self.__board_size:
                break
        self.__border["Right"] = right

    def print_board(self):
        for key in self.__board.keys():
            print('|', self.__board[key], end=" | ")
            if(key % self.__board_size == 0):
                print()

    def print_border(self):
        print(self.__border)

    def space_is_free(self, pos):
        if(self.__board[pos] == ' '):
            return True
        return False

    def insert_move(self, pos, move):

        if(self.__board[pos] == ' '):
            if(self.validate_rules(pos, move)):
                print()
                self.__board[pos] = move
                self.print_board()

            else:
                print("Movimiento inválido")
            print()
        else:
            print("Esta posición está ocupada")
            posicion = int(input("Digite otra posicion"))

    def validate_rules(self, pos, move):
        #return self.validate_col(pos, move)
        return self.validate_row(pos,move)

    def validate_col(self, pos, move):
        isTop = False
        isLow = False
        if pos not in self.__border["Top"] and pos not in self.__border["Low"]:
            if(self.__board[pos-self.__board_size] == ' ' and self.__board[pos+self.__board_size] == ' ' or self.__board[pos-self.__board_size] == move or self.__board[pos+self.__board_size] == move):
                return False
        else:
            if pos in self.__border["Top"]:
                isTop = True
                if(self.__board[pos+self.__board_size] == ' ' or self.__board[pos+self.__board_size] == move):
                    return False
            else:
                isLow = True
                if(self.__board[pos-self.__board_size] == ' ' or self.__board[pos-self.__board_size] == move):
                    return False
        # Si la posición está en los límites
        flagTop = False
        flagLow = False
        # Buscar hacia abajo
        if isLow == False:
            print("1ro")
            cont = pos + self.__board_size
            while cont < (self.__board_size * self.__board_size):
                if self.__board[cont] == move:
                    flagLow = True
                    break
                cont += self.__board_size
        # Buscar hacia arriba
        if isTop == False:
            cont = pos - self.__board_size
            while cont >= 1:
                if self.__board[cont] == move:
                    flagTop = True
                    break
                cont -= self.__board_size

        if flagLow: 
            cont = pos + self.__board_size
            while cont < (self.__board_size * self.__board_size):
                if self.__board[cont] == move:
                    break
                self.__board[cont] = move
                cont += self.__board_size
            return True
        if flagTop: 
            cont = pos - self.__board_size
            while cont >= 1:               
                if self.__board[cont] == move:
                    break
                self.__board[cont] = move
                cont -= self.__board_size
            return True
        return False

    def validate_row(self, pos, move):
        print("entra al metodo")
        isRight = False
        isLeft = False
        
        if pos not in self.__border["Left"] and pos not in self.__border["Right"]:
            if(self.__board[pos-1] == ' ' and self.__board[pos+1] == ' ' or self.__board[pos-1] == move or self.__board[pos+1] == move):
                return False
        else:
            if pos in self.__border["Left"]:
                isLeft = True
                if(self.__board[pos+1] == ' ' or self.__board[pos+1] == move):
                    return False
            else:
                isRight = True
                if(self.__board[pos-1] == ' ' or self.__board[pos-1] == move):
                    return False
       
        flagLeft=False
        flagRight=False
        
        # Buscar hacia la derecha
        if isRight == False:
            
            cont = pos + 1
            while cont < (pos + self.__board_size ):
                if self.__board[cont] == move:
                    flagLeft = True
                    break
                cont += 1
        # Buscar hacia la izquierda
        if isLeft == False:
            cont = pos - 1
            while cont > (pos -self.__board_size):
                if self.__board[cont] == move:
                    flagRight = True
                    break
                cont -= 1
        
        ##pintar lascasillas
        if flagLeft: 
            cont = pos + 1
            while cont < (pos + self.__board_size):
                if self.__board[cont] == move:
                    break
                self.__board[cont] = move
                cont += 1
            return True
        if flagRight: 
            cont = pos - 1
            while cont > (pos - self.__board_size):               
                if self.__board[cont] == move:
                    break
                self.__board[cont] = move
                cont -= 1
            return True
        print("llega al final")
        return False


    def validate_diag(self, pos, move):
        if(self.__board[pos-(self.__board_size+1)] == ' ' and self.__board[pos+(self.__board_size+1)]):
            return False
        return True
