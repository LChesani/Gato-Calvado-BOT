import libs.pk as pk;
from discord.ext import commands;
import BotAgendamentoRU.botRU as botRU;

data = pk.load_pickle(dict(), 'data');

class RestauranteUniversitario(commands.Cog):
    @commands.command(name='logar' , description='#logar -matricula- -senha-')
    async def logar(self, context, *info):
        if len(info) != 2:
            await context.channel.send('Insira os dados corretamente!');
        else:
            if str(context.author.id) not in data:
                data[str(context.author.id)] = info;
                pk.save_pickle(data, 'data');
                await context.channel.send('Dados enviados para o governo chinês com sucesso!');
            else:
                await context.channel.send('seu login já foi cadastrado no governo chinês, use "!remover" para deletar e cadastrar um novo');
        context.message.delete();
        
    @commands.command(name='remover', description='Remova o seu login do bd')
    async def remover(self, context):
        if str(context.author.id) not in data:
            await context.reply('Login nao existe no bd');
        else:
            del data[str(context.author.id)];
            pk.save_pickle(data, 'data');
            await context.reply('login deletado do bd com sucesso!');

    @commands.command(name='agendar' , description='Faça uma chamada de agendamento para os próximos 3 dias')
    async def agendar(self, context):
        idx = str(context.author.id);
        if idx not in data:
            await context.channel.send('É preciso logar primeiro!');
        else:
            await botRU.agendar(context, data[idx]);
    
    
    