class Board:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]

    def setup_board(self):
        for i in range(8):
            for j in range(8):
                if i == 0 or i == 7:
                    if j == 0 or j == 7:
                        self.board[i][j] = Rook(
                            "white" if i == 0 else "black").figur()
                if i == 0 or i == 7:
                    if j == 2 or j == 5:
                        self.board[i][j] = Bishop(
                            "white" if i == 0 else "black").figur()
                if i == 0 or i == 7:
                    if j == 1 or j == 6:
                        self.board[i][j] = Knight(
                            "white" if i == 0 else "black").figur()
                if i == 0:
                    if j == 3:
                        self.board[i][j] = King("white").figur()
                    if j == 4:
                        self.board[i][j] = Queen("white").figur()
                if i == 7:
                    if j == 4:
                        self.board[i][j] = King("black").figur()
                    if j == 3:
                        self.board[i][j] = Queen("black").figur()
        for i in range(8):
            self.board[1][i] = Pawn("white").figur()
            self.board[6][i] = Pawn("black").figur()
        for i in range(8):
            print(self.board[i])


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
    board = Board()
    board.setup_board()


if __name__ == "__main__":
    main()
