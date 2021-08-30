#!/usr/bin/python3

import adafruit_dht
from board import D22
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

