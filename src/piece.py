from enum import IntEnum

from PIL import ImageTk, Image
import tkinter as tk

piece_name = {
    0: "pawn",
    1: "king",
    2: "queen",
    3: "knight",
    4: "bishop",
    5: "rook"
}

class PieceType(IntEnum):
    NONE = -1,
    BLACK_PAWN = 0,
    BLACK_KING = 1,
    BLACK_QUEEN = 2,
    BLACK_KNIGHT = 3,
    BLACK_BISHOP = 4,
    BLACK_ROOK = 5,
    WHITE_PAWN = 6,
    WHITE_KING = 7,
    WHITE_QUEEN = 8,
    WHITE_KNIGHT = 9,
    WHITE_BISHOP = 10,
    WHITE_ROOK = 11

    def image_location(self):
        if self.value == PieceType.NONE:
            return "";

        ret = "resource/pieces/"
        if self.value <= 5:
            ret = ret + "black_"
        else:
            ret = ret + "white_"

        ret = ret + piece_name[self.value % 6]

        return ret + ".png"