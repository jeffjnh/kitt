import cleverbot
import discord
import time
import image
import weather

kit = cleverbot.Cleverbot()
client = discord.Client()
client.login('kitthediscordbot@gmail.com','transam82')

if client.is_logged_in:
    print ('Logged into discord woo!')

def cleverResponse(message):
    response = kit.ask(message.content[5:])
    time.sleep(2)
    client.send_message(message.channel,'paxbot ' + response, False, True)
    
def img(content):
    return image.image(content)
    
def wthr(content):
    return weather.weather(content)

@client.event
def on_message(message):
    #match = re.findall(r"kitt image (.*)", message.content)
    print ('EVENT: ')
    print (message)
    print (message.content)
    if message.content.startswith('kitt'):
        cleverResponse(message)
    elif message.content.startswith('!image'):
        client.send_message(message.channel,img(message.content[7:]))
    elif message.content.startswith('!weather'):
        client.send_message(message.channel,wthr(message.content[9:]))
        

@client.event
def on_ready():
    print ('ready to go pew pew')


client.run()