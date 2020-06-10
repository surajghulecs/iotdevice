'''
Created on Apr 18, 2019
@author: Suraj
'''

'''
Sends data to Ubidots using MQTT over TLS
'''
import sys,os
import project
sys.path.insert(0,'/home/pi/workspace/iot-device/apps')
import paho.mqtt.client as mqttClient
import time
import json
import ssl
from        project   import WeatherData
from        sense_hat       import SenseHat
sense = SenseHat()
sense.clear()

'''
global variables
'''
connected = False                                                                       # Stores the connection status
BROKER_ENDPOINT = "things.ubidots.com"                                                  # Stores the broker url
TLS_PORT = 8883                                                                         # Secure port
MQTT_USERNAME = ""                                                                      # Here we give our API Token(Left blank intentionally)
MQTT_PASSWORD = ""                                                                      # Left this in blank purposefully
TOPIC = "/v1.6/devices/"                                                                # Our parent topic name                                            
DEVICE_LABEL = "TEST"                                                                   # Our device label on ubidots
TLS_CERT_PATH = "/home/pi/workspace/iot-device/apps/labs/module08/ubidots_cert.pem"     # Put here the path of your TLS cert
weather = WeatherData.WeatherData()                                                     # Instance of the WeatherData class

'''
Functions to process incoming and outgoing streaming
@param client:The client is the client object, and is useful when you have multiple clients that are publishing data 
@param userdata:Any use data for logging purpose
@param flags:Used to set the flag
@param rc:return code
@return: None  
'''
def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print("[INFO] Connected to broker")
        global connected  # Use global variable
        connected = True  # Signal connection
    else:
        print("[INFO] Error, connection failed")

'''
When the message has been published to the Broker an acknowledgement is sent that 
results in the on_publish callback being called.
@param client:The client is the client object, and is useful when you have multiple clients that are publishing data
@param userdata:The userdata is user defined data which isn’t normally used.
@param result:The result is the message id and can be used with the result returned from the publish method to check 
that a particular message has been published. 
@return: None 
'''
def on_publish(client, userdata, result):
    print("Published!")

'''
Client initiates connection with the CONNECT message
@param mqtt_client:The client identifier (ClientId) identifies each MQTT client that connects to an MQTT broker. 
@param mqtt_username: MQTT can send a user name and password for client authentication and authorization. 
@param mqtt_password:MQTT can send a user name and password for client authentication and authorization. 
@param broker_endpoint:the IP address of a local network interface to bind this client to, assuming multiple interfaces exist
@param port:The network port of the server host to connect to. Defaults to 1883. 
@return: None 
'''
def connect(mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
    global connected

    if not connected:
        mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
        mqtt_client.on_connect = on_connect
        mqtt_client.on_publish = on_publish
        mqtt_client.tls_set(ca_certs=TLS_CERT_PATH, certfile=None,
                            keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                            tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        mqtt_client.tls_insecure_set(False)
        mqtt_client.connect(broker_endpoint, port=port)
        mqtt_client.loop_start()

        attempts = 0

        while not connected and attempts < 5:  # Wait for connection
            print(connected)
            print("Attempting to connect...")
            time.sleep(1)
            attempts += 1

    if not connected:
        print("[ERROR] Could not connect to broker")
        return False

    return True

'''
This causes a message to be sent to the broker and subsequently from the broker to any clients subscribing to matching topics.
@param mqtt_client::The client identifier (ClientId) identifies each MQTT client that connects to an MQTT broker. 
@param topic:The topic that the message should be published on
@param payload:The actual message to send. 
@return: None 
'''
def publish(mqtt_client, topic, payload):

    try:
        mqtt_client.publish(topic, payload)

    except Exception as e:
        print("[ERROR] Could not publish data, error: {}".format(e))

'''
Our main function which acts as starting point of program execution.
@param:None
@return True:Boolean value to continue the while loop infinitely
'''
def main():

    topic = "{}{}".format(TOPIC, DEVICE_LABEL)
    
    mqtt_client = mqttClient.Client()
    while True:
        payload = json.dumps({"TempSensor": weather.getTempValue()})
        payload1 = json.dumps({"HumiditySensor":weather.getHumidityValue()})    
        if not connect(mqtt_client, MQTT_USERNAME,MQTT_PASSWORD, BROKER_ENDPOINT, TLS_PORT):
            return False
        
        publish(mqtt_client, topic, payload)
        publish(mqtt_client, topic, payload1)
        time.sleep(10)
        print("Next Publication")        
    return True

'''
Start of our infinite while loop with main function
'''
if __name__ == '__main__':
    while True:
        main()
        time.sleep(10)
        
