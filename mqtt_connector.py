#!/usr/bin/python3

import paho.mqtt.client as mqtt
import dht22_sensor_readings as dht22
import logging
import time
import json
import os
import random
from dotenv import load_dotenv
from typing import Any, Dict

load_dotenv()
BROKER_ADDRESS = os.environ.get('BROKER_ADDRESS')
BROKER_PORT = os.environ.get('BROKER_PORT')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_PSSWD = os.environ.get('CLIENT_PSSWD')


def main():
    logging.basicConfig(
        filename='logs/application.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    mqtt_client = mqtt.Client(client_id=CLIENT_ID, clean_session=False)
    mqtt_client.username_pw_set(CLIENT_ID, CLIENT_PSSWD)
    mqtt_client.max_queued_messages_set(0)
    mqtt_client.connect(BROKER_ADDRESS, int(BROKER_PORT))
    mqtt_client.on_connect = on_connect
    mqtt_client.on_disconnect = on_disconnect
    periodically_publish_dht22_data(mqtt_client)
    mqtt_client.loop_forever()


def on_disconnect(client: mqtt.Client, userdata: Any, flags: Dict, rc: int) -> None:
    logging.warning("MQTT Client Disconnecting...")


def on_connect(client: mqtt.Client, userdata: Any, flags: Dict, rc: int) -> None:
    logging.debug('{}  MQTT Client Connected to {}  {}'.format(
        "#" * 30, BROKER_ADDRESS, "#" * 30))
    logging.debug('Client connected with flags: {}'.format(flags))
    logging.debug('Client connected with return code: {}'.format(rc))



def periodically_publish_dht22_data(client: mqtt.Client) -> None:
    while(True):
        try:
            res = {
                'temp': dht22.fetch_temperature(),
                'humidity': dht22.fetch_humidity()
            }
            client.publish('sensor/{}'.format(CLIENT_ID), json.dumps(res))
            print('sensor/{}'.format(CLIENT_ID))
            logging.info('Published Data: ')
            logging.info(json.dumps(res)) 
            time.sleep(2)
        except Exception as e:
            logging.error(e)
            continue

if __name__ == '__main__':
    main()
