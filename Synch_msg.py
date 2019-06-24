import time
from sinchsms import SinchSMS

number = '+8883045000'
message = 'I am Vishnu'

client = SinchSMS("961f8bd4-9a3c-46dc-a7d3-f22153949cde", "0M4ebrmr1kiFGm8UYLBC6w==")

print("Sending '%s' to %s" % (message, number))
response = client.send_message(number, message)
message_id = response['messageId']

response = client.check_status(message_id)
while response['status'] != 'Successful':
    print(response['status'])
    time.sleep(1)
    response = client.check_status(message_id)
    print(response['status'])