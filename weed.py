import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
TOKEN = ""

bot = commands.Bot(command_prefix='!', intents=intents)

with open('token.txt') as f:
        lines = f.readlines()
        if len(lines) != 1:
            raise ValueError("token.txt should contain exactly one line")
        TOKEN = lines[0].strip()
        print(f'Token read from file: {TOKEN}')

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    # Sync the command tree so discord understands this bot has commands
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

@bot.tree.command(name="penis", description="time to measure")
async def pepsi(interaction: discord.Interaction, user: discord.User = None):
    target_user = user or interaction.user
    if target_user.id == 275238964838006784: ## this id is my own bot's user id. you can change it if you want.
        response = "ERROR: CHARACTER LIMIT REACHED TRYING TO INPUT CHARACTER: ="
    else:
        random.seed(target_user.id)
        if random.randint(1, 255) == 1:
            size = random.randint(20, 35)
        else:
            size = random.randint(1, 10)
        response = f'{target_user.mention} Size: 8{"=" * size}D'
    await interaction.response.send_message(response)

@bot.hybrid_group(invoke_without_command=True) # most of these !faq commands ar einside jokes made for my friends to spam. edit them to your liking
async def faq(ctx):
    await ctx.send("Available FAQs: lines, owowhatsthis") ## todo: change this so it gets all the available commands in a list and outputs them dynamically

@faq.command()
async def lines(ctx):
    await ctx.send("It's best to type one big message instead of 5 short ones in a row.")

@faq.command()
async def owowhatsthis(ctx):
    await ctx.send(":regional_indicator_n: :regional_indicator_u: :regional_indicator_z: :regional_indicator_z: :regional_indicator_l: :regional_indicator_e: :regional_indicator_s: :large_blue_diamond: :regional_indicator_u: :large_blue_diamond: :regional_indicator_b: :regional_indicator_a: :regional_indicator_c: :regional_indicator_k: :large_blue_diamond: :regional_indicator_a: :regional_indicator_n: :regional_indicator_d: :large_blue_diamond: :regional_indicator_n: :regional_indicator_o: :regional_indicator_t: :regional_indicator_i: :regional_indicator_c: :regional_indicator_e: :regional_indicator_s: :large_blue_diamond: :regional_indicator_y: :regional_indicator_o: :regional_indicator_u: :regional_indicator_r: :large_blue_diamond: :regional_indicator_b: :regional_indicator_u: :regional_indicator_l: :regional_indicator_g: :regional_indicator_e:")
    await ctx.send(":regional_indicator_o: :regional_indicator_w: :regional_indicator_o: :large_blue_diamond: :regional_indicator_w: :regional_indicator_h: :regional_indicator_a: :regional_indicator_t: :regional_indicator_s: :large_blue_diamond: :regional_indicator_t: :regional_indicator_h: :regional_indicator_i: :regional_indicator_s: :question:")

@faq.command()
async def douche(ctx):
    await ctx.send("Stop being such a fucking douche.") # omg the bad word

@faq.command()
async def peanut(ctx):
    await ctx.send("MMMMMMMMMM YUM, YUM, YUM, YUMMU AH HOW I LOVE JIFF PEANUT BUTTER !!!!!!!!!!! 😄 😄 😄 😄 😄 😄  SOOOOOOO(O GOOD WHEN IT SLIDMMMMMMMMMM YUM, YUM, YUM, YUMMU AH HOW I LOVE JIFF PEANUT BUTTER !!!!!!!!!!! 😄 😄 😄 😄 😄 😄  SOOOOOOO(O GOOD WHEN IT SLIDMMMMMMMMMM YUM, YUM, YUM, YUMMU AH HOW I LOVE JIFF PEANUT BUTTER !!!!!!!!!!! 😄 😄 😄 😄 😄 😄  SOOOOOOO(O GOOD WHEN IT SLIDMMMMMMMMMM YUM, YUM, YUM, YUMMU AH HOW I LOVE JIFF PEANUT BUTTER !!!!!!!!!!! 😄 😄 😄 😄 😄 😄  SOOOOOOO(O GOOD WHEN IT SLID")

@faq.command()
async def u(ctx):
    await ctx.send("That's rude :(")

bot.run(TOKEN)
