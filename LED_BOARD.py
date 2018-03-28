import machine
import utime

class Led_board():

    def __init__(self):
        self.led = machine.Pin(2, machine.Pin.OUT)
        self.led_pwm = machine.PWM(self.led)
        self.led_pwm.freq(1000)

    def fade_led(self, czas):
        while True:
            for i in range(1024):
                self.led_pwm.duty(i)
                utime.sleep_ms(czas)
            for i in range(1024, -1, -1):
                self.led_pwm.duty(i)
                utime.sleep_ms(czas)

    def pwm(self, pwm):
        self.led_pwm.duty(pwm)

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()


