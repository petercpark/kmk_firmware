import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.A3,
        board.A2,
        board.A1,
        board.A0,
        board.SCK,
        board.MISO,
    )
    row_pins = (board.D4, board.D5, board.D6, board.D7)
    diode_orientation = DiodeOrientation.COLUMNS
