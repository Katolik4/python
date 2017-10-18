
def main():
    print('Załadowano main')
    Wifiscan()

def Wifistart():
    import network
    ssid = "Dom_Smocza"
    password = "biednykarzel"

    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("Połączono")
        return
    station.active(True)

def Wificonncet():
    import network
    station = network.WLAN(network.STA_IF)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print("Połączono")
    print(station.ifconfig())

def Wifiscan():

    import network
    import ubinascii
    station = network.WLAN(network.STA_IF)
    station.active(True)

    a = station.scan()

    for n in a:

        print("ssid: %s,        chanel: %s, RSSI: %s, authmode: %s, hidden: %s" % (n[0], n[2], n[3], n[4], n[5]))

if __name__ == '__main__':
        main()