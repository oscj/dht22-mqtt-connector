import adafruit_dht
from board import D22
import time 
import logging

dht_device = adafruit_dht.DHT22(D22)

def fetch_humidity():
  try:
    humidity = dht_device.humidity
    return humidity
  except Exception as e:
    logging.error(e) 
    raise e

def fetch_temperature():
  try:
    temperature = dht_device.temperature
    return temperature
  except Exception as e:
    logging.error(e)
    raise e

# test
if __name__ == "__main__":
  while(True):
    try:
      temperature = dht_device.temperature
      humidity = dht_device.humidity

      print(temperature, humidity)
      time.sleep(2) 
    except Exception as e:
      print(e)
