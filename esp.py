import machine

import time
from MQTT import MQTTClient

led=machine.Pin(25, machine.Pin.OUT)


import ubinascii
import micropython

print('test1')
# ESP8266 ESP-12 modules have blue, active-low LED on GPIO2, replace
# with something else if needed.


# Default MQTT server to connect to
SERVER = "192.168.0.10"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"/led"


state = 0

def sub_cb(topic, msg):
    global state
    print((topic, msg))
    if msg == b"on":
        led.value(0)
        state = 1
    elif msg == b"off":
        led.value(1)
        state = 0
    elif msg == b"toggle":
        # LED is inversed, so setting it to current state
        # value will make it toggle
        led.value(state)
        state = 1 - state


def main(server=SERVER):
    c = MQTTClient(CLIENT_ID, server)
    # Subscribed messages will be delivered to this callback
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))

    try:
        while 1:
            #micropython.mem_info()
            c.wait_msg()
    finally:
        c.disconnect()