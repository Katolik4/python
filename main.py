import network
import time
import ws_led


class wifi():

    def __init__(self):
        self.station= network.WLAN(network.STA_IF)
        self.ssid = "Dom_Smocza"
        self.password = "biednykarzel"
        self.station.active(True)
        print("ESP gotowe")

    def isconnected(self):
        if self.station.isconnected() == True:
            print("Połączono")
            return

    def connect(self):
        self.station.connect(self.ssid, self.password)

        while self.station.isconnected() == False:
            print("\n łączenie")
            time.sleep(0.5)

        print("Połączono")

    def scan(self):
        a = self.station.scan()
        for n in a:
            print("ssid: %s   chanel: %s    RSSI: %s    authmode: %s" % (n[0], n[2], n[3], n[4]))




if __name__ == '__main__':
    espwifi = wifi()
    espws = ws_led.WS_class()

    print('######################### \n')
    print("espwifi - ustawienia Wifi: .scan .connect .isconnected")
    print("espws - diody ws2812: .test .alloff .random(ile,co ile) .allcolors .linijka(kolor) .dioda(nr, color)")
    print("######################### \n")