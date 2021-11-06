import paho.mqtt.client as paho
from time import sleep

def on_publish(client, userdata, mid):
    print("msg.id: "+str(mid))


host_ip="localhost"
this_client_id = "Publisher-1"

client = paho.Client(client_id=this_client_id,clean_session=False, userdata=None, protocol=paho.MQTTv31)
client.on_publish = on_publish

client.connect(host=host_ip, port=1883)
client.loop_start()

(rc, mid) = client.publish("my/topic1", str("script_to_run"), qos=1)
sleep(10)