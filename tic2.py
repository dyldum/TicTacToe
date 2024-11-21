import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player1 = tk.StringVar()
        self.player2 = tk.StringVar()
        self.turn = True  # True for player1, False for player2
        self.board = [""] * 9
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Player 1 Name:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.player1).grid(row=0, column=1)
        tk.Label(self.root, text="Player 2 Name:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.player2).grid(row=1, column=1)
        self.buttons = [tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2, command=lambda i=i: self.click(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=(i // 3) + 2, column=i % 3)
        tk.Button(self.root, text="Restart", command=self.restart).grid(row=5, column=0, columnspan=3)

    def click(self, index):
        if self.board[index] == "":
            self.board[index] = "X" if self.turn else "O"
            self.buttons[index].config(text=self.board[index], fg="blue" if self.turn else "red", font=('Helvetica', 20, 'bold'))
            if self.check_winner():
                winner = self.player1.get() if self.turn else self.player2.get()
                messagebox.showinfo("Tic Tac Toe", f"{winner} wins!")
                self.restart()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.restart()
            self.turn = not self.turn

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                return True
        return False

    def restart(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.turn = True

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()