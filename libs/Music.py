import discord;
from discord.ext import commands;
import youtube_dl
import asyncio

playlist = [];

class Music(commands.Cog):
    
    @commands.command(name='add', description='#play url')
    async def add(self, ctx, url:str):
        playlist.append(str(url));
    
    
    @commands.command(name='queue', description='queue')
    async def queue(self, ctx):
        global current_song,vc;
        pl = '';
        for music in playlist:
            pl += '\n' + music;
        await ctx.channel.send(pl);
        
    @commands.command(name='play' , description='#play')
    async def play(self, ctx):
        global current_song,vc
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        voice_channel = ctx.author.voice.channel
        vc = await voice_channel.connect()

        # Iterate through the list of URLs
        for url in playlist:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                song = info['formats'][0]['url']
                current_song = song;
            vc.play(discord.FFmpegPCMAudio(song), after=lambda e: print('done', e))
            vc.source = discord.PCMVolumeTransformer(vc.source)
            vc.source.volume = 1;
            while vc.is_playing():
                await asyncio.sleep(1)
        await vc.disconnect()
    
    @commands.command(name='skip' , description='#skip')
    async def skip(self, ctx):
        global current_song,vc
        if current_song:
            vc.stop()
            current_song = None
        else:
            await ctx.send("No song is currently playing.")
    
    @commands.command(name='leave', description='leave')
    async def leave(self, ctx):
        global vc
        await vc.disconnect()