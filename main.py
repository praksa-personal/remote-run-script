import paho.mqtt.client as paho
from time import sleep

def on_publish(client, userdata, mid):
    print("msg.id: "+str(mid))

host_ip="localhost"
this_client_id = "WBT-station"

client = paho.Client(client_id=this_client_id,clean_session=False, protocol=paho.MQTTv31)
client.on_publish = on_publish

client.connect(host=host_ip, port=1883)
client.loop_start()


while(1):
    print("Enter y to send test run")
    flag = input()
    if(flag == 'y'):
        (rc, mid) = client.publish("my/test_1/start", str("script_to_run"), qos=1)
        flag = 0
    