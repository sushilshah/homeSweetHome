#!/usr/bin/python

#required libraries
import sys                                 
import ssl
import paho.mqtt.client as mqtt

#called while client tries to establish connection with the server
def on_connect(mqttc, obj, flags, rc):
    if rc==0:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: successful")
    elif rc==1:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: Connection refused")

#called when a topic is successfully subscribed to
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos)+"data"+str(obj))

#called when a message is received by a topic
def on_message(mqttc, obj, msg):
    print("Received message from topic: "+msg.topic+" | QoS: "+str(msg.qos)+" | Data Received: "+str(msg.payload))

#creating a client with client-id=mqtt-test
mqttc = mqtt.Client(client_id="mqtt-test")

mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message

#Configure network encryption and authentication options. Enables SSL/TLS support.
#adding client-side certificates and enabling tlsv1.2 support as required by aws-iot service
ca_cert = "/home/pi/homeSweetHome/aws_setup/rootCA_certificate_aws_iot.crt"
cert_file = "/home/pi/homeSweetHome/aws_setup/cert.pem"
key_file = "/home/pi/homeSweetHome/aws_setup/myHomePiPrivateKey.pem"
host = "A3AYPMLSON0XOW.iot.ap-northeast-1.amazonaws.com"
port = 8883

mqttc.tls_set(ca_cert,
                certfile=cert_file,
                keyfile=key_file,
              tls_version=ssl.PROTOCOL_SSLv23,
              ciphers=None)

#connecting to aws-account-specific-iot-endpoint
mqttc.connect(host, port=port) #AWS IoT service hostname and portno

topic = "$aws/things/MyHomePi/shadow/update"

#the topic to publish to
mqttc.subscribe(topic, qos=1) #The names of these topics start with $aws/things/thingName/shadow."
#mqttc.publish("my/topic",'{"foo":"foo"}')

#automatically handles reconnecting
mqttc.loop_forever()
