import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

host = "A3AYPMLSON0XOW.iot.ap-northeast-1.amazonaws.com"
port = 8883
certfile = "/home/pi/homeSweetHome/cert.pem"
ca_certs  = "/home/pi/homeSweetHome/aws_setup/CA_certificate_aws_iot"
keyfile = "/home/pi/homeSweetHome/aws_setup/myHomePiPrivateKey.pem"
 
client = mqtt.Client()

client.tls_set(ca_certs, certfile=certfile, keyfile=keyfile, cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)
#tls_set(ca_certs, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
#   tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)

client.on_connect = on_connect
client.on_message = on_message

#client.connect("iot.eclipse.org", 1883, 60)
connect(host, port=port, keepalive=60, bind_address="")
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
