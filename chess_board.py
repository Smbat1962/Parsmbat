class Board:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]

class Piece:
    def __init__(self, color):
        self.color = color

class King(Piece):
    # Код для короля
    def figur(self):
        if self.color == "white":
            return "\u2654"
        elif self.color == "black":
            return "\u265A"
        
class Queen(Piece):
    # Код для ферзя
    def figur(self):
        if self.color == "white":
            return "\u2655"
        elif self.color == "black":
            return "\u265B"

class Rook(Piece):
    # Код для ладьи
    def figur(self):
        if self.color == "white":
            return "\u2656"
        elif self.color == "black":
            return "\u265C"

class Bishop(Piece):
    # Код для слона
    def figur(self):
        if self.color == "white":
            return "\u2657"
        elif self.color == "black":
            return "\u265D"

class Knight(Piece):
    # Код для коня
    def figur(self):
        if self.color == "white":
            return "\u2658"
        elif self.color == "black":
            return "\u265E"

class Pawn(Piece):
    # Код для пешки
    def figur(self):
        if self.color == "white":
            return "\u2659"
        elif self.color == "black":
            return "\u265F"
    



def main():
    bard = Board()
    bard.board[0][3] = King("white").figur()
    bard.board[7][4] = King("black").figur()
    bard.board[0][4] = Queen("white").figur()
    bard.board[7][3] = Queen("black").figur()
    bard.board[0][0] = Rook("white").figur()
    bard.board[0][7] = Rook("white").figur()
    bard.board[7][0] = Rook("black").figur()
    bard.board[7][7] = Rook("black").figur()
    bard.board[0][2] = Bishop("white").figur()
    bard.board[0][5] = Bishop("white").figur()
    bard.board[7][2] = Bishop("black").figur()
    bard.board[7][5] = Bishop("black").figur()
    bard.board[0][1] = Knight("white").figur()
    bard.board[0][6] = Knight("white").figur()
    bard.board[7][1] = Knight("black").figur()
    bard.board[7][6] = Knight("black").figur()
    for i in range(8):
        bard.board[1][i] = Pawn("white").figur()
        bard.board[6][i] = Pawn("white").figur()

    for i in range(8):
        print(bard.board[i])
    

if __name__ == "__main__":
    main()

