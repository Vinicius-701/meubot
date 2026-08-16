import discord
from discord.ext import commands
from config import discord_token
from caalculador import calc

valor1 = discord.Intents.default()
valor1.message_content = True

class Base(commands.Bot):

    async def on_ready(self):
        print(f'ligado cacete')

    async def on_message(self, message):
        print(f'mensagem de {message.author}: {message.content}')

        await self.process_commands(message)

vartrol = Base(
    command_prefix='!',
    intents=valor1
)

@vartrol.command()
async def ping(ctx):
    await ctx.send(f" latencia de {vartrol.latency * 1000:.2f} ms!")


@vartrol.command()
async def prox(ctx, num):
        result = calc(num)
        await ctx.send(f'o proximo numero é {result}')


vartrol.run(discord_token)

