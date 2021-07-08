import tkinter as tk

class Board():
    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(False, False)
        
        b = False

        for i in range(8):
            for j in range(8):
                frame = tk.Frame(master=self.window, relief=tk.RAISED, bg=("lemon chiffon", "gray25")[b], width=50, height=50)
                frame.grid(row=i, column=j)
                
                b = not b
            b = not b
        
        self.window.bind("<Key>", self.handle_keypress)
    
    def mainloop(self):
        self.window.mainloop()

    def handle_keypress(self, event):
        if event.char == "q":
            self.window.destroy()
        print(event.char) 

if __name__ == "__main__":
    board = Board()
    board.mainloop()