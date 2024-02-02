class TicTacToe:
    # Inisialisasi papan permainan dengan spasi kosong (' ') dan setel pemain saat ini ke 'X'.
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
    # Mencetak status papan Tic-Tac-Toe saat ini dalam format 3x3.
    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("---------")
    # Memungkinkan pemain untuk bergerak di papan dengan menentukan posisi (1-9). 
    # Memeriksa apakah langkah tersebut valid dan memperbarui papan sesuai dengan itu.
    # Mengganti pemain saat ini setelah gerakan yang valid.
    def make_move(self, position):
        if 1 <= position <= 9 and self.board[position - 1] == ' ':
            self.board[position - 1] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")
    # Memeriksa pemenang dengan memeriksa baris, kolom, dan diagonal.
    # Mengembalikan True jika pemain menang, jika tidak False.
    def check_winner(self):
        # Periksa baris
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != ' ':
                return True

        # Periksa kolom
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ':
                return True

        # Periksa diagonal
        if self.board[0] == self.board[4] == self.board[8] != ' ' or \
           self.board[2] == self.board[4] == self.board[6] != ' ':
            return True

        return False
    # Memeriksa apakah papan terisi penuh dengan gerakan. 
    # Mengembalikan Truejika papan penuh, menunjukkan seri.
    def is_board_full(self):
        return ' ' not in self.board

# Fungsi utama program
def main():
    game = TicTacToe()

    while not game.check_winner() and not game.is_board_full():
        game.print_board()
        try:
            position = int(input(f"Player {game.current_player}, enter your move (1-9): "))
            game.make_move(position)
        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("Invalid input. Please enter a number between 1 and 9.")
    # Mencetak keadaan akhir papan dan mengumumkan pemenang atau menyatakan seri.
    game.print_board()

    if game.check_winner():
        print(f"Player {game.current_player} wins!")
    else:
        print("It's a draw!")

# Memastikan bahwa program utama dijalankan hanya, 
# jika file ini dieksekusi langsung 
if __name__ == "__main__":
    main()
