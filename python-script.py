# Install request module by running ->
#  pip3 install requests

# Replace the deviceToken key with the device Token for which you want to send push notification.
# Replace serverToken key with your serverKey from Firebase Console

# Run script by ->
# python3 fcm_python.py


import requests
import json

serverToken = '//get firebase server token from your firebase project'


deviceToken = '//get device token'

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
      }

body = {
          'notification': {'title': 'Ntegeka is cool',
                            'body': 'Ntegeka is Smart'
                            },
          'to':
              deviceToken,
          'priority': 'high',
        #   'data': dataPayLoad,
        }
response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
print(response.status_code)

print(response.json())