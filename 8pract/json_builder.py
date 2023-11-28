import paho.mqtt.client as mqtt
import json
from datetime import datetime

mov = None
noise = None
light = None
temp = None
dict = []

# The callback for when the client receives a CONNACK response from the server.
#Функция для подключения к топикам
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/devices/wb-msw-v3_21/controls/Current Motion")
    client.subscribe("/devices/wb-msw-v3_21/controls/Sound Level")
    client.subscribe("/devices/wb-msw-v3_21/controls/Illuminance")
    client.subscribe("/devices/wb-msw-v3_21/controls/Temperature")


# The callback for when a PUBLISH message is received from the server.
#функция получения новых значений параметров и обновления json-файла
def on_message(client, userdata, msg):
    global mov, noise, light, temp
    print(msg.topic+" "+str(msg.payload))

    if msg.topic == "/devices/wb-msw-v3_21/controls/Current Motion":
        mov = msg.payload.decode()
    if msg.topic == "/devices/wb-msw-v3_21/controls/Sound Level":
        noise = msg.payload.decode()
    if msg.topic == "/devices/wb-msw-v3_21/controls/Illuminance":
        light = msg.payload.decode()
    if msg.topic == "/devices/wb-msw-v3_21/controls/Temperature":
        temp = msg.payload.decode()


    #Условие, проверяющие, что пришли новые знаения
    if mov != None and noise != None and light != None:
        with open('data.json', encoding="utf-8",) as f:
            dict = json.load(f) #Запись информации из json-файла
            obj = {"movement" : mov, "noise" : noise, "light" : light, "temperature" : temp, "case": 23, "time":str(datetime.now())}
            dict.append(obj) #добавление новой информации в dict
            #обнуление параметров
            mov = None
            noise = None
            light = None
            temp = None
        with open('data.json', 'w') as f:
            f.write(json.dumps(dict)) #добавление новой информации в json-файл

#client - объект класса Client, управляющий подключением к брокеру
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.2.23", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()