#!/usr/bin/env python3
import os, sys, requests
from datetime import datetime

if sys.argv[1:]:
  target_path = sys.argv[1]
else:
  target_path = './'

appliance = os.environ.get('FORTI_APPLIANCE')
if (appliance == None):
  print('FORTI_APPLIANCE not defined')
  exit(1)

token = os.environ.get('FORTI_TOKEN')
if (token == None):
  print('FORTI_TOKEN not defined')
  exit(1)

product = 'fortinet'
if (os.environ.get('FORTI_PRODUCT') != None):
  product = os.environ.get('FORTI_PRODUCT')

scope = 'global'
if (os.environ.get('FORTI_SCOPE') != None):
  scope = os.environ.get('FORTI_SCOPE')

url = 'https://' + appliance + '/api/v2/monitor/system/config/backup?scope=' + scope + '&access_token=' + token

requests.packages.urllib3.disable_warnings()

try:
  req = requests.get(url, verify = False, timeout = 5)
except Exception as e:
  print(e)
  exit(1)

if (req.status_code != 200):
  print('API Error', req.status_code)
  exit(1)

filename = target_path + datetime.now().strftime('%Y_%m_%d-%H_%M_%S') + '-backup-' + product + '-' + appliance + '.conf'

with open(filename, 'wb') as f:
  for line in req:
    f.write(line)
