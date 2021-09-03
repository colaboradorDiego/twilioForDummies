from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/wasap", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    remitente = request.form.get('From')
    fecha = request.form.get('date_created')
    msgID = request.form.get('sid')


    # Create reply
    resp = MessagingResponse()
    respuesta = "Hola {telefono}, como estas! Tu mensage es: {} y lo mandaste el: {}. El id del msg es: {}".format(remitente,msg,fecha,msgID)
    resp.message(respuesta)

    return str(resp)


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