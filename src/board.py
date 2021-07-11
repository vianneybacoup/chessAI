import tkinter as tk

from piece import Piece, PieceType

class Board:
    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(False, False)
        
        b = False

        for i in range(8):
            for j in range(8):
                frame = tk.Frame(master=self.window, relief=tk.RAISED, bg=("lemon chiffon", "gray25")[b], width=100, height=100)
                frame.grid(row=i, column=j)
                
                b = not b
            b = not b

        self.newgame()

        self.window.bind("<Key>", self.handle_keypress)

    def newgame(self):
        self.pieces = []

        c = "a"
        for _ in range(8):
            self.pieces.append(Piece(PieceType.WHITE_PAWN, (2, c)))
            self.pieces.append(Piece(PieceType.BLACK_PAWN, (7, c)))
            c = chr(ord(c) + 1)

        self.pieces.append(Piece(PieceType.WHITE_ROOK, (1, "a")))
        self.pieces.append(Piece(PieceType.WHITE_ROOK, (8, "a")))
        self.pieces.append(Piece(PieceType.BLACK_ROOK, (1, "h")))
        self.pieces.append(Piece(PieceType.BLACK_ROOK, (8, "h")))

        self.pieces.append(Piece(PieceType.WHITE_KNIGHT, (2, "a")))
        self.pieces.append(Piece(PieceType.WHITE_KNIGHT, (7, "a")))
        self.pieces.append(Piece(PieceType.BLACK_KNIGHT, (2, "h")))
        self.pieces.append(Piece(PieceType.BLACK_KNIGHT, (7, "h")))

        self.pieces.append(Piece(PieceType.WHITE_BISHOP, (3, "a")))
        self.pieces.append(Piece(PieceType.WHITE_BISHOP, (6, "a")))
        self.pieces.append(Piece(PieceType.BLACK_BISHOP, (3, "h")))
        self.pieces.append(Piece(PieceType.BLACK_BISHOP, (6, "h")))

        self.pieces.append(Piece(PieceType.WHITE_QUEEN, (4, "a")))
        self.pieces.append(Piece(PieceType.WHITE_KING, (5, "a")))
        self.pieces.append(Piece(PieceType.BLACK_QUEEN, (4, "h")))
        self.pieces.append(Piece(PieceType.BLACK_KING, (5, "h")))

    def mainloop(self):
        self.window.mainloop()

    def handle_keypress(self, event):
        if event.char == "q":
            self.window.destroy()

if __name__ == "__main__":
    board = Board()
    board.mainloop()