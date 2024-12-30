import random

class MGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.revealed = [[False for _ in range(4)] for _ in range(4)]  # Track revealed cards
        self.matched_pairs = 0
        self.total_pairs = 8  # 8 pairs to match (for a 4x4 grid)

    def initialize_board(self):
        """Initialize the board with pairs of cards."""
        cards = list(range(1, 9)) * 2  # Create pairs (1-1, 2-2, ..., 8-8)
        random.shuffle(cards)  # Shuffle the cards
        return [cards[i:i + 4] for i in range(0, len(cards), 4)]  # Create 4x4 grid

    def print_board(self):
        """Print the board with hidden and revealed cards."""
        for r in range(4):
            for c in range(4):
                if self.revealed[r][c]:
                    print(self.board[r][c], end="  ")
                else:
                    print("X", end="  ")  # Hidden card
            print()

    def get_player_move(self):
        """Get a valid player move (row and column)."""
        while True:
            try:
                move = input("Enter your move (row col): ").split()
                row, col = int(move[0]), int(move[1])
                if 0 <= row < 4 and 0 <= col < 4:
                    return row, col
                else:
                    print("Invalid input. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

    def play_turn(self):
        """Handle a single turn of the game."""
        print("Select the first card to flip:")
        row1, col1 = self.get_player_move()
        
        if self.revealed[row1][col1]:
            print("Card already revealed. Try again.")
            return False

        self.revealed[row1][col1] = True
        self.print_board()

        print("Select the second card to flip:")
        row2, col2 = self.get_player_move()

        if self.revealed[row2][col2]:
            print("Card already revealed. Try again.")
            self.revealed[row1][col1] = False  # Hide the first card again
            return False

        self.revealed[row2][col2] = True
        self.print_board()

        # Check if the two cards match
        if self.board[row1][col1] == self.board[row2][col2]:
            print("It's a match!")
            self.matched_pairs += 1
            return True
        else:
            print("Not a match. Cards will be hidden again.")
            self.revealed[row1][col1] = False
            self.revealed[row2][col2] = False
            return False

    def play_game(self):
        """Main game loop."""
        print("Welcome to the Memory Card Game!")

        # Game loop
        while self.matched_pairs < self.total_pairs:
            self.print_board()
            if not self.play_turn():
                input("Press Enter to continue...")

        print("Congratulations! You've matched all pairs!")

# Start the game
if __name__ == "__main__":
    game = MGame()
    game.play_game()
