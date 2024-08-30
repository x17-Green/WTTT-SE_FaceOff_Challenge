# game models
class Game:
    def __init__(self):
        self.board = ['', '', '', '', '', '', '', '', '']
        self.turn = 'X'
        self.players = []

    def make_move(self, index, player):
        if self.board[index] == '' and self.turn == player:
            self.board[index] = player
            self.turn = 'O' if player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        win_combinations = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
            [0, 3, 6],  # Left column
            [1, 4, 7],  # Center column
            [2, 5, 8],  # Right column
            [0, 4, 8],  # Diagonal (top-left to bottom-right)
            [2, 4, 6]   # Diagonal (top-right to bottom-left)
        ]
        for combo in win_combinations:
            if self.board[combo[0]] != '' and self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                return self.board[combo[0]]
        return None