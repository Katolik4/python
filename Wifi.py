def connect():
    import network

    ssid="Dom_Smocza"
    password="biednykarzel"

    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("Połączono")
        return
    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print("Połączono")
    print(station.ifconfig())