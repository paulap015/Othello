class IA:

    def __init__(self, t):
        self.__t = t
        self.movIa = 'X'
        self.movHuman = 'O'

    SQUARE_WEIGHTS = {
        1: 120, 2: -20,  3: 20,   4: 5,  5: 5,  6: 20, 7: -20, 8: 120,
        9: -20, 10: -40, 11: -5,  12: -5, 13: -5,  14: -5, 15: -40, 16: -20,
        17: 20,  18: -5,  19: 15,   20: 3,   21: 3,  22: 15,  23: -5,  24: 20,
        25: 5, 26: -5,  27: 3,   28: 3,   29: 3,  30: 3,  31: -5,   32: 5,
        33: 5,  34: -5,   35: 3,  36: 3,   37: 3,   38: 3,  39: -5,   40: 5,
        41: 20,  42: -5,  43: 15,   44: 3,   45: 3,  46: 15,  47: -5,  48: 20,
        49: -20, 50: -40,  51: -5,  52: -5,  53: -5,  54: -5, 55: -40, 56: -20,
        57: 120, 58: -20,  59: 20,   60: 5,   61: 5,  62: 20, 63: -20, 64: 120
    }

    def move_ia(self, move):
        max_score = -1000
        best_move = 0
        for key in self.__t.getBoard().keys():
            if self.__t.getBoard()[key] == ' ' and self.__t.validate_rules(key, move, True):
                board_copy = self.__t.getBoard().copy()
                self.__t.insert_move(key, move, True)
                score = self.minmax_alpa_betha(key, -100, 100, self.__t.getBoard(), 3, False)
                self.__t.setBoard(board_copy)
                if score > max_score:
                    max_score = score
                    best_move = key
        return best_move

    def ia(self, mov):
        pos = self.move_ia(mov)
        
        if pos != 0:
            print("IA: " + str(pos))
            self.__t.insert_move(pos, mov, False)
        else:
            print("IA Sin Movimientos...")

    def heuristic_function(self, position, board):
        #return self.SQUARE_WEIGHTS[position]
        return self.__t.contarFichas(self.movIa) - self.__t.contarFichas(self.movHuman)

    def minmax_alpa_betha(self, position, alpha, beta, board, depth, isMax):
        if self.__t.fullBoard() or depth == 0:
            return self.heuristic_function(position, board)
        if isMax:
            max_eval = -100
            for key in board.keys():
                if board[key] == ' ' and self.__t.validate_rules(key, self.movIa, True):
                    copy_board = board.copy()
                    self.__t.insert_move(key, self.movIa, True)
                    score = self.minmax_alpa_betha(key, alpha, beta, board, depth-1, False)
                    max_eval = max(max_eval, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        self.__t.setBoard(copy_board)
                        break
                    self.__t.setBoard(copy_board)
            return max_eval

        else:
            min_eval = +100
            for key in board.keys():
                if board[key] == ' ' and self.__t.validate_rules(key, self.movHuman, True):
                    #board[key] = self.movHuman
                    copy_board = board.copy()
                    self.__t.insert_move(key, self.movHuman, True)
                    score = self.minmax_alpa_betha(
                        key, alpha, beta, board, depth-1, True)
                    min_eval = min(min_eval, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        #board[key] = ' '
                        self.__t.setBoard(copy_board)
                        break
                    #board[key] = ' '
                    self.__t.setBoard(copy_board)
            return min_eval
