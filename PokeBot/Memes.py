import discord
from discord.ext import commands   
from discord import client
import pokebase as pb
import sqlite3
import random
import json
with open("pokedex.json") as f:
    filename = json.load(f)
import requests

class Memes:
    
    def __init__(self, bot):
        self.bot = bot
    '''
    @commands.command(pass_context=True)
    async def fuccboi(self, ctx):
        """A wild fuccboi appeared!"""
        em = discord.Embed(title = "Everyone, meet " + str(ctx.message.author) + "'s Fuccboi.", colour = discord.Colour.green())
        em.add_field(name = "ID", value=42069)
        em.add_field(name = "Type(s)", value='Fairy')
        em.add_field(name = "Speed", value=69)
        em.add_field(name = "Attack", value=3)
        em.add_field(name = "Defense", value=19)
        em.add_field(name = "HP", value=111)
        em.add_field(name = "Sp.Atk", value=42)
        em.add_field(name = "Sp.Def", value=2)
        em.set_image(url="https://cdn.discordapp.com/attachments/214577196180701184/399747212965576704/wild_fuccboi.png")
        await self.bot.say(embed = em)
    @commands.command(pass_context=True)
    async def dounodawae(self, ctx):
        """Click click click click click click click"""
        em3 = discord.Embed(title="BRODDA", description="I KNOW DA WAE")
        em3.set_image(url="http://i0.kym-cdn.com/entries/icons/original/000/025/067/ugandanknuck.jpg")
        await self.bot.say(embed = em3)
    @commands.command(pass_context=True)
    async def idonotnodawae(self, ctx):
        """Spit on him!"""
        em4 = discord.Embed(title="oh no", description="You do not no da wae?")
        em4.set_image(url="https://scontent.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/26221780_341922392952260_521252353622409216_n.jpg")
        await self.bot.say(embed = em4)
    @commands.command(pass_context=True)
    async def thetruepath(self,ctx):
        """SHARP TURN!"""
        em = discord.Embed(title="The only worthy exit")
        em.set_image(url="https://i.imgur.com/u5woQs4.png")
        await self.bot.say(embed = em)
    @commands.command(pass_context=True)
    async def say(self, ctx, *, something=None):
        """Coerce the bot to say whatever you want."""
        if something is None:
            await self.bot.say("What do you want to know about Pokemon?")
            await self.bot.delete_message(ctx.message)
        else:
            await self.bot.say(something)
            await self.bot.delete_message(ctx.message)
    
    @commands.group(pass_context=True)
    async def omanyte(self, ctx):
        """The helix god rises!"""
        em1 = discord.Embed(title="Hail the Helix God", description="All Hail!")
        em1.set_image(url="https://cdn.discordapp.com/attachments/399657923732570112/399659505534631945/794.png")
        await self.bot.say(embed = em1)
    @commands.command(pass_context=True)
    async def missingno(self):
        """Glitch"""
        em2 = discord.Embed(title="Missingno", description="Error. Error. Error.")
        em2.set_image(url="https://vignette.wikia.nocookie.net/vsbattles/images/d/d8/MissingNo..png/revision/latest/scale-to-width-down/480?cb=20170302202745")
        await self.bot.say(embed = em2)
    @commands.command(pass_context=True)
    async def blep(self):
        """oh h*ck"""
        emblep = discord.Embed(title="Blep", description="Heckin' Blepped")
        emblep.set_image(url="https://i.redditmedia.com/jDGZNJZLYVb7b8ZPz8opCMC3Gedq9IwPNKEV7sLrzSc.jpg?w=669&s=423abace36b880435408f1fa5e1baa9d")
        await self.bot.say(embed = emblep)
    @commands.command(pass_context=True)
    async def eatdinner(self, ctx):
        """Hungry? I got your favorite dinner."""
        emtide = discord.Embed(title="Your dinner is served, " + str(ctx.message.author) + "!", description="Bone Apple Teeth!")
        emtide.set_image(url="http://cdn.smosh.com/sites/default/files/2018/01/tide-pods-meme-hot-pockets.jpg")
        await self.bot.say(embed = emtide)
    '''
    @commands.command(pass_context=True, aliases=['nl','NL','NicLande','niclande'])
    async def nicLande(self, ctx):
        """No, his name is..."""
        Letters = ['B','C','D','F','G','H','J','K','L','M','N','P','Qu','R','S','T','V','W','X','Y','Z','Th','Ch','Sh','Br','Shm','Shl', 'Tw', 'Shn']  
        First = random.randint(0, len(Letters))
        Last = random.randint(0, len(Letters))
        F = Letters[First]
        L = Letters[Last]
        em = discord.Embed(title="Hey look, it's " + F + "ic " + L + "ande!")
        await self.bot.say(embed = em)
        
        
def setup(bot):
    bot.add_cog(Memes(bot))