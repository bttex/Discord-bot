import discord
from discord.ext import commands, tasks
import datetime
import asyncio

# Configure seu bot
TOKEN = '################################'
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
@bot.command()
async def agendar(ctx, data_hora: str, mencao: str = '', *, mensagem: str):
    """
    Comando para agendar mensagens.
    Exemplo de uso: !agendar 02-08-2024-15:30 everyone Lembrete importante!
                  ou
                    !agendar 02-08-2024-15:30 me Lembrete importante!
    """
    try:
        print(f"Tentando agendar mensagem com data_hora: {data_hora}, mencao: {mencao}, e mensagem: {mensagem}")
        
        # Convertendo a string de data e hora para objeto datetime
        agendamento = datetime.datetime.strptime(data_hora, '%d-%m-%Y-%H:%M')

        if agendamento < datetime.datetime.now():
            await ctx.send('Não é possível agendar no passado. Tente novamente.')
            return

        await ctx.send(f'Mensagem agendada para {agendamento.strftime("%d-%m-%Y %H:%M")}: {mensagem}')
        # Agendar a tarefa de envio de mensagem
        bot.loop.create_task(enviar_mensagem_later(agendamento, ctx.channel, mensagem, mencao, ctx.author))
    except ValueError as e:
        print(f"Erro ao converter data_hora: {e}")
        await ctx.send('Formato inválido. Use: !agendar DD-MM-AAAA-HH:MM [me/everyone] Sua mensagem')

async def enviar_mensagem_later(agendamento, channel, mensagem, mencao, autor):
    # Calcular o tempo até o agendamento
    agora = datetime.datetime.now()
    delay = (agendamento - agora).total_seconds()
    # Esperar até o horário agendado
    await asyncio.sleep(delay)
    # Enviar a mensagem no canal especificado com a menção adequada
    if mencao.lower() == 'everyone':
        await channel.send(f"@everyone {mensagem}")
    elif mencao.lower() == 'me':
        await channel.send(f"{autor.mention} {mensagem}")
    elif mencao.lower() == 'milionarios':
        await channel.send(f"@Milionários {mensagem}")
    else:
        await channel.send(mensagem)

bot.run(TOKEN)