import tkinter as tk

from PIL import Image

from piece import PieceType

boardCaseMove = None

class BoardCaseMove(tk.Canvas):
    def __init__(self, board, coords, piece_type = PieceType.NONE):
        self.master = board
        self.coords = coords
        self.piece = piece_type
        
        tk.Canvas.__init__(self, board, width=100, height=100, borderwidth=0)
        self.place(x=coords[0], y=coords[1])
        
        self.display_update()
    
    def __destroy__(self):
        self.img_displayed.destroy()
        self.img.destroy()

    def display_update(self):
        if (self.piece != PieceType.NONE):
            self.img = tk.PhotoImage(file=self.piece.image_location())
            self.img_displayed = self.create_image(50, 50, image=self.img)

    def move(self, x, y):
        self.place(x=x, y=y)

class BoardCase(tk.Canvas):
    def __init__(self, board, coords, piece_type = PieceType.NONE):
        self.master = board
        self.coords = coords
        self.piece = piece_type
        self.bg_color = ("gray25", "lemon chiffon")[(coords[0] + coords[1]) % 2]
        
        tk.Canvas.__init__(self, board, width=100, height=100, bg=self.bg_color, borderwidth=0)
        self.place(x=(self.coords[1] - 1) * 100, y=(8 - self.coords[0]) * 100)
        self.display_update()
        
        self.bind('<B1-Motion>', self.mouse_moved)
        self.bind('<Button-1>', self.mouse_press)
        self.bind('<ButtonRelease-1>', self.mouse_release)

    def piece_link(self, piece_type):
        self.piece = piece_type
        self.display_update()
    
    def display_update(self):
        if (self.piece != PieceType.NONE):
            self.img = tk.PhotoImage(file=self.piece.image_location())
            self.img_displayed = self.create_image(50, 50, image=self.img)

    def real_coords(self):
        return self.master.winfo_pointerx() - self.master.winfo_rootx(), self.master.winfo_pointery() - self.master.winfo_rooty()

    def mouse_moved(self, event):
        global boardCaseMove

        if boardCaseMove is not None:
            x, y = self.real_coords()
            boardCaseMove.move(x - 50, y - 50)

    def mouse_press(self, event):
        global boardCaseMove

        if self.piece == PieceType.NONE:
            return

        event.widget["bg"] = "yellow"
        x, y = self.real_coords()
        boardCaseMove = BoardCaseMove(self.master, (x - 50, y - 50), self.piece)

    def mouse_release(self, event):
        global boardCaseMove

        if boardCaseMove is not None:
            event.widget["bg"] = self.bg_color
            boardCaseMove.destroy()
            boardCaseMove = None
        

class Board(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=800, height=800)
        self.master = parent

        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(BoardCase(self, (i + 1, j + 1)))

        self.newgame()

    def newgame(self):
        for i in range(8):
            self.board[1][i].piece_link(PieceType.WHITE_PAWN)
            self.board[6][i].piece_link(PieceType.BLACK_PAWN)

        self.board[0][0].piece_link(PieceType.WHITE_ROOK)
        self.board[0][7].piece_link(PieceType.WHITE_ROOK)
        self.board[7][0].piece_link(PieceType.BLACK_ROOK)
        self.board[7][7].piece_link(PieceType.BLACK_ROOK)
        
        self.board[0][1].piece_link(PieceType.WHITE_KNIGHT)
        self.board[0][6].piece_link(PieceType.WHITE_KNIGHT)
        self.board[7][1].piece_link(PieceType.BLACK_KNIGHT)
        self.board[7][6].piece_link(PieceType.BLACK_KNIGHT)
        
        self.board[0][2].piece_link(PieceType.WHITE_BISHOP)
        self.board[0][5].piece_link(PieceType.WHITE_BISHOP)
        self.board[7][2].piece_link(PieceType.BLACK_BISHOP)
        self.board[7][5].piece_link(PieceType.BLACK_BISHOP)
        
        self.board[0][3].piece_link(PieceType.WHITE_QUEEN)
        self.board[0][4].piece_link(PieceType.WHITE_KING)
        self.board[7][3].piece_link(PieceType.BLACK_QUEEN)
        self.board[7][4].piece_link(PieceType.BLACK_KING)
    
    def get(self, x, y):
        if 0 <= x and x <= 8 and 0 <= y and y <= 8:
            return self.board[x][y].piece
        return PieceType.NONE

    def display(self):
        for piece in self.pieces:
            coords = piece.coords()
            self.board[coords.x][coords.y]


class Game(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.resizable(False, False)
        self.geometry("800x800")
        
        self.board = Board(self)
        self.board.pack()

        self.bind("<Key>", self.handle_keypress)


    def handle_keypress(self, event):
        if event.char == "q":
            self.destroy()

if __name__ == "__main__":
    chess = Game()
    chess.mainloop()