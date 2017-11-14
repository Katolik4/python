import machine
from config import ConfigPL
cfg=ConfigPL()
scl=int(cfg.dict['piny']['i2c_scl'])
sda=int(cfg.dict['piny']['i2c_sda'])

class I2C:

    def __init__(self):
        self.i2c = machine.I2C(sda=machine.Pin(sda), scl=machine.Pin(scl), freq=400000)
        print("i2c start")

    def scan(self):
        p=self.i2c.scan()
        print(p)

