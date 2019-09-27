from twilio.rest import Client
import random


def sent_verification_code(number):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC256841cf8eca5f5133c45991d837598a'
    auth_token = '15a1431a2d3f4ca8f859186e65aad860'
    client = Client(account_sid, auth_token)

    code = random.randint(1000, 9999)
    mes = 'Ваш код подтверждения: ' + str(code)

    message = client.messages \
                    .create(
                        body=mes,
                        from_='+12055128793',
                        to=number
                    )
    return code