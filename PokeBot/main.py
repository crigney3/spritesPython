
import discord
from discord.ext import commands   
from discord import client
import pokebase as pb
import sqlite3
import random
import json
with open("pokedex.json") as f:
    filename = json.load(f)
with open("secrets.json") as s:
    secrets = json.load(s)
import requests


bot = commands.Bot(command_prefix='/', description='The PokeBot')
client = discord.Client()
token = secrets[0]

sqlite_file = 'pokemon_storage.sqlite'
table_name1 = 'pokemonStorage'  
new_field = 'user1' 
field_type = 'STRING'
column_name = "Name"
column_health = "Health"
column_defense = "Defense"
column_attack = "Attack"
column_special_defense = "SpecialDefense"
column_special_attack = "SpecialAttack"
column_speed = "Speed"
column_level = "Level"
column_experience = "XP"
column_type_text = "TEXT"
column_type_int = "INTEGER"

sqlite_items = 'item_storage.sqlite'
table_name2 = 'itemStorage'
new_field = 'user1'

column_ulevel = "Level"
column_uexperience = "XP"
column_pball = 'Pokeballs'
column_gball = 'GreatBalls'
column_uball = 'UltraBalls'
  

#Remember to use conn.close(), and use conn.commit()

def pbase():
    try:
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=new_field, ft=field_type))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=column_name, ct=column_type_text))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=column_health, ct=column_type_int))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=column_defense, ct=column_type_int))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=column_attack, ct=column_type_int))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=column_special_defense, ct=column_type_int))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=column_special_attack, ct=column_type_int))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=column_speed, ct=column_type_int))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=column_level, ct=column_type_int))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=column_experience, ct=column_type_int))
        c.execute("INSERT INTO {tn} ({idf}) VALUES ('{cuUs}')".\
        format(tn=table_name1, idf=column_name, cuUs="test"))
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        print("The pokemon database has already been created.")   
def itemb():
    try:
        conn = sqlite3.connect(sqlite_items)
        c = conn.cursor()
        c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name2, nf=new_field, ft=field_type))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=column_name, ct=column_type_text))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=column_ulevel, ct=column_type_int))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=column_pball, ct=column_type_int))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=column_gball, ct=column_type_int))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=column_uball, ct=column_type_int))
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=column_uexperience, ct=column_type_int))
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        print("The item database has already been created.") 
    
        #print("The item database has already been created.") 
class Main:
    @bot.event
    async def on_member_join(self,member):
        msg = str('Welcome to Rochester\'s Finest, <@!' + str(member.id) + '>! Please read <#458113475609231384> and say hello here!')
        channel = member.server.get_channel('448845960794210307')
        print(channel)
        await bot.send_message(channel,msg)
    @bot.event
    async def on_ready(self):
        bot.load_extension("Memes")
        bot.load_extension("Test")
        bot.load_extension("Pokemon")
        bot.load_extension("Beenado")
        print('Logged in as')
        print(bot.user.name)
        pbase();
        itemb();
    
    
bot.add_cog(Main())
bot.run(token)    

