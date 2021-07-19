import tkinter as tk

from piece import PieceType
        

class Board(tk.Canvas):
    selected = None
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent, width=800, height=800, borderwidth=0)
        self.master = parent
        
        self.background_case = []
        for i in range(8):
            self.background_case.append([])
            for j in range(8):
                c = self.create_rectangle(j * 100, (7 - i) * 100,
                                          (j + 1) * 100, (8 - i) * 100,
                                          fill=("gray25", "lemon chiffon")[(i + j) % 2])
                self.background_case[i].append(c)

        self.pieces = []
        for i in range(8):
            self.pieces.append([])
            for j in range(8):
                self.pieces[i].append(PieceType.NONE)

        self.images = []

        self.newgame()
        self.display()
        
        self.bind('<B1-Motion>', self.mouse_moved)
        self.bind('<Button-1>', self.mouse_press)
        self.bind('<ButtonRelease-1>', self.mouse_release)

    def newgame(self):
        for i in range(8):
            self.pieces[1][i] = PieceType.WHITE_PAWN
            self.pieces[6][i] = PieceType.BLACK_PAWN

        self.pieces[0][0] = PieceType.WHITE_ROOK
        self.pieces[0][7] = PieceType.WHITE_ROOK
        self.pieces[7][0] = PieceType.BLACK_ROOK
        self.pieces[7][7] = PieceType.BLACK_ROOK
        
        self.pieces[0][1] = PieceType.WHITE_KNIGHT
        self.pieces[0][6] = PieceType.WHITE_KNIGHT
        self.pieces[7][1] = PieceType.BLACK_KNIGHT
        self.pieces[7][6] = PieceType.BLACK_KNIGHT
        
        self.pieces[0][2] = PieceType.WHITE_BISHOP
        self.pieces[0][5] = PieceType.WHITE_BISHOP
        self.pieces[7][2] = PieceType.BLACK_BISHOP
        self.pieces[7][5] = PieceType.BLACK_BISHOP
        
        self.pieces[0][3] = PieceType.WHITE_QUEEN
        self.pieces[0][4] = PieceType.WHITE_KING
        self.pieces[7][3] = PieceType.BLACK_QUEEN
        self.pieces[7][4] = PieceType.BLACK_KING

    def display(self):
        for i in range(8):
            for j in range(8):
                img = tk.PhotoImage(file=self.pieces[i][j].image_location())
                self.create_image(j * 100 + 50, (7 - i) * 100 + 50, image=img, tag=str(i) + "-" + str(j))
                self.images.append(img)

    def get_coords(self, event):
        return int(7 - (event.y - (event.y % 100)) / 100), int((event.x - (event.x % 100)) / 100)

    def mouse_moved(self, event):
        if self.selected is not None:
            self.coords(self.selected, event.x, event.y)

    def mouse_press(self, event):
        x, y = self.get_coords(event)
        self.selected = str(x) + "-" + str(y)
        self.coords(self.selected, event.x, event.y)
    
    def mouse_release(self, event):
        x, y = self.get_coords(event)
        if self.selected is not None:
            self.coords(self.selected, y * 100 + 50, (7 - x) * 100 + 50)
            self.itemconfig(self.selected, tag=str(x) + "-" + str(y))
            self.selected = None

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