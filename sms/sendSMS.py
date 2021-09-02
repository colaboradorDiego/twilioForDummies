from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="mi msg",
    from_='+phone',
    to='+myPhone'
)

print(message.sid)

