import os
import requests
from time import sleep
import json
try:
    while True:
        r = requests.get('http://{}:{}/connectors'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT']))    
        connectors=r.json()
        for connector in connectors:
            status=requests.get('http://{}:{}/connectors/{}/status'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT'],connector)).json()
            config=requests.get('http://{}:{}/connectors/{}'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT'],connector)).json()
            status['config']=config
            status_json=json.dumps(status)
            print(status_json)
        sleep(int(os.environ['SLEEP_TIME']))
except:
    raise
