class Othello():
    def __init__(self, board_size):
        self.__board = {}
        self.__border = {}
        self.__board_size = board_size
        self.init_board()
    

    def getBoard(self):
        return self.__board

    def contarFichas(self,ficha):
        cont =0
        for pos in range (1, self.__board_size * self.__board_size +1):
            if self.__board[pos] == ficha:
                cont = cont +1
        return cont

    def fullBoard(self):
        for key in self.__board.keys():
            if self.__board[key] == ' ':
                return False
        return True

    def init_board(self):
        for i in range(1, (self.__board_size*self.__board_size)+1):
            if(i == 28 or i == 37 or i==2 or i==11 or i==20 or i==29 or i==21 or i==19 or i==21 or i==22 or i==23):
                self.__board[i] = 'X'
                continue
            if(i == 29 or i == 36 or i==19 or i==27 or i==28 or i==37 or i==46 or i==17):
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
            if(self.validate_rules(pos, move, False)):

                print()
                self.__board[pos] = move
                self.print_board()

            else:
                print("Movimiento inválido")
            print()
        else:
            print("Esta posición está ocupada")
            posicion = int(input("Digite otra posicion"))

    def validate_rules(self, pos, move, validate):
        result=(self.validate_col(pos, move,validate),self.validate_row(pos,move,validate),self.validate_diag(pos,move, validate))
        # print("Pos: Result:", pos, result)
        return any(result)


    def validate_col(self, pos, move, isValid):
        isTop = False
        isLow = False
        if pos not in self.__border["Top"] and pos not in self.__border["Low"]:
            if((self.__board[pos-self.__board_size] == ' ' and self.__board[pos+self.__board_size] == ' ') or (self.__board[pos-self.__board_size] == move and self.__board[pos+self.__board_size] == move) or (self.__board[pos-self.__board_size] == move and self.__board[pos+self.__board_size] == ' ') or(self.__board[pos-self.__board_size] == ' ' and self.__board[pos+self.__board_size] == move)):    
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
            cont = pos + self.__board_size
            if self.__board[cont] != move:
                while cont < (self.__board_size * self.__board_size) and self.__board[cont] != ' ':
                    if self.__board[cont] == move:
                        flagLow = True
                        break
                    cont += self.__board_size
        # Buscar hacia arriba
        if isTop == False:
            cont = pos - self.__board_size
            if self.__board[cont] != move:
                while cont >= 1 and self.__board[cont] != ' ':
                    if self.__board[cont] == move:
                        flagTop = True
                        break
                    cont -= self.__board_size
        if isValid == False:
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
        if isValid:
            if flagTop or flagLow:
                return True
        return False

    def validate_row(self, pos, move, isValid):

        isRight = False
        isLeft = False

        if pos not in self.__border["Left"] and pos not in self.__border["Right"]:
            if((self.__board[pos-1] == ' ' and self.__board[pos+1] == ' ') or (self.__board[pos-1] == move and self.__board[pos+1] == move)) or (self.__board[pos-1] == move and self.__board[pos+1] == ' ') or (self.__board[pos-1] == ' ' and self.__board[pos+1] == move):
                return False
        else:
            if pos in self.__border["Left"]:
                isLeft = True
                if(self.__board[pos+1] == ' ' or self.__board[pos+1] == move):
                    return False
            elif pos in self.__border["Right"]:
                isRight = True
                if(self.__board[pos-1] == ' ' or self.__board[pos-1] == move):
                    return False

        flagLeft = False
        flagRight = False

        # Buscar hacia la derecha
        if isRight == False:
            cont = pos + 1
            if self.__board[cont] != move:
                while cont not in self.__border["Left"] and cont < 65 and self.__board[cont] != ' ':
                    if self.__board[cont] == move:
                        flagRight = True
                        break
                    cont += 1
        # Buscar hacia la izquierda
        if isLeft == False:
            cont = pos - 1
            if self.__board[cont] != move:
                while cont not in self.__border["Right"] and cont>0 and self.__board[cont] != ' ' :
                    #print("CONT POS", cont," " ,pos ," mov : ", move)
                    if self.__board[cont] == move:
                        flagLeft = True
                        break
                    cont -= 1
        # pintar lascasillas
        if isValid == False:
            if flagRight:
                cont = pos + 1
                while cont not in self.__border["Left"]:
                    if self.__board[cont] == move:
                        break
                    self.__board[cont] = move
                    cont += 1
                return True
            if flagLeft:
                cont = pos - 1
                while cont not in self.__border["Right"]:
                    if self.__board[cont] == move:
                        break
                    self.__board[cont] = move
                    cont -= 1
                return True
        if isValid:
            if flagLeft or flagRight:
                return True
        return False

    

    def validate_diag(self, pos, move, isValid):
        
        isCorner=False
        isBorder=False

        flagLeftTop=False
        flagLeftLow=False
        flagRightTop=False
        flagRightLow=False
        
        #no esta en los bordes del tablero 
        if pos not in self.__border["Left"] and pos not in self.__border["Right"] and pos not in self.__border["Top"] and pos not in self.__border["Low"]:
            
            firstDiag = (self.__board[pos-(self.__board_size+1)] == ' ' , self.__board[pos+(self.__board_size+1)] == ' ')
            secondDiag = (self.__board[pos+(self.__board_size-1)] == ' ' , self.__board[pos-(self.__board_size-1)] == ' ')
            posicionesVacias=(self.__board[pos-(self.__board_size+1)] == ' ' , self.__board[pos+(self.__board_size+1)] == ' ' , self.__board[pos+(self.__board_size-1)] == ' ' , self.__board[pos-(self.__board_size-1)] == ' ')

            movFirstDiag=True
            movSecondDiag=True
            # print("psiciones vacias ",posicionesVacias.count(True))
            # print("diag 1 ", self.__board[pos-(self.__board_size+1)], "  ",self.__board[pos+(self.__board_size+1)])
            # print("diag 2 ", self.__board[pos+(self.__board_size-1)], "  ",self.__board[pos-(self.__board_size-1)])
            
            if (posicionesVacias.count(True)==4):
                #return false de una 4 posiciones vacias 
                
                return False
                
            if( (self.__board[pos-(self.__board_size+1)]==move and (firstDiag[1]==True or self.__board[pos+(self.__board_size+1)]==move)) or
                (self.__board[pos+(self.__board_size+1)]==move and (firstDiag[0]==True or self.__board[pos-(self.__board_size+1)] ==move))
                ):


                movFirstDiag=False
                #si en la esquina superior izquierda(primera diagonal, primera posicion) es igual a mi  y en la segunda pos de la primera diagonal es vacio o soy yo  
                #no se puede mover en esa diagonal 

            
            if( (self.__board[pos+(self.__board_size-1)]==move and (secondDiag[1]==True or self.__board[pos-(self.__board_size-1)]==move)) or
                (self.__board[pos-(self.__board_size-1)]==move and (secondDiag[0]==True or self.__board[pos+(self.__board_size-1)]==move))
                ):
                
                
                movSecondDiag=False

            # print("movFisrst ->", movFirstDiag)
            # print("movSecond ->",movSecondDiag)
            if movFirstDiag ==False and movSecondDiag==False:
                return False
            
            if movFirstDiag ==True and movSecondDiag==False:
                if (self.puedeConvertir(pos,move,"first") ==False):

                    return False
            if movFirstDiag ==False and movSecondDiag==True:
                if self.puedeConvertir(pos,move,"second")==False:
                    return False
                    
            
            isBorder=False
        else:
            
            
            #esta en algun borde del tablero
            isBorder=True
            #esta en los bordes y es una esquina
            #esquina superiot izquierda 
            if(pos in self.__border["Left"] and pos in self.__border["Top"]):
                
                isCorner=True
                #verificar diagonal inferior derecha
                if(self.__board[pos+(self.__board_size+1)] == ' ' or  self.__board[pos+(self.__board_size+1)] == move):
                    return False
                #diagonal derecha inferior
                cont = pos + (self.__board_size+1)
                if self.__board[cont] != move:
                    while cont  not in self.__border["Left"] and cont < self.__board_size *self.__board_size and self.__board[cont] != ' ':
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
                if self.__board[cont] != move:
                    while cont  not in self.__border["Left"] and cont >1 and self.__board[cont] != ' ':
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
                if self.__board[cont] != move:
                    while cont not in self.__border["Right"] and cont < (self.__board_size * self.__board_size) and self.__board[cont] != ' ':
                        
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
                if self.__board[cont] != move:
                    while cont not in self.__border["Right"] and cont >1 and self.__board[cont] != ' ' :
                        if self.__board[cont] == move:
                            
                            flagLeftTop = True
                            break
                        cont -= (self.__board_size+1)            
            
    
        # Buscar diagonalmente en 4 direcciones
        if isBorder == False:
            
            # diagonal izquierda superior
            cont = pos - (self.__board_size+1)
            if self.__board[cont] != move:
                while cont not in self.__border["Right"] and cont >1 and self.__board[cont] != ' ':
                    if self.__board[cont] == move:
                        
                        flagLeftTop = True
                        break
                    cont -= (self.__board_size+1)
            #diagonal izquierda inferior
            cont = pos + (self.__board_size-1)
            if self.__board[cont] != move:
                while cont not in self.__border["Right"] and cont < (self.__board_size * self.__board_size) and self.__board[cont] != ' ':
            
                    if self.__board[cont] == move:
                        
                        flagLeftLow = True
                        break
                    cont += (self.__board_size-1)
            
            #diagonal derecha superior
            cont = pos - (self.__board_size-1)
            if self.__board[cont] != move:
                while cont  not in self.__border["Left"] and cont >1 and self.__board[cont] != ' ':
            
                    if self.__board[cont] == move:
                        flagRightTop = True
                        break
                    cont -= (self.__board_size-1)

            #diagonal derecha inferior
            cont = pos + (self.__board_size+1)
            if self.__board[cont] != move:
                while cont  not in self.__border["Left"] and cont <self.__board_size * self.__board_size and self.__board[cont] != ' ':
            
                    if self.__board[cont] == move:
                        flagRightLow = True
                        break
                    cont += (self.__board_size+1)
        else: 
            verOne=True
            verTwo=True
            #es borde pero no es esquina 
            if (pos in self.__border["Left"] and (pos not in self.__border["Top"] and pos not in self.__border["Low"])): #es borde izquierdo debe buscar derSuperior derInfe
                
                #diagonal derecha superior
                if(self.__board[pos-(self.__board_size-1)] == ' ' or  self.__board[pos-(self.__board_size-1)] == move):
                    verOne=False
                #verificar diagonal inferior derecha
                if(self.__board[pos+(self.__board_size+1)] == ' ' or  self.__board[pos+(self.__board_size+1)] == move):
                    verTwo =False
                
                if verTwo ==True:
                    #diagonal derecha inferior
                    cont = pos + (self.__board_size+1)
                    if self.__board[cont] != move:
                        while cont  not in self.__border["Left"] and cont <self.__board_size * self.__board_size and self.__board[cont] != ' ':
            
                            if self.__board[cont] == move:
                                flagRightLow = True
                                break
                            cont += (self.__board_size+1)

                if verOne ==True:
                    #diagonal derecha superior
                    cont = pos - (self.__board_size-1)
                    if self.__board[cont] != move:
                        while cont  not in self.__border["Left"] and cont >1 and self.__board[cont] != ' ':
            
                            if self.__board[cont] == move:
                                flagRightTop = True
                                break
                            cont -= (self.__board_size-1)

            elif(pos in self.__border["Right"] and (pos not in self.__border["Top"] and pos not in self.__border["Low"])):

                verOne=True
                verTwo=True

                #diagonal izquierda superior 
                if(self.__board[pos-(self.__board_size+1)] == ' ' or  self.__board[pos-(self.__board_size+1)] == move):
                    verOne=False
                #diagonal izquierda inferior
                if(self.__board[pos+(self.__board_size-1)] == ' ' or  self.__board[pos+(self.__board_size-1)] == move):
                    verTwo =False

                if verOne ==True:
                    # diagonal izquierda superior
                    cont = pos - (self.__board_size+1)
                    if self.__board[cont] != move:
                        while cont not in self.__border["Right"] and cont >1 and self.__board[cont] != ' ' :
    
                            if self.__board[cont] == move:
                                
                                flagLeftTop = True
                                break
                            cont -= (self.__board_size+1)
                if verTwo ==True:
                    #diagonal izquierda inferior
                    cont = pos + (self.__board_size-1)
                    if self.__board[cont] != move:
                        while cont not in self.__border["Right"] and cont < (self.__board_size * self.__board_size) and self.__board[cont] != ' ':
                
                            if self.__board[cont] == move:
                                
                                flagLeftLow = True
                                break
                            cont += (self.__board_size-1)

            elif(pos in self.__border["Top"] and (pos not in self.__border["Right"]  and pos not in self.__border["Left"])):
                verOne=True
                verTwo=True

                #verificar diagonal inferior derecha
                if(self.__board[pos+(self.__board_size+1)] == ' ' or  self.__board[pos+(self.__board_size+1)] == move):
                    verOne =False
                #diagonal izquierda inferior
                if(self.__board[pos+(self.__board_size-1)] == ' ' or  self.__board[pos+(self.__board_size-1)] == move):
                    verTwo =False

                if verTwo ==True:
                #diagonal izquierda inferior
                    cont = pos + (self.__board_size-1)
                    if self.__board[cont] != move:
                        while cont not in self.__border["Right"] and cont < (self.__board_size * self.__board_size) and self.__board[cont] != ' ':
                
                            if self.__board[cont] == move:
                                
                                flagLeftLow = True
                                break
                            cont += (self.__board_size-1)

                if verOne==True:
                    #diagonal derecha inferior
                    cont = pos + (self.__board_size+1)
                    if self.__board[cont] != move:
                        while cont  not in self.__border["Left"] and cont <self.__board_size * self.__board_size and self.__board[cont] != ' ':
            
                            if self.__board[cont] == move:
                                flagRightLow = True
                                break
                            cont += (self.__board_size+1)

            elif(pos in self.__border["Low"] and (pos not in self.__border["Right"] and pos not in self.__border["Left"])):
                verOne=True
                verTwo=True

                #diagonal izquierda superior 
                if(self.__board[pos-(self.__board_size+1)] == ' ' or  self.__board[pos-(self.__board_size+1)] == move):
                    verOne=False
                #diagonal derecha superior
                if(self.__board[pos-(self.__board_size-1)] == ' ' or  self.__board[pos-(self.__board_size-1)] == move):
                    verTwo=False

                if verOne==True:
                    # diagonal izquierda superior
                    cont = pos - (self.__board_size+1)
                    if self.__board[cont] != move:
                        while cont not in self.__border["Right"] and cont >1 and self.__board[cont] != ' ':
            
                            if self.__board[cont] == move:
                                
                                flagLeftTop = True
                                break
                            cont -= (self.__board_size+1)
                if verTwo==True:
                    #diagonal derecha superior
                    cont = pos - (self.__board_size-1)
                    if self.__board[cont] != move:
                        while cont  not in self.__border["Left"] and cont >1 and self.__board[cont] != ' ':

                            if self.__board[cont] == move:
                                flagRightTop = True
                                break
                            cont -= (self.__board_size-1)
                
        ##pintar lascasillas
        bandera = False
        if isValid == False:
            if flagLeftTop: 
                cont = pos - (self.__board_size+1)
                if( self.__board[cont]!=' '):
                    while cont >1:
                        if self.__board[cont] == move:
                            break
                        self.__board[cont] = move
                        cont -=  (self.__board_size+1)
                #return True
            if flagLeftLow: 
                cont = pos + (self.__board_size-1)
                if( self.__board[cont]!=' '):
                    while self.__board[cont]  not in self.__border["Right"] or cont < self.__board_size*self.__board_size :              
                        if self.__board[cont] == move:
                            break
                        self.__board[cont] = move
                        cont += (self.__board_size-1)
                #return True
            if flagRightTop: 
                cont = pos - (self.__board_size-1)
                if( self.__board[cont]!=' '):
                    while self.__board[cont]  not in self.__border["Left"] or cont >1:              
                        if self.__board[cont] == move:
                            break
                        self.__board[cont] = move
                        cont -= (self.__board_size-1)
                #return True
            if flagRightLow: 
                cont = pos + (self.__board_size+1)
                if( self.__board[cont]!=' '):
                    while  self.__board[cont]  not in self.__border["Left"] or cont <self.__board_size:            
                        if self.__board[cont] == move:
                            break
                        self.__board[cont] = move
                        cont += (self.__board_size+1)
                #return True
            result = (flagLeftLow,flagLeftTop,flagRightTop,flagRightLow)
            return any(result)
        if isValid:
            if flagLeftLow or flagLeftTop or flagRightTop or flagRightLow:
                return True
        return False
    

    def puedeConvertir(self,pos,move,diagonal):
        #verificar si una que no es borde puede capturar
        
        
        #puede capturar en la primera diagonal 
        if (diagonal == "first"):
            # diagonal izquierda superior
                cont = pos - (self.__board_size+1)
                if( self.__board[cont]!=' '):
                    while cont not in self.__border["Right"] and cont >1 :
                        
                        if self.__board[cont] == move:
                            return True
                        cont -= (self.__board_size+1)

            #diagonal derecha inferior
                cont = pos + (self.__board_size+1)
                if( self.__board[cont]!=' '):
                    while cont  not in self.__border["Left"] and cont <self.__board_size * self.__board_size:
                        
                        if self.__board[cont] == move:
                            return True
                        cont += (self.__board_size+1)

        elif( diagonal =="second"):
            #diagonal izquierda inferior
            cont = pos + (self.__board_size-1)
            if( self.__board[cont]!=' '):
                while cont not in self.__border["Right"] and cont < (self.__board_size * self.__board_size) :
                    
                    if self.__board[cont] == move:
                        return True
                    cont += (self.__board_size-1)
            
            #diagonal derecha superior
            cont = pos - (self.__board_size-1)
            if( self.__board[cont]!=' '):
                while cont  not in self.__border["Left"] and cont >1:
                    
                    if self.__board[cont] == move:
                        return True
                    cont -= (self.__board_size-1)

        return False
