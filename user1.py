import paho.mqtt.client as mqtt
from time import sleep

def on_message(client,user_data,msg):
    print("User 2: " + str(msg.payload.decode("UTF-8")))

client = mqtt.Client()
mqtt_broker = "broker.emqx.io"
client.connect(mqtt_broker)
print("connected")
topicPost = "MMMUT_SoftPro1"
topicGet = "MMMUT_SoftPro2"
client.subscribe(topicGet)


while(True):
    whatToDo = input("Post / Get (P/G): ")
    if(whatToDo == "p" or whatToDo == "P"):
        message =input("You: ")
        client.publish(topicPost,message)
    elif(whatToDo == "g" or whatToDo == "G"):
        client.loop_start()
        client.on_message = on_message
        sleep(0.2)
        client.loop_stop()
    else:
        print("...")

        
