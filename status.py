import os
import requests
import uuid
from datetime import datetime

from time import sleep
import json

try:
    while True:
        r = requests.get('http://{}:{}/connectors'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT']))    
        request_id=str(uuid.uuid1())
        connectors=r.json()
        for connector in connectors:
            request_timestamp=str(datetime.now())
            status=requests.get('http://{}:{}/connectors/{}/status'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT'],connector)).json()
            config=requests.get('http://{}:{}/connectors/{}'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT'],connector)).json()['config']
            status['config']=config
            status['state']=status.get('connector').get('state')
            status['request_id']=request_id
            status['request_timestamp']=request_timestamp
            status_json=json.dumps(status)           
            print(status_json)
        sleep(int(os.environ['SLEEP_TIME']))
except:
    raise
