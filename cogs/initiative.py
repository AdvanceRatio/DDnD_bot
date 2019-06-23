import discord
from discord.ext import commands


class Example(commands.Cog):
    initiatives = []
    current_initiative = 0
    current_round = 1

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Initiative *cog* is loaded')

    @commands.command(name="si")
    async def set_initiative(self, ctx, *args):
        """
         Sets initial combat initiative
        :param ctx:
        :return:
        """
        it = iter(args)
        self.initiatives.extend(zip(it, it))
        await ctx.send('Set initiative')

    @commands.command(name="ni")
    async def next_initiative(self, ctx):
        """
         Moves to the next entities turn
        :param ctx:
        :return:
        """
        init = self.initiatives
        i = self.current_initiative
        if i >= len(self.initiatives):
            await ctx.send('-'*10)
            await ctx.send(' Round is over')
            await ctx.send('-' * 10)
            self.current_round += 1
            i = 0
        self.current_initiative = i + 1
        await ctx.send(f'{init[i][0]} is up. Initiative: {init[i][1]}')

    @commands.command(name="ei")
    async def reset_initiative(self, ctx):
        """
         Ends initiative
        :param ctx:
        :return:
        """
        self.initiatives = []
        self.current_initiative = 0
        await ctx.send('Combat is over. Is Thorgal dead?')


def setup(client):
    client.add_cog(Example(client))
