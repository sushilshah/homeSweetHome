import paho.mqtt.publish as publish
publish.single(topic=self.topic, payload=msg, hostname=self.host, auth=self.auth, tls=self.tls, port=self.port)

