# KMK Firmware Setup

This repo already includes a local copy of KMK in [`../kmk_firmware`](../kmk_firmware).

## Board mapping

These pins were taken from the KiCad PCB for the XIAO RP2040:

- Matrix columns: `D0`, `D1`, `D9`
- Matrix rows: `D2`, `D3`
- OLED: `D4` = SDA, `D5` = SCL
- WS2812 chain: `D10`

## What to copy to `CIRCUITPY`

1. Install CircuitPython for the Seeed Studio XIAO RP2040.
2. Copy `kmk_firmware/kmk/` to the root of `CIRCUITPY`.
3. Copy `kmk_firmware/boot.py` to the root of `CIRCUITPY`.
4. Copy [`main.py`](./main.py) and [`kb.py`](./kb.py) to the root of
   `CIRCUITPY`.
5. Copy these CircuitPython display libraries into `CIRCUITPY/lib/`:

   - `adafruit_displayio_ssd1306.mpy`
   - `adafruit_display_text/`
6. Copy this CircuitPython RGB library into `CIRCUITPY/lib/`:

   - `neopixel.py`

[`main.py`](./main.py) keeps the keymap minimal, but it does initialize the
OLED on `D4`/`D5` and the WS2812 LEDs on `D10`. The OLED defaults to an idle
screen and switches to the pressed key name for one second whenever a key is
pressed.

## Example Linux copy command

```sh
cp -r kmk_firmware/kmk /run/media/$USER/CIRCUITPY/
cp kmk_firmware/boot.py firmware/main.py firmware/kb.py /run/media/$USER/CIRCUITPY/
```
