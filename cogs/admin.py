from asgiref.sync import sync_to_async
import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option
from core.models.guild import Guild
from maakay.shortcuts import convert_to_decimal


class admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_subcommand(base="admin",
                            name="set_withdrawl_address",
                            description="Set withdrawl adress for the server",
                            options=[
                                create_option(
                                    name="address",
                                    description="Withdrawl address",
                                    required=True,
                                    option_type=3)
                            ])
    async def admin_set_withdrawl_address(self, ctx, address):

        guild, created = await sync_to_async(Guild.objects.get_or_create)(guild_id=str(ctx.guild.id))

        if guild.has_permissions:

            has_role = False
            for role in ctx.author.roles:

                if role.id == int(guild.manager_role_id):
                    has_role = True
                    break

            if has_role:
                if len(address) == 64:

                    guild.withdrawal_address = address
                    guild.save()

                    await ctx.send(f"Withdrawl address for **{ctx.guild.name}** set to `{address}` successfully!", hidden=True)
                else:
                    await ctx.send("Invalid Withdrawl Address!", hidden=True)

            else:
                role = ctx.guild.get_role(int(guild.manager_role_id))
                await ctx.send(f"You don't have the required `{role.name}` Role!!", hidden=True)

        else:
            await ctx.send("Oh no, seems like Maakay-bot was not invited with correct permissions!!, \nHere are some steps to resolve the issue! \n ```1. Kick Maakay-bot. \n2. Invite Maakay-bot with 'Manage Roles' and 'Send Message' permissions.```", hidden=True)

    @cog_ext.cog_subcommand(base="admin",
                            name="info",
                            description="Check the maakay profile of your discord server.")
    async def admin_info(self, ctx):

        guild, created = await sync_to_async(Guild.objects.get_or_create)(guild_id=str(ctx.guild.id))

        if guild.has_permissions:

            has_role = False
            for role in ctx.author.roles:

                if role.id == int(guild.manager_role_id):
                    has_role = True
                    break

            if has_role:

                embed = discord.Embed()
                embed.add_field(name="Withdrawal Address", value=guild.withdrawal_address, inline=False)
                embed.add_field(name="Total Fees Collected (TNBC)", value=convert_to_decimal(guild.total_fee_collected))
                embed.add_field(name="Guild Balance (TNBC)", value=convert_to_decimal(guild.guild_balance))
                await ctx.send(embed=embed, hidden=True)

            else:
                role = ctx.guild.get_role(int(guild.manager_role_id))
                await ctx.send(f"You don't have the required `{role.name}` Role!!", hidden=True)
        else:
            await ctx.send("Oh no, seems like Maakay-bot was not invited with correct permissions!!, \nHere are some steps to resolve the issue! \n ```1. Kick Maakay-bot. \n2. Invite Maakay-bot with 'Manage Roles' and 'Send Message' permissions.```", hidden=True)



def setup(bot):
    bot.add_cog(admin(bot))
