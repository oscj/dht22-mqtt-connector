#!/usr/bin/python3

import sys,os
sys.path.append(os.getcwd())
import dht22_sensor_readings as dht22
import time

def fetch_readings_every_2_seconds():
  while(True):
    try:
      temp = dht22.fetch_temperature()
      humidity = dht22.fetch_humidity()
      print("Temperature: {}°C, Humidity: {}%".format(temp, humidity))
      time.sleep(2)
    except Exception as e:
      continue

if __name__ == "__main__":
  fetch_readings_every_2_seconds()
