import sys
import os
import json
from twilio.rest import Client

def startApp(conArgs):

    account_sid = conArgs['api']['account']
    auth_token = conArgs['api']['token']
    twilioPhone = conArgs['wasap']['twilio']
    diegoPhone = conArgs['wasap']['diego']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Me presento soy el bot de MYH!",
        from_='whatsapp:' + twilioPhone,
        to='whatsapp:' + diegoPhone
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
