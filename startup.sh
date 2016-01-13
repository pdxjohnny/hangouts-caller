#!/bin/bash

touch ~/.Xauthority
pip install --user -r requirements.txt
/usr/bin/firefox \
  'https://accounts.google.com/ServiceLogin?continue=https://hangouts.google.com' &
sleep 10
python call.py $ACCOUNT $PASSWORD $NUMBER
