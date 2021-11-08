import paho.mqtt.client as paho
import os
import proc
import psutil
import datetime


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_publish(client, userdata, mid):
    print("msg.id: "+str(mid))

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    name = msg.payload.decode("utf-8")
    name = name + '.exe'
    print("Attempting to run: " + name)
    
    os.startfile(name)
    t1, test_pid, test_name = proc.on_test_start(name)
    procs_list = [psutil.Process(test_pid)]
    gone, alive = psutil.wait_procs(
        procs_list, timeout=30, callback=proc.on_terminate)
    print("terminated")
    t2 = datetime.datetime.now()
    t2 = t2.strftime("%H:%M:%S")
    FMT = '%H:%M:%S'
    tdelta = datetime.datetime.strptime(
        t2, FMT) - datetime.datetime.strptime(t1, FMT)
    send_test_runtime(name, tdelta)
    

def send_test_runtime(name, t):
    print(t)
    (rc, mid) = client.publish("my/test_1/end", "Test " + name + " terminated." + "\nTotal runtime: " + str(t), qos=1)

host_ip = "localhost"
this_client_id = "Test-station"

client = paho.Client(client_id=this_client_id,
                     clean_session=False, protocol=paho.MQTTv31)
        
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect(host=host_ip, port=1883)
client.subscribe("my/test_1/start", qos=1)
client.loop_forever()
