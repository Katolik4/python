def random():

    import time
    from MQTT import MQTTClient
    import urandom
    SERVER = '192.168.0.10'
    CLIENT_ID = "ESP32"
    TOPIC="/ESP"
    client = MQTTClient(CLIENT_ID, SERVER)
    client.connect()


    while True:
        try:
            i = urandom.getrandbits(10)
            msg = "%s" % (i)
            client.publish(TOPIC, msg)
            print(msg)

        except OSError:
            print('Blad')

        time.sleep(1)

