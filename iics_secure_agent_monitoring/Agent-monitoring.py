import requests
import json
import configparser
import time
import os
import logging
from requests.exceptions import HTTPError

#Logging for Agent monitoring

log_month = time.strftime("%Y%m")
logdir = 'E:\\Python-Lecture\\'
logfile = logdir + 'agent_monitoring_log.' + log_month      # Log File Name: agent_monitoring_log.201911
logging.basicConfig(filename=logfile,format="%(asctime)-15s [%(levelname)s]: %(message)s",level=logging.DEBUG)

parser = configparser.ConfigParser()

try:
    cfgfile = 'E:\\Python-Lecture\\agent_monitoring_cfg'
    parser.read(cfgfile)
except configparser.Error as err:
    logging.error("There is issue with CFG File")
    raise ValueError('CFG File is not a valid', err)

# Function to connect With API


def connection_with_api(url, payload, header):
    try:
        response = requests.post(url, payload, headers=header)
        #print (response.status_code)
        #print (response.text)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6

    return response.text

def get_agent_details(url, header):
    try:
        res = requests.get(url,headers=header)
        print (res.status_code)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6

    return json.loads(res.text)


# read iPaaS API url
if (parser.has_option('API-options', 'url')):
    url=parser.get('API-options', 'url')
else:
    logging.error("No Url Found for monitoring script in cfg file")
    exit(1)

# read iPaaS username to autheticate

if (parser.has_option('API-options', 'username')):
    user=parser.get('API-options', 'username')
else:
    logging.error("No UserName Found for monitoring script in cfg file")
    exit(1)

# read password to authenticate

if (parser.has_option('API-options', 'password')):
    pass_user=parser.get('API-options', 'password')
else:
    logging.error("No Password Found for monitoring script in cfg file")
    exit(1)

# read email id to send mail in case agent is not running

if (parser.has_option('API-options','emailid')):
    recipient=parser.get('API-options','emailid')
else:
    logging.error("No email Found for sending mail in cfg file")
    exit(1)

print (url + "\n" + user + "\n" + pass_user + "\n" + recipient)


# Call function to connect with API and create header and payload to make post call

header = {'Content-Type':'application/json'}
payload = json.dumps({"@type": "login","username": user,"password": pass_user})

#Call function
#connection_with_api(url, payload, header)

data = json.loads(connection_with_api(url, payload, header))
icSessionID=data['icSessionId']
serverUrl=data['serverUrl']
print(serverUrl)
print(icSessionID)

#Call Function to get Agent details using Cloud API

api_header = {'Content-Type' : 'application/json','icSessionId': icSessionID}
api_url = serverUrl + '/api/v2/agent/details/<agentID>'

aget_data = get_agent_details(api_url,api_header)

#Services Status of secure agent

admin_server_status = aget_data['agentEngines'][0]['agentEngineStatus']['status']
integration_server_status = aget_data['agentEngines'][1]['agentEngineStatus']['status']
process_system_status = aget_data['agentEngines'][2]['agentEngineStatus']['status']

print (aget_data['agentEngines'][1]['agentEngineStatus']['appname'] + " :- " + integration_server_status)
print (aget_data['agentEngines'][2]['agentEngineStatus']['appname'] + " :- " + process_system_status)
print (aget_data['agentEngines'][0]['agentEngineStatus']['appname'] + " :- " + admin_server_status)
