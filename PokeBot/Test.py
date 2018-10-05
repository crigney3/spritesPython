import discord
from discord.ext import commands   
from discord import client
import pokebase as pb
import sqlite3
import random
import urllib3
from bs4 import BeautifulSoup
import json
with open("pokedex.json") as f:
    filename = json.load(f)
import requests

sqlite_file = 'testdb.sqlite'
table_name = 'users'  
new_field = 'userList' 
field_type = 'STRING' 
id_column = "The_first_column"
column_type = 'TEXT'

class Test:
    currentUser = None
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self):
        """pong!"""
        await self.bot.say('pong!')
    @commands.command()
    async def scrape(self):
        """please don't use this command."""
        bulb = "https://bulbapedia.bulbagarden.net/wiki/Kanto_Route_1"
        http = urllib3.PoolManager()
        response = http.request('GET', bulb)
        soup = BeautifulSoup(response.data, 'html.parser')
        chance = soup.find_all('td')[0].get_text()
        print(chance.encode("utf-8"))
        
    '''
    @commands.command(pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def getUser(self, ctx):       
        await self.bot.say("Attempting to add user" + str(ctx.message.author) + " to database...")
        currentUser = str(ctx.message.author)
        try:
            conn = sqlite3.connect(sqlite_file)
            c = conn.cursor()
            c.execute('CREATE TABLE {tn} ({nf} {ft})'\
            .format(tn=table_name, nf=new_field, ft=field_type))
            c.execute("ALTER TABLE {tn} ADD COLUMN '{idf}' {ct}"\
            .format(tn=table_name, idf=id_column, ct=column_type))
            c.execute("INSERT INTO {tn} ({nf}, {idf}) VALUES ({vl}, '{cuUs}')".\
                format(tn=table_name, nf=new_field, idf=id_column, cuUs=currentUser, vl="Test"))
            conn.commit()
            conn.close()
        except sqlite3.OperationalError:
            print("The database has already been created.")  
            conn = sqlite3.connect(sqlite_file)
            c = conn.cursor() 
            c.execute("INSERT INTO {tn} ({idf}) VALUES ('{cuUs}')".\
                format(tn=table_name, idf=id_column, cuUs=currentUser))
            conn.commit()
            conn.close()
    @getUser.error #if you want the same cooldown message for all commands, define an on_command_error(err, ctx) event instead
    async def getUser_error(self, err, ctx):
        if isinstance(err, commands.CommandOnCooldown):
            await self.bot.say(err)
    
    
    @commands.command(pass_context=True)
    async def getUser2(self, ctx):
        currentUser = str(ctx.message.author)
        conn = sqlite3.connect(sqlite_file)
        
        c = conn.cursor() 
        c.execute("INSERT INTO {tn} ({idf}, {idf2}) VALUES ('{cuUs}', {var1})".\
            format(tn=table_name, idf=id_column, cuUs=currentUser, idf2="Extra", var1="1"))
        conn.commit()
        conn.close()
        
    '''     
            
        
def setup(bot):
    bot.add_cog(Test(bot))