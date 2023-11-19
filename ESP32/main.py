import network
from machine import Pin, PWM
import dht
import ujson
from umqtt.simple import MQTTClient
import json
import time

# Pin for controlling the LED
LED_PIN = 4  # Assuming GPIO 4 is connected to the LED
SOM_PIN = 12
# Function to turn on the LED
def turn_on_led():
    led = Pin(LED_PIN, Pin.OUT)
    led.value(1)  # Assuming HIGH turns on the LED
    som = PWM(Pin(SOM_PIN))
    som.freq(1000)  # Set the frequency of the sound (adjust as needed)
    som.duty(512)  # Set the duty cycle to control volume

# Function to turn off the LED
def turn_off_led():
    led = Pin(LED_PIN, Pin.OUT)
    led.value(0)  # Assuming LOW turns off the LED
    som = PWM(Pin(SOM_PIN))
    som.deinit()



# MQTT Server Parameters
MQTT_CLIENT_ID = "micropython-weather-demo"
MQTT_BROKER = "broker.mqttdashboard.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_TOPIC = "teste_fiap"
MQTT_TOPIC_OUT = "teste_fiap_out"

#Acessando o wifi na rede
print("Conectando ao WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')

#Processo de espera da conexão do wifi
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Conectado!")

#Conexão ao servidor MQTT
print("Conectando ao servidor MQTT... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()
print("Conectado!")

print("Testando.......... ", end="")

#abertura do arquivo json
with open("dados.json") as f:
    diagram = json.load(f)

#tratamento do arquivo
diagram_str = ujson.dumps(diagram)

#encode para envio a rede MQTT
diagram_bytes = diagram_str.encode('utf-8')




#subscribe funcao

def sub_cb(topic, msg):
    print(f"Received message on topic {topic}: {msg.decode('utf-8')}")
    turn_on_led()
    time.sleep(10)
    turn_off_led()
    time.sleep(10)
    # Trate os dados recebidos conforme necessário
    try:
        data = json.loads(msg)
        # Faça algo com os dados tratados do Node-RED
        print("Dados tratados:", data)
    except ValueError as e:
        print(f"Error decoding JSON: {e}")

print("Connecting to MQTT server out... ", end="")
client2 = MQTTClient(MQTT_CLIENT_ID + "_sub", MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client2.set_callback(sub_cb)  # Configura a função de callback para mensagens recebidas
client2.connect()

client2.subscribe(MQTT_TOPIC_OUT)  # Inscreve-se no tópico MQTT do Node-RED
print(" Connected!")

#envio a rede no tópico MQTT
print("Atualizado!")
print("Reportando ao MQTT : {}".format(MQTT_TOPIC))

while True:
    client.publish(MQTT_TOPIC, diagram_bytes)
    client2.check_msg()


    time.sleep(1)

print("\nLeitura de dados finalizada!")

