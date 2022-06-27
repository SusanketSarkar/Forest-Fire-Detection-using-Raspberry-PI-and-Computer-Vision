from datetime import datetime
import smtplib
import os
from re import split
from log_handler import open_log_file, close_log_file
from twilio.rest import Client


def get_recievers():

    # code to get recievers based on provided dataset

    # returning dummy data temporarily
    return {'email':[os.environ['email']], 'phone':[os.environ['phone']]}


def send_email(sender, email_password, receivers, warning_level, message, automation_alert):

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, password=email_password)

    if warning_level == 0:
        server.sendmail(sender, receivers, message['emergency']+automation_alert)
    elif warning_level == 2:
        server.sendmail(sender, receivers, message['alert']+automation_alert)

    return


def send_message(tw_account_sid, tw_auth_token, receivers, warning_level, message, automation_alert):

    client = Client(tw_account_sid, tw_auth_token)

    for receiver in receivers:
        if warning_level == 0:
            tw_message = client.messages.create(
                    to=receiver,
                    messaging_service_sid=os.environ['messaging_service_sid'],
                    body=message['emergency']+automation_alert)
        elif warning_level == 2:
            tw_message = client.messages.create(
                    to=receiver,
                    messaging_service_sid=os.environ['messaging_service_sid'],
                    body=message['alert']+automation_alert)

    return


def get_link(lat, lon):
    # get google maps link using lat and lon
    return f"http://www.google.com/maps/place/{lat},{lon}"


def send_email_message(lat_lon, receivers, warning_level):

    lat, lon = lat_lon[0], lat_lon[1]
    maps_link = get_link(lat, lon)

    message = {'alert' : f"Fire Alert: \nSmoke has been detected at \nLat: {lat} \nLon: {lon} \nPlease take neccessary actions. \nLocation: {maps_link}",
                'emergency': f"Emergency \nFire loacated at: \nLat: {lat} \nLon: {lon} \nPlease take immidiate actions. \nLocation: {maps_link}"
                }

    automation_alert = "\n\nThis is an auto-generated message. Please do not reply."

    old_stdout, log_file = open_log_file("email_message")

    if warning_level == 1: return

    try:
        sender  = os.environ['email']
        email_password  = os.environ['email_password']
        send_email(sender=sender,
                    email_password=email_password,
                    receivers=receivers['email'],
                    warning_level=warning_level,
                    message=message,
                    automation_alert=automation_alert)
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+":")
        print(f"\tMail Sent to {receivers['email']} with warning level {warning_level}.")

    except Exception as e:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+":")
        print("\tUnable to send mail because of error", e)

    try:
        tw_account_sid = os.environ['twillio_sid']
        tw_auth_token  = os.environ['twillio_auth_token']
        send_message(tw_account_sid=tw_account_sid,
                    tw_auth_token=tw_auth_token,
                    receivers=receivers['phone'],
                    warning_level=warning_level,
                    message=message,
                    automation_alert=automation_alert)
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+":")
        print(f"\tMessage Sent to {receivers['phone']} with warning level {warning_level}.")

    except Exception as e:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+":")
        print("\tUnable to send message because of error", e, end=" ")
        print(" ".join( split("\n", str(e)) ))
        print()

    close_log_file(old_stdout, log_file)


if __name__=="__main__":
    recv=get_recievers()
    print("Testing: ")
    send_email_message(lat_lon=[45,45], receivers=recv, warning_level=2)