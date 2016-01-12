#!/bin/bash

touch ~/.Xauthority
pip install --user -r requirements.txt
/usr/bin/firefox https://hangouts.google.com &
sleep 20
python call.py
