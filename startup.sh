#!/bin/bash

touch ~/.Xauthority
pip install --user -r requirements.txt
./contact-call-center.py
