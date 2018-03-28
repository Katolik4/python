import network
import time
import ws_led
import ujson
import oled
import qq
from config import ConfigPL

cfg = ConfigPL()
siec = cfg.siec['ssid']
password = cfg.siec['pass']


class WiFi():

    def __init__(self, ssid=siec, password=password):
        self.station= network.WLAN(network.STA_IF)
        self.ssid = ssid
        self.password = password
        self.station.active(True)
        print("espwifi - ustawienia Wifi: .scan .connect .isconnected")

    def isconnected(self):
        if self.station.isconnected() == True:
            print("Połączono")
            return

    def connect(self):
        self.station.connect(self.ssid, self.password)

        while self.station.isconnected() == False:
            print("łączenie")
            time.sleep(0.5)

        print("Połączono")
        print(self.station.ifconfig())

    def scan(self):
        a = self.station.scan()
        for n in a:
            print("ssid: %s   chanel: %s    RSSI: %s    authmode: %s" % (n[0], n[2], n[3], n[4]))





if __name__ == '__main__':

    print('#########################')
    espwifi = WiFi()
    espws = ws_led.WS()
    espoled = oled.Oled()
    espmqtt = qq.Mqtt()
    print('#########################')
