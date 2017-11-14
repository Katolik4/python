from time import sleep_ms
from encoder import Encoder  # or from pyb_encoder import Encoder

print('start 1')

e = Encoder(pin_clk=9, pin_dt=10)  # optional: add pin_mode=Pin.PULL_UP
lastval = e.value

print('start enk')
print(lastval)

while True:
    val = e.value
    if lastval != val:
        lastpos = val
        print(val)
    sleep_ms(100)