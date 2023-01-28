import discord;
from discord.ext import commands;
import libs.RestauranteUniversitario as RU;
import libs.Music as M;



client = commands.Bot(intents=discord.Intents.all(), command_prefix='#');



@client.event
async def on_ready():
    await client.add_cog(RU.RestauranteUniversitario())
    await client.add_cog(M.Music())
    print(f'Logado com sucesso como {client.user}');


@client.event
async def on_message(message):
    await client.process_commands(message);
    if 'logar' in message.content and not(message.author.bot):
        await message.delete();
    if message.author == client.user:
        return;
    



client.run('');
