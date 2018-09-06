from twilio.rest import Client

account_sid = "AC55c20707981d8098c4d6014ec509f06a"
auth_token = "2f509fafb2abd6203dcc227e8456b61c"

client = Client(account_sid, auth_token)


message = client.messages.create(to="+8613126830206",
                                from_='+15017122661',
                                body="Do you know who I am ?"
                                )

