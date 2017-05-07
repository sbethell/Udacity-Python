from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC0c87692e63cbea74751dd3cc2aeddca6"
# Your Auth Token from twilio.com/console
auth_token  = "c6d91d3053074202b570f4397d5dc9f6"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+12505320540", 
    from_="+15874094518",
    body="I love Sophia Ariana Mayen! She's a babe!!")

print(message.sid)
