import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

broker = "103.11.99.171" #"jardik.web.id"
id = socket.gethostname()
ip = socket.gethostbyname(socket.gethostname())
client = mqtt.Client(id)
client.username_pw_set("root", "root")
client.connect(broker)
client.loop_start()

print(ip)

while True:
	now = datetime.now()
	data = now.strftime('%Y/%m/%d %H:%M:%S')
	#client.publish("opi2g/debug", "message: %s-%s-%s %s:%s:%s"
 #%(now.year, now.month, now.day, now.hour, now.minute, now.second))
	client.publish(id +"/debug", "{" +id +", "
			+ip +", "  +data +"}", retain=True)
	print("pub me \n")
	time.sleep(2)
		
