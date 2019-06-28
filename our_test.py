// take attention values into consideration only if its above 0
from NeuroPy import NeuroPy
import time 
import win32gui
from twilio.rest import Client

account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxx'          // Change twilio account details to your own 
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

print("1")
ob = NeuroPy("COM26")
print("2")

ob.start()
print("3")



# count=0
# flag=1
# lastAttention = 0
while(True):
    if(ob.attention > 0)and(ob.attention < 50):                     // Sending alert if attention levels go below a certain level.
        message = client.messages.create(
            body='Attention levels loww !'+str(ob.attention),
            from_='+17738773065',
            to='+918056054049'
        )
        time.sleep(3)

    # print(message)
    print(ob.attention, "  -attention strength")
    # print(ob.attention)
    print(ob.highAlpha)       
ob.stop()
ob.save()
