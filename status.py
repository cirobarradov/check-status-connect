import os
import requests
import uuid

from time import sleep
import json

try:
    while True:
        r = requests.get('http://{}:{}/connectors'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT']))    
        request_id=uuid.uuid1()
        connectors=r.json()
        for connector in connectors:
            status=requests.get('http://{}:{}/connectors/{}/status'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT'],connector)).json()
            config=requests.get('http://{}:{}/connectors/{}'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT'],connector)).json()['config']
            status['config']=config
            status['state']=status.get('connector').get('state')
            status['request_id']=request_id
            status_json=json.dumps(status)           
            print(status_json)
        sleep(int(os.environ['SLEEP_TIME']))
except:
    raise
