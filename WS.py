
from machine import Pin
from neopixel import NeoPixel
from time import sleep

def init():
    np = NeoPixel(Pin(13),3)


def test(self):

    np[0] = (255,0,0)
    np[1] = (0,255,0)
    np[2] = (0,0,255)
    np.write()

#except KeyboardInterrupt:
 #   print("\n Ctrl-c pressed. Exit")
def off():
    np[0] = (0,0,0)
    np[1] = (0,0,0)
    np[2] = (0,0,0)
    np.write()