import discord
from bot_mantik import gen_pass
import sympy

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('ily'):
        await message.channel.send("ly2")
    if message.content.startswith('çikolata'):
        await message.channel.send("severim")
    if any(message.content.startswith(word) for word in ['hi', 'yo', 'wsup', 'hello']):
        await message.channel.send("Hi!<3")
    
    elif any(message.content.startswith(word) for word in ['goodbye', 'bye', 'see ya', 'take care']):
        await message.channel.send("byee<3")
        await message.add_reaction('👋')

    elif any(message.content.startswith(word) for word in['parola','key']):
        await message.channel.send(gen_pass(12))
    if message.content.startswith('Allah varmidir?'):
        await message.channel.send('vardir,ve tekdir!')
    if message.content.startswith('Allah'):
        await message.channel.send('tekdir!')
    if message.content.startswith('!math'):
        try:
            # Get the expression by removing the command prefix
            expression = message.content[6:]
            # Use sympy to evaluate the expression
            result = sympy.sympify(expression)
            await message.channel.send(f'The result is: {result}')
        except Exception as e:
            await message.channel.send(f'Error: {e}')

client.run("")
