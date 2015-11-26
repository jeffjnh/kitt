import cleverbot
import discord
import time

kit = cleverbot.Cleverbot()
client = discord.Client()
client.login('kitthediscordbot@gmail.com','transam82')

if client.is_logged_in:
    print ('Logged into discord woo!')



@client.event
def on_message(message):
    print ('EVENT: ')
    print (message.content)
    if message.content.startswith('kitt'):
        response = kit.ask(message.content[5:])
        time.sleep(2)
        client.send_message(message.channel,'paxbot ' + response, False, True)

@client.event
def on_ready():
    print ('ready to go pew pew')


client.run()