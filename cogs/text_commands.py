from discord.ext import commands
from firebase.api.projects import get_project, get_project_key_by_discord_user_id
from helpers.embed_templates import create_project_embed, error_embed


class MyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def show(self, ctx: commands.Context):
        project_key = get_project_key_by_discord_user_id(str(ctx.author.id))
        if project_key is None:
            await ctx.send(
                embed=error_embed(
                    "No project found, please connect to a project first using /connect"
                )
            )
            return

        # Get the project
        project = get_project(project_key)
        if project is None:
            await ctx.send(
                embed=error_embed(
                    "Invalid Project Key, please try to connect again using /connect"
                )
            )
            return

        # Create an embed using the provided function
        embed = create_project_embed(project)

        # Send the embed
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(MyCommands(bot))
