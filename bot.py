import discord

# Escribir aquí el Token de tu bot
TOKEN = ""

bot = discord.Client()

# Cambiar estas palabras por las que tú gustes, puedes agregar también las que quieras dentro de las [] y con ""
palabras = ["hola", "adios", "https://"]

@bot.event
async def on_ready():
    # Puedes poner el mensaje que quieras dentro de las ""
    print("El bot ha sido iniciado!")

@bot.event
async def on_message(message):
    if message.author != bot.user:
        for text in palabras:
            # Puedes cambiar dentro de las comillas el nombre del rol o los roles que quieras que se ignoren
            if "Administrador" not in str(message.author.roles) and text in (message.content.lower()):
                await message.delete()
                return

bot.run(TOKEN)