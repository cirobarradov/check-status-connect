import os
import requests
import time
import json
try:
    r = requests.get('http://{}:{}/connectors'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT']))    
    connectors=r.json()
    print(connectors)
    for connector in connectors:
    #print(connector)
        status=requests.get('http://{}:{}/connectors/{}/status'.format(os.environ['CONNECT_HOST'],os.environ['CONNECT_PORT'],connector)).json()
        status_json=json.dumps(status)
        print(status_json)
except:
    raise

