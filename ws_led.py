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

    def random(self, t, okres):
        while t > 0:

            for i in range(8):
                h = urandom.getrandbits(8)
                self.np[i] = (self.hsvtorgb(h, 1, 0.5))

            self.np.write()
            sleep(okres)
            t -= 1

    def allcolors(self):
        c = 0

        while c < 360:

            for i in range(8):
                h = c + i
                self.np[i] = (self.hsvtorgb(h, 1, 0.5))

            self.np.write()
            sleep(0.05)
            c += 1

    def linijka(self, color):
        for i in range(8):
            self.np[i] = (self.hsvtorgb(color, 1, 0.5))
        self.np.write()

    def dioda(self, nr, color):
        self.np[nr] = (self.hsvtorgb(color, 1, 0.5))
        self.np.write()






