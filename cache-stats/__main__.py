from . import Config
from . import StatsCollector
import paho.mqtt.client as mqtt
import time
import json

def main():
    config_file = 'config.yml'
    config = Config(config_file)


    mqtt_config = config.get_mqtt()
    mq = mqtt.Client()
    mq.connect(mqtt_config['host'])
    mq.on_log = log

    collector = StatsCollector()
    while(True):
        for device in config.get_devices():
            data = collector.collect(device['device'])
            data['device'] = device['device']
            data['device_alias'] = device['device_alias']
            print(data)
            mq.publish(device['target_topic'], json.dumps(data))
        
        time.sleep(30)

    
def log(self, client, userdata, level, buf):
    if level >= MQTT_LOG_INFO:
        print(buf)


if __name__ == '__main__':
    main()
