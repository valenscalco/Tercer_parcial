class TaTeTi():
    def __init__(self, board=None):
        if not board:
            board = [' ' for _ in range(9)]
        self.board = board

    def full(self):
        for i in range(9):
            if self.board[i] == ' ':
                return False

        return True

    def win(self):
        for i in range(9):
            if i == 0 or i == 3 or i == 6:
                if self.board[i] == 'x' and self.board[i+1] == 'x' and self.board[i+2] == 'x':
                    return True
                if self.board[i] == 'o' and self.board[i+1] == 'o' and self.board[i+2] == 'o':
                    return True
        if self.board[2] == 'x' and self.board[4] == 'x' and self.board[6] == 'x':
            return True
        elif self.board[2] == 'o' and self.board[4] == 'o' and self.board[6] == 'o':
            return True
        if self.board[0] == 'x' and self.board[4] == 'x' and self.board[8] == 'x':
            return True
        elif self.board[0] == 'o' and self.board[4] == 'o' and self.board[8] == 'o':
            return True
        if self.board[2] == 'x' and self.board[5] == 'x' and self.board[8] == 'x':
            return True
        elif self.board[2] == 'o' and self.board[5] == 'o' and self.board[8] == 'o':
            return True
        if self.board[1] == 'x' and self.board[4] == 'x' and self.board[7] == 'x':
            return True
        elif self.board[1] == 'o' and self.board[4] == 'o' and self.board[7] == 'o':
            return True
        if self.board[0] == 'x' and self.board[3] == 'x' and self.board[6] == 'x':
            return True
        elif self.board[0] == 'o' and self.board[3] == 'o' and self.board[6] == 'o':
            return True

        return False

    def validate(self, position):
        if self.board[position-1] == ' ':
            return True
        return False

    def assign(self, position, piece):
        if self.validate(position):
            self.board[position-1] = piece
        else:
            raise Exception

    def draw_board(self):
        self.display = "\n"
        for i in range(9):
            if self.board[i] != " ":
                self.display += " " + self.board[i] + " "
            else:
                self.display += " " + str(1+i) + " "
            if i == 2 or i == 5:
                self.display += "\n---+---+---\n"
            elif i == 8:
                self.display += "\n"
            else:
                self.display += "|"
        return self.display
