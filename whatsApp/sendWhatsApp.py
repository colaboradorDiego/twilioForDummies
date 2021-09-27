import sys
import os
import json
from twilio.rest import Client


def enviarMensage(client, recipient_number, recipient_name, myPhone):
    mensaje = """
        Hola {}, este es un msg de binvenida.
        Que tengas un excelente dia.
        Nos vemos pronto.""".format(recipient_name)

    try:
        message = client.messages.create(
            body=mensaje,
            from_='whatsapp:' + myPhone,
            to='whatsapp:' + recipient_number
        )

        print("Mensaje id:", message.sid, "enviado a:", recipient_name, "al WhatsApp:", recipient_number)
        return True

    except Exception as e:
        print("Something went wrong. Message not sent.")
        print(repr(e))
        return False


def startApp(conArgs):
    account_sid = conArgs['api']['account']
    auth_token = conArgs['api']['token']
    twilioPhone = conArgs['wasap']['twilio']
    diegoPhone = conArgs['wasap']['diego']

    client = Client(account_sid, auth_token)

    enviarMensage(client, diegoPhone, "Diego", twilioPhone)


def main(argv):
    parametros = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'twilio.ini'))
    with open(parametros, 'r') as f:
        conArgs = json.load(f)
    startApp(conArgs)


def init():
    if __name__ == '__main__':
        sys.exit(main(sys.argv))


init()
