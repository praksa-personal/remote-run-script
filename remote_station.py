import paho.mqtt.client as paho
import os

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    name = msg.payload.decode("utf-8") 
    print("Attempting to run: " + name + ".exe")
    os.startfile(name + ".exe")



host_ip="localhost"
this_client_id = "Subscriber-1"

client = paho.Client(client_id=this_client_id, clean_session=False, userdata=None, protocol=paho.MQTTv31)
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect(host=host_ip, port=1883)
client.subscribe("my/topic1", qos=1)

client.loop_forever()