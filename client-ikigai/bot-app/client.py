from __main__ import TARGET_CHANNEL_ID
import person
import discord
import sqlite3
import logs
import re


class Client(discord.Client):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        super().__init__()

    async def on_ready(self):
        logs.info("Logged in as", self.user.name)

    async def on_message(self, message: discord.Message):
        if message.channel.id == TARGET_CHANNEL_ID:
            if message.content == "/points":
                await self.command_my_score(message)
                return
            if message.content in ("/leaderboard", "/lb"):
                await self.command_leaderboard(message)
                return
            if re.match(
                r"https://twitter\.com/[a-zA-Z0-9_\-]+/status/*", message.content
            ):
                if (
                    message.embeds
                    and type(message.embeds[0].description) is str
                    and "@SilencioWL" in message.embeds[0].description
                ):
                    await self.raise_score(message, 3)
                    return
            if (
                message.attachments
                and message.attachments[0].content_type
                and message.attachments[0].content_type.startswith("image")
            ):
                await self.raise_score(message, 1)
                return

    async def raise_score(self, message: discord.Message, by: int):
        person_id = message.author.id
        try:
            person_score = person.get_score(self.conn, message.author.id)
            person.set_score(self.conn, person_id, person_score + by)
        except ValueError:
            person.add_new(self.conn, person_id)
            person.set_score(self.conn, person_id, by)
        embed = discord.Embed(
            title=f":tada: You gained {by} point(s)",
            description=f"{message.author.mention} has {person_score + by} point(s)",
            color=0xFF9900,
        )
        await message.channel.send(embed=embed)

    async def command_my_score(self, message: discord.Message):
        try:
            person_score = person.get_score(self.conn, message.author.id)
            embed = discord.Embed(
                title=":shopping_bags: Your Points",
                description=f"{message.author.mention} has {person_score} point(s)",
                color=0xFF9900,
            )
            await message.channel.send(embed=embed)
        except ValueError:
            embed = discord.Embed(
                description=f"{message.author.mention} does not have any points",
                color=0xFF9900,
            )
            await message.channel.send(embed=embed)

    async def command_leaderboard(self, message: discord.Message):
        i = 1
        res = ""
        for person_id, person_score in person.get_top_scores(self.conn, 10):
            user = await self.fetch_user(person_id)
            emoji = {1: ":first_place:", 2: ":second_place:", 3: ":third_place:"}.get(
                i, ""
            )
            res += f"`{i:>02}. `  {emoji}{user.mention}  -  `{person_score} Points`\n"
            i += 1
        embed = discord.Embed(
            title=":crossed_swords: Points Leaderboard",
            description=res,
            url="https://twitter.com/SilencioWL",
            color=0xFF9900,
        )
        await message.channel.send(embed=embed)
