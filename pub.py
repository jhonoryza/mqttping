import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

#broker = "103.11.99.171" 
broker = "jardik.web.id"
id = socket.gethostname()
ip = socket.gethostbyname(socket.gethostname())
print(id +" " +ip)

client = mqtt.Client(id)
client.username_pw_set("root", "root")
client.connect(broker, 1883, 60)
client.loop_start()

while True:
	now = datetime.now()
	data = now.strftime('%Y/%m/%d %H:%M:%S')
	#client.publish("opi2g/debug", "message: %s-%s-%s %s:%s:%s"
 #%(now.year, now.month, now.day, now.hour, now.minute, now.second))
	message = "{" +id +", " +ip +", "  +data +"}"
	client.publish(id+"/debug", message, retain=True)
	print(message +" \n")
	time.sleep(2)
		
