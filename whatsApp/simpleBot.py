import os
import json
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd
from datetime import datetime


app = Flask(__name__)

account_sid = ''
auth_token = ''
twilioPhone = ''
diegoPhone = ''
client = False

parametros = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'twilio.ini'))
with open(parametros, 'r') as f:
    conArgs = json.load(f)

    account_sid = conArgs['api']['account']
    auth_token = conArgs['api']['token']
    twilioPhone = conArgs['wasap']['twilio']
    diegoPhone = conArgs['wasap']['diego']

    client = Client(account_sid, auth_token)


@app.route("/wasap", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    remitente = request.form.get('From')

    # todo los siguientes dos no me funcionan
    fecha = request.form.get('date_created')
    msgID = request.form.get('sid')


    # Create reply
    resp = MessagingResponse()
    respuesta = "Hola {}, como estas! Tu mensage es: {} y lo mandaste el: {}. El id del msg es: {}".format(remitente, msg, fecha, msgID)
    resp.message(respuesta)

    return str(resp)


def enviarMensage(client, recipient_number, recipient_name, myPhone):
    mensaje = """
        Hola {}, Este es un msg de binvenida.
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


def createDataframe():
    try:
        dateparse = lambda x: datetime.strptime(x, "%d-%m-%Y")
        conjuntoDeDatos = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'twilio.ini'))
        df = pd.read_csv(
            conjuntoDeDatos,
            dtype=str,
            parse_dates=['Vencimiento'],
            date_parser=dateparse
        )
        print(df)
        return df

    except Exception as e:
        print("Something went wrong. Dataframe not created.")
        print(repr(e))
        return False


def checkForMatchs():
    try:
        matchDf = createDataframe()
        matchDf["day"] = matchDf["Vencimiento"].dt.day
        matchDf["month"] = matchDf["Vencimiento"].dt.month
        today = datetime.now()
        for i in range(matchDf.shape[0]):
            matchDfDay = matchDf.loc[i, "day"]
            matchDfMonth = matchDf.loc[i, "month"]
            if today.day == matchDfDay and today.month == matchDfMonth:
                enviarMensage(client, matchDf.loc[i, "Numero WhatsApp"], matchDf.loc[i, "Nombre"], twilioPhone)
        return True

    except Exception as e:
        print("Something went wrong. Birthday check not successful.")
        print(repr(e))
        return False


scheduler = BackgroundScheduler()
tarea = scheduler.add_job(checkForMatchs, 'cron', day_of_week ='mon-sun', hour=0, minute=1)
scheduler.start()


if __name__ == "__main__":
    app.run(debug=True)


"""
request
from twilio.rest import Client 

account_sid = '[accountID]' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 

message = client.messages.create( 
                              from_='whatsapp:+phone',  
                              body='Hola! Bienvenido al sandbox',      
                              to='whatsapp:+phone' 
                          ) 

print(message.sid)

response 
{
    "sid": "id",
    "date_created": "Fri, 03 Sep 2021 14:32:43 +0000",
    "date_updated": "Fri, 03 Sep 2021 14:32:43 +0000",
    "date_sent": null,
    "account_sid": "id",
    "to": "whatsapp:+phone",
    "from": "whatsapp:+phone",
    "messaging_service_sid": null,
    "body": "Hola! Bienvenido al sandbox",
    "status": "queued",
    "num_segments": "1",
    "num_media": "0",
    "direction": "outbound-api",
    "api_version": "2010-04-01",
    "price": null,
    "price_unit": null,
    "error_code": null,
    "error_message": null,
    "uri": "/2010-04-01/Accounts/xxx/Messages/yy.json",
    "subresource_uris": {
        "media": "/2010-04-01/Accounts/xxx/Messages/yy/Media.json"
    }
}

"""