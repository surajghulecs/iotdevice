'''
Created on Apr 18, 2019
@author: Suraj
'''

'''
Subscribes data from Ubidots using MQTT over TLS
'''
import paho.mqtt.client as mqtt                         # importing the paho library
from sense_hat import SenseHat                          # importing the SenseHat library

sense = SenseHat()                                      # Creating instance of SenseHat
sense.clear()                                           # Command to clear the SenseHat display

BROKER_ENDPOINT = "things.ubidots.com"                  # Our broker url
PORT = 1883
MQTT_USERNAME = "**********************************"    # API Token used to connect to our broker, Intentioanlly kept blank
MQTT_PASSWORD = ""                                      # Intentionally kept blank
TOPIC = "/v1.6/devices"                                 # Our parent topic name
DEVICE_LABEL = "test"                                   # Device name to be subscribed
VARIABLE_LABEL = "average-temperature"                  # Variable name to be subscribed

'''
Functions to process incoming and outgoing streaming
@param client:The client is the client object, and is useful when you have multiple clients that are publishing data 
@param userdata:Any use data for logging purpose
@param flags:Used to set the flag
@param rc:return code
@return: None  
'''
def on_connect(mqttc, obj, flags, rc):
    print("[INFO] Connected!")
    topic = "{}/{}/{}/".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL)
    print(topic)
    mqttc.subscribe(topic, 0)

'''
Called when a message has been received on a topic that the client subscribes to and the message does not match 
an existing topic filter callback.
@param mqttc:the client instance for this callback
@param obj:the private user data as set in Client() or user_data_set()
@param msg:an instance of MQTTMessage. This is a class with members topic, payload, qos, retain.
@return: None   
'''
def on_message(mqttc, obj, msg):
    print("[INFO] value received: {}".format(float(msg.payload)))
    return msg.payload

'''
When the message has been published to the Broker an acknowledgement is sent that 
results in the on_publish callback being called.
@param mqttc:The client is the client object, and is useful when you have multiple clients that are publishing data
@param obj:The userdata is user defined data which isn’t normally used.
@param mid:The result is the message id and can be used with the result returned from the publish method to check 
that a particular message has been published. 
@return: None 
'''
def on_publish(mqttc, obj, mid):
    print("[INFO] Published!")

'''
Called when the broker responds to a subscribe request.
@param mqttc:The client is the client object, and is useful when you have multiple clients that are publishing data
@param obj:The userdata is user defined data which isn’t normally used.
@param mid:The result is the message id and can be used with the result returned from the publish method to check 
that a particular message has been published.
@param granted_qos:The granted_qos variable is a list of integers that give the QoS level the broker has granted 
for each of the different subscription requests.
@return: None 
'''
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("[INFO] Subscribed!")

'''
Called when the client has log information.
@param mqttc:The client is the client object, and is useful when you have multiple clients that are publishing data
@param obj:The userdata is user defined data which isn’t normally used.
@param level:The level variable gives the severity of the message and will be one of MQTT_LOG_INFO, MQTT_LOG_NOTICE, 
MQTT_LOG_WARNING, MQTT_LOG_ERR, and MQTT_LOG_DEBUG.
@param string:The message itself is in string
@return: None 
'''
def on_log(mqttc, obj, level, string):
    print("[INFO] Log info: {}".format(string))

'''
Our main function which acts as starting point of program execution.
@param:None
@return:None
'''
def main():
    
    '''
    Configuring the MQTT client
    '''
    mqttc = mqtt.Client()
    mqttc.username_pw_set(MQTT_USERNAME, password="")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    #mqttc.on_log = on_log                                               
    mqttc.connect(BROKER_ENDPOINT, PORT, 60)
    topic = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL)
    print(topic)
    sense.show_message("AC ON")
    mqttc.loop_forever()
    
'''
Start of our infinite while loop with main function
'''
if __name__ == '__main__':
    main()
