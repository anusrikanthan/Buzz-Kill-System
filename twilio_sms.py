# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC0d982082455eff6334adaba25a77d04f'
auth_token = '3b3e2361f7fdb0ac94e4ba9d9fe30d56'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+17738773065',
         to='+918056054049'
     )

print(message)