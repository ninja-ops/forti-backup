#!/bin/bash

export FORTI_APPLIANCE='127.0.0.1:443'
export FORTI_TOKEN='1fNp5ff7z0q34bsrg8Qxm96pHdNyaf'

./backup-fortinet-appliance.py ./ && echo DONE || echo ERROR
