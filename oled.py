import ssd1306
import machine

class Oled:

    def __init__(self):
        i2c = machine.I2C(sda=machine.Pin(4), scl=machine.Pin(5), freq=400000)
        self.oled = ssd1306.SSD1306_I2C(128, 64, i2c, 60, False)

    def run(self):
        self.text('Witaj')

    def text(self,text,x=0,y=0):
        self.oled.text(text,x,y)
        self.oled.show()
