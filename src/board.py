import tkinter as tk

from piece import PieceType


class Board(tk.Canvas):
    selected = [-1, -1]
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

        self.images = {}

        self.newgame()
        
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

        for i in range(8):
            for j in range(8):
                img = tk.PhotoImage(file=self.pieces[i][j].image_location())
                self.create_image(j * 100 + 50, (7 - i) * 100 + 50, image=img, tag=self.get_tag(i, j))
                self.images[self.get_tag(i, j)] = img

    # Actions
    def move(self, x, y):
        tag = self.get_tag(x, y)
        selected_tag = self.get_tag(*self.selected)

        if (x < 0 or x > 7 or y < 0 or y > 7) or (tag == selected_tag):
            self.coords(selected_tag, self.selected[1] * 100 + 50, (7 - self.selected[0]) * 100 + 50)
            return

        if tag in self.images:
            self.delete(tag)
            self.images.pop(tag)

        self.coords(selected_tag, y * 100 + 50, (7 - x) * 100 + 50)
        self.itemconfig(selected_tag, tag=tag)
        self.images[tag] = self.images[selected_tag]

        self.delete(selected_tag)
        self.images.pop(selected_tag)

    # Getters
    def get_coords(self, event):
        return int(7 - (event.y - (event.y % 100)) / 100), int((event.x - (event.x % 100)) / 100)

    def get_tag(self, x, y):
        return (str(x) + "-" + str(y))

    # Bindings functions
    def mouse_moved(self, event):
        if self.selected != [-1, -1]:
            X = event.x
            Y = event.y

            if X < 50:
                X = 50
            elif X > 750:
                X = 750
                
            if Y < 50:
                Y = 50
            elif Y > 750:
                Y = 750

            selected_tag = self.get_tag(*self.selected)
            self.coords(selected_tag, X, Y)

    def mouse_press(self, event):
        x, y = self.get_coords(event)
        if not self.get_tag(x, y) in self.images:
            return

        self.selected = [x, y]
        selected_tag = self.get_tag(*self.selected)

        self.tag_raise(selected_tag)
        self.coords(selected_tag, event.x, event.y)
    
    def mouse_release(self, event):
        x, y = self.get_coords(event)
        if self.selected != [-1, -1]:
            self.move(x, y)
            self.selected = [-1, -1]

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