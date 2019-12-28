# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:59:23 2019

@author: anuja
"""
#346548299291033600
# MzQ2NTQ4Mjk5MjkxMDMzNjAw.XOzUtw.s1WEW7uJQzD7pT6s2ibzMAcMT2Y
#75840
# bot2 token NTgyODM2NzM2ODI0OTY3MTY5.XOznHA.gWtO3I8rQu98bu6L6x1tcC3L9kc
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")
@client.event
async def on_ready():
    print('Logged on as')
#
#    async def on_message(self, message):
#        # don't respond to ourselves
#        if message.author == self.user:
#            return
#
#        if message.content == 'ping':
#            await message.channel.send('pong')


client.run(')
