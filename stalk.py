#!/usr/bin/python3

import discord
import requests
import secrets

class StalkBot(discord.Client):

    err_string = ("Invalid command!\n" "Available commands:"
                        "\n\tprice <stalk price> <am/pm>"
                        "\n\tpredict")

    async def on_message(self, message):
        # ignore if bot post
        if message.author == self.user: return

        command = message.content.split(' ')

        # verify if command
        if command[0] != '!stalk':
            return

        # verify command present
        try:
            cmd_type = command[1]
        except:
            await message.channel.send(self.err_string)
            return

        # handle command
        if cmd_type == 'price':
            await self.price(message, command[2:])
        elif cmd_type == 'predict':
            await self.predict(message)
        else:
            await message.channel.send(self.err_string)
            return
                 
    async def price(self, message, command):
        try:
            price = command[0]
            am_or_pm = command[1]
        except:
            await message.channel.send(self.err_string)
            return

        user = message.author

        # verify command input
        if not price.isnumeric() or not isinstance(am_or_pm, str) or \
                                    not (am_or_pm == 'am' or am_or_pm == 'pm'):
            await message.channel.send(('Invalid price command;\n' 
                                        'Example use: !stalk price <cost as integer> <string am or pm>'))
            return

        # TODO
        # for user
            # store price for current day as am/pm
            # in db

    async def predict(self, message):
        # TODO
        # for user
            # retrieve current week prices so far from database
            # use Turnip Calculator to get current prediction
        # r = requests.get('https://api.ac-turnip.com/data/?f=-129-93-160-193-168-46')
        # print(r.json())
        print('a lot or nothing')

if __name__ == "__main__":
    bot = StalkBot()
    bot.run(secrets.A_TOKEN)