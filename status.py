import os
import requests
import time
import json
try:
    while True:
        r = requests.get('http://{}:{}/connectors'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT']))    
        connectors=r.json()
        for connector in connectors:
            status=requests.get('http://{}:{}/connectors/{}/status'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT'],connector)).json()
            status_json=json.dumps(status)
            print(status_json)
        sleep(os.environ['SLEEP_TIME'])
except:
    raise

