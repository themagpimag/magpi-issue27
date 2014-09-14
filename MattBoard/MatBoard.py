#!/usr/bin/python
#
# Note: you need to change lines 28,29 & 30

import RPi.GPIO as GPIO, feedparser
from time import sleep
import smtplib , os, sys
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Set up GPIO Inputs
#Yellow Input
GPIO.setup(7, GPIO.IN)
#Orange LED
GPIO.setup(12, GPIO.OUT)

#Set LEDs to Off and outputs to False
GPIO.output(12,False)

Yellow_Status = 0
Red_Status = 0

def send_email(msg):
    USERNAME = "yourgoogleemailid@gmail.com" # change this to your ID
    PASSWORD = "yourgoogleemaipassword"      # change this to your password
    MAILTO  = "someone@example.com"          # change this to the recipient

    msg['From'] = USERNAME
    msg['To'] = MAILTO

    msg.attach(MIMEImage(file( "/home/pi/magpi/water.jpg" ).read()))

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME, MAILTO, msg.as_string())
    server.quit()

    print"email sent to:" + MAILTO
    return

def Send_nowater_email():
    print"No water"
    msg = MIMEMultipart()
    msg.attach(MIMEText('Water Butt Empty'))
    msg['Subject'] = 'Water Butt Empty'
    send_email(msg)
    return

def Send_watered_email():
    print"sending image"
    msg = MIMEMultipart()
    msg.attach(MIMEText('Greenhouse watered'))
    msg['Subject'] = 'Greenhouse Watered'
    send_email(msg)
    return

def water_plants():
    GPIO.output(12,True)
    sleep(3)
    GPIO.output(12,False)
    return

def take_picture():
    os.system("raspistill -o /home/pi/magpi/water.jpg -w 1024 -h 768 -q 30")

while True:
    Input_yellow = GPIO.input(7)
    print Input_yellow

    if Input_yellow == False:
        water_plants()
        take_picture()
        Send_watered_email()

        print"wait 30 seconds"
        sleep(30)
        print"exit program"
        sys.exit()

    if Input_yellow == True:
        take_picture()
        Send_nowater_email()
        sys.exit()
