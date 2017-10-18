from machine import Pin
from neopixel import NeoPixel
import urandom
import math
from time import sleep

class WS_class():

    def __init__(self):
        self.np = NeoPixel(Pin(13), 8)
        print("inicjacja WS")

    def hsvtorgb(self, h, s, v):

        h = float(h)
        s = float(s)
        v = float(v)
        h60 = h / 60.0
        h60f = math.floor(h60)
        hi = int(h60f) % 6
        f = h60 - h60f
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)
        r, g, b = 0, 0, 0
        if hi == 0:
            r, g, b = v, t, p
        elif hi == 1:
            r, g, b = q, v, p
        elif hi == 2:
            r, g, b = p, v, t
        elif hi == 3:
            r, g, b = p, q, v
        elif hi == 4:
            r, g, b = t, p, v
        elif hi == 5:
            r, g, b = v, p, q
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        return r, g, b

    def test(self):
        self.np[0] = (255, 0, 0)
        self.np[1] = (0, 255, 0)
        self.np[2] = (0, 0, 255)
        self.np.write()
        sleep(10)

        self.np[0] = (0, 0, 0)
        self.np[1] = (0, 0, 0)
        self.np[2] = (0, 0, 0)
        self.np.write()

    def alloff(self):
        for i in range(8):
            self.np[i] = (0,0,0)
        self.np.write()

    def random(self, t):

        while t > 0:

            for i in range(8):
                r = urandom.getrandbits(7)
                g = urandom.getrandbits(7)
                b = urandom.getrandbits(7)
                self.np[i] = (r, g, b)

            self.np.write()
            sleep(1)
            t -= 1






