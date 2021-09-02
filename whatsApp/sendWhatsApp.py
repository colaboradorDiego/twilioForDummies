from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+phone',
    body='mi msg',
    to='whatsapp:+miphone'
)

print(message.sid)
