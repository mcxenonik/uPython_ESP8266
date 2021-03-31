from machine import Pin
from neopixel import NeoPixel

pin = Pin(0, Pin.OUT)  # wyjście GPIO0>D3
np = NeoPixel(pin, 8)  # tworzymy obiekt NeoPixel dla 8 diód LED WS2812b
np[0] = (255, 255, 255)  # pierwszy pixel [0], kolor biały (R=255,G=255,B=255)
np[1] = (255, 0, 0)
np[2] = (255, 0, 0)
np[3] = (0, 255, 0)
np[4] = (0, 255, 0)
np[5] = (0, 0, 255)
np[6] = (0, 0, 255)
np[7] = (255, 255, 255)
np.write()  # zapisanie danych do wszystkich pixeli
