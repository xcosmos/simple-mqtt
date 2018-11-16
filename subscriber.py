# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

HOST = '127.0.0.1'
PORT = 1883
KEEP_ALIVE = 60
TOPIC = 'test_topic/test1'

def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))
    client.subscribe(client.topic)

def on_message(client, userdata, message):
    print(message.topic + ' ' + str(message.payload))

if __name__ == '__main__':

    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.topic = TOPIC

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(HOST, port=PORT, keepalive=KEEP_ALIVE)

    client.loop_forever()                                  
