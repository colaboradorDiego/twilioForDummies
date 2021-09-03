import sys
import os
import json
from twilio.rest import Client


def startApp(conArgs):

    account_sid = conArgs['api']['account']
    auth_token = conArgs['api']['token']
    twilioPhone = conArgs['phones']['twilio']
    diegoPhone = conArgs['phones']['diego']
    messaging_service_sid = conArgs['phones']['messagingService']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="CORTE DE LUZ EN MYH",
        # from_=twilioPhone,
        messaging_service_sid=messaging_service_sid,
        to=diegoPhone
    )
    print(message.sid)


def main(argv):
    parametros = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'twilio.ini'))
    with open(parametros, 'r') as f:
        conArgs = json.load(f)
    startApp(conArgs)


def init():
    if __name__ == '__main__':
        sys.exit(main(sys.argv))

init()
