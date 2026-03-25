from sys import path

import board

from kb import KMKKeyboard
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.rgb import RGB
from kmk.keys import KC
from kmk.modules import Module

keyboard = KMKKeyboard()

rgb = RGB(
    pixel_pin=board.D10,
    num_pixels=4,
    val_default=40,
)
keyboard.extensions.append(rgb)

display = Display(
    display=SSD1306(sda=board.D4, scl=board.D5),
    entries=[

        TextEntry(text='Minecraft', x=64, y=4, x_anchor='M', y_anchor='T'),
        TextEntry(text='Lectern', x=64, y=18, x_anchor='M', y_anchor='T'),
    ],
    flip=True,
)
keyboard.extensions.append(display)

KEY_LABELS = {
    0: 'F13',
    1: 'F14',
    2: 'F15',
    3: 'F16',
    4: 'F17',
    5: 'F18',
}


def show_idle():
    display.entries = [
        ImageEntry(image = "key_up.bmp", x=32, y=16),
        TextEntry(text='Minecraft', x=96, y=16, x_anchor='M', y_anchor='T'),
    ]
    display.render(keyboard.active_layers[0])


def show_pressed(name):
    display.entries = [
        ImageEntry(image = "key_down.bmp", x=32, y=16),
        TextEntry(text=name, x=100, y=16, x_anchor='M', y_anchor='T'),
    ]
    display.render(keyboard.active_layers[0])


class DisplayListener(Module):
    def __init__(self):
        self._timeout = None

    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def process_key(self, keyboard, key, is_pressed, int_coord):
        if is_pressed and int_coord is not None:
            show_pressed(KEY_LABELS.get(int_coord, f'Key {int_coord + 1}'))

            if self._timeout is not None:
                keyboard.cancel_timeout(self._timeout)

            self._timeout = keyboard.set_timeout(1000, show_idle)

        return key

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return


keyboard.modules.append(DisplayListener())

keyboard.keymap = [
    [
        KC.F13,
        KC.F14,
        KC.F15,
        KC.F16,
        KC.F17,
        KC.F18,
    ]
]

if __name__ == '__main__':
    keyboard.go()
