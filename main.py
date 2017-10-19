import network
import time


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
            sleep(0.5)

        print("Połączono")

    def scan(self):
        a = self.station.scan()
        for n in a:
            print("ssid: %s,        chanel: %s, RSSI: %s, authmode: %s, hidden: %s" % (n[0], n[2], n[3], n[4], n[5]))

if __name__ == '__main__':
    wifi.scan()
