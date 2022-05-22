class Othello():
    def __init__(self, board_size):
        self.__board = {}
        self.__border = {}
        self.__board_size = board_size
        self.init_board()

    def init_board(self):
        for i in range(1, (self.__board_size*self.__board_size)+1):
            if(i == 28 or i == 37 or i == 45  or i==38 or i==39 or i==44):
                self.__board[i] = 'X'
                continue
            if(i == 29 or i == 36 or i == 21 or i == 13 or i==30 or i==46 or i==55):
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
        result=(self.validate_col(pos, move),self.validate_row(pos,move),self.validate_diag(pos,move))
        
        return any(result)


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
            while cont not in self.__border["Right"]:
                print(cont)
                if self.__board[cont] == move:
                    print("CONT ",cont)
                    
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
        
        return False


    def validate_diag(self, pos, move):
        
        isCorner=False
        isBorder=False

        flagLeftTop=False
        flagLeftLow=False
        flagRightTop=False
        flagRightLow=False
        #no esta en los bordes del tablero 
        if pos not in self.__border["Left"] and pos not in self.__border["Right"] and pos not in self.__border["Top"] and pos not in self.__border["Low"]:
            if(self.__board[pos-(self.__board_size+1)] == ' ' and self.__board[pos+(self.__board_size+1)] == ' ' or self.__board[pos-(self.__board_size+1)] == move or self.__board[pos+(self.__board_size+1)] == move):
                isBorder=False
            
                #return False
        else:
            
            
            #esta en algun borde del tablero
            isBorder=True
            #esta en los bordes y es una esquina
            #esquina superiot izquierda 
            if(pos in self.__border["Left"] and pos in self.__border["Top"]):
                isCorner=True
                if(self.__board[pos+(self.__board_size+1)] == ' ' or  self.__board[pos+(self.__board_size+1)] == move):
                    return False
                #diagonal derecha inferior
                cont = pos + (self.__board_size+1)
                while cont  not in self.__border["Left"] and cont <self.__board_size:
                    if self.__board[cont] == move:
                        flagRightLow = True
                        break
                    cont += (self.__board_size+1)

            elif(pos in self.__border["Left"] and pos in self.__border["Low"]):
                if(self.__board[pos-(self.__board_size-1)] == ' ' or  self.__board[pos-(self.__board_size-1)] == move):
                    return False
                isCorner=True
                #diagonal derecha superior
                cont = pos - (self.__board_size-1)
                while cont  not in self.__border["Left"] and cont >1:
                    if self.__board[cont] == move:
                        flagRightTop = True
                        break
                    cont -= (self.__board_size-1)
            elif(pos in self.__border["Right"] and pos in self.__border["Top"]):
                isCorner=True
                if(self.__board[pos+(self.__board_size-1)] == ' ' or  self.__board[pos+(self.__board_size-1)] == move):
                    return False
                #diagonal izquierda inferior
                cont = pos + (self.__board_size-1)
                while cont not in self.__border["Right"] and cont < (self.__board_size * self.__board_size) :
                    print("esquina inferior izquierda ",cont)
                    if self.__board[cont] == move:
                        
                        flagLeftLow = True
                        break
                    cont += (self.__board_size-1)
            elif(pos in self.__border["Right"] and pos in self.__border["Low"]):
                isCorner=True
                if(self.__board[pos-(self.__board_size+1)] == ' ' or  self.__board[pos-(self.__board_size+1)] == move):
                    return False
                # diagonal izquierda superior
                cont = pos - (self.__board_size+1)
                while cont not in self.__border["Right"] and cont >1 :
                    if self.__board[cont] == move:
                        
                        flagLeftTop = True
                        break
                    cont -= (self.__board_size+1)            
            
    
        # Buscar diagonalmente en 4 direcciones
        if isBorder == False:
            # diagonal izquierda superior
            cont = pos - (self.__board_size+1)
            while cont not in self.__border["Right"] and cont >1 :
                if self.__board[cont] == move:
                    
                    flagLeftTop = True
                    break
                cont -= (self.__board_size+1)
            #diagonal izquierda inferior
            cont = pos + (self.__board_size-1)
            while cont not in self.__border["Right"] and cont < (self.__board_size * self.__board_size) :
                print("esquina inferior izquierda ",cont)
                if self.__board[cont] == move:
                    
                    flagLeftLow = True
                    break
                cont += (self.__board_size-1)
            
            #diagonal derecha superior
            cont = pos - (self.__board_size-1)
            while cont  not in self.__border["Left"] and cont >1:
                if self.__board[cont] == move:
                    flagRightTop = True
                    break
                cont -= (self.__board_size-1)

            #diagonal derecha inferior
            cont = pos + (self.__board_size+1)
            while cont  not in self.__border["Left"] and cont <self.__board_size:
                if self.__board[cont] == move:
                    flagRightLow = True
                    break
                cont += (self.__board_size+1)
        
        ##pintar lascasillas
        bandera = False
        if flagLeftTop: 
            cont = pos - (self.__board_size+1)
            while cont >1:
                if self.__board[cont] == move:
                    break
                self.__board[cont] = move
                cont -=  (self.__board_size+1)
            #return True
        if flagLeftLow: 
            cont = pos + (self.__board_size-1)
            while self.__board[cont]  not in self.__border["Right"] or cont < self.__board_size*self.__board_size :              
                if self.__board[cont] == move:
                    break
                self.__board[cont] = move
                cont += (self.__board_size-1)
            #return True
        if flagRightTop: 
            cont = pos - (self.__board_size-1)
            while self.__board[cont]  not in self.__border["Left"] or cont >1:              
                if self.__board[cont] == move:
                    break
                self.__board[cont] = move
                cont -= (self.__board_size-1)
            #return True
        if flagRightLow: 
            cont = pos + (self.__board_size+1)
            while  self.__board[cont]  not in self.__border["Left"] or cont <self.__board_size:            
                if self.__board[cont] == move:
                    break
                self.__board[cont] = move
                cont += (self.__board_size+1)
            #return True
        result = (flagLeftLow,flagLeftTop,flagRightTop,flagRightLow)
        return any(result)
