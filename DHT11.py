import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 25

while True:
    hum, temp = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if hum is not None and temp is not None:
        print("Temp={0:0.1f}C Humidity={1:0.01f}%".format(temp, hum))
    time.sleep(2)