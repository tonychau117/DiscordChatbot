import discord
import response

async def send_msg(message, userMessage, isPrivate):
    try:
        responses = response.get_response(userMessage)
        await message.author.send(responses) if isPrivate else await message.channel.send(responses)
    
    except Exception as e:
        print(e)

def run_bot():
    TOKEN = "" # place your bot token here
    intent = discord.Intents.default()
    intent.message_content = True
    client = discord.Client(intents = intent)

    @client.event
    async def on_ready():
        print(f"{client.user} is now active")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        userMessage = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{userMessage}' ({channel})")

        if userMessage[0] == "?":
            userMessage = userMessage[1:]
            await send_msg(message, userMessage, isPrivate = True)
        else:
            await send_msg(message, userMessage, isPrivate = False)

    client.run(TOKEN)
