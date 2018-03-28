import MQTT

class Mqtt:

    def __init__(self):
        self.server = "192.168.0.11"
        self.client = "ESP12E"
        self.connect()
        print("Połączono z %s", self.server)

    def connect(self):
        self.c = MQTT.MQTTClient(self.client, self.server, 1883, "esp")
        self.c.connect()

    def sub_cb(self, topic, msg):
        print((topic, msg))

    def set_cb(self):
        self.c.set_callback(self.sub_cb)
    def sub_block(self):
        self.c.wait_msg()

    def sub_noblock(self):
        self.c.check_msg()

    def pub(self, topic, msg):
        self.c.publish(topic, msg)

