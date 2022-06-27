#!/bin/bash

pip install twilio
pip install gps
pip install picamera
pip install tensorflow
pip install numpy
pip install matplotlib
pip install opencv-contrib-python
pip install keras
pip install pillow
echo "Input email: "
read email
export email=$email

echo "Input email password: "
read email_password
export email_password=$email_password

echo "Input twillio sid: "
read twillio_sid
export twillio_sid=$twillio_sid

echo "Input twillio auth token: "
read twillio_auth_token
export twillio_auth_token=$twillio_auth_token

echo "Input phone number: "
read phone
export phone=$phone

echo "Input twillio messaging service sid: "
read messaging_service_sid
export messaging_service_sid=$messaging_service_sid
