import board
import digitalio
import neopixel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)

while True:
    if not button.value:
        pixel.fill((0, 255, 0))
    else:
        pixel.fill((0, 0, 0))
