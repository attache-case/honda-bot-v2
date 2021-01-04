import discord
import logging

from app.controllers.conversation import process_message

import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = discord.Client()

active_ch = None


@client.event
async def on_ready():
    global active_ch
    print('Logged in as...')
    print('user name: ' + client.user.name)
    print('user id: ' + str(client.user.id))
    print('------')
    # find channel to respond
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.name == settings.active_channel_name:
                active_ch = channel
    if active_ch != None:
        pass


@client.event
async def on_message(message):
    # logger.info(
    #     f'action=on_message author={message.author}, channel={message.channel}, message={message.content}')
    if client.user == message.author:
        return
    if active_ch == None or message.channel != active_ch:
        return

    await process_message(message)

if __name__ == '__main__':
    client.run(settings.discord_access_token)
