import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()

        # Pin mapping taken from the KiCad PCB for the XIAO RP2040 build.
        self.col_pins = (board.D0, board.D1, board.D9)
        self.row_pins = (board.D2, board.D3)
        self.diode_orientation = DiodeOrientation.COL2ROW
