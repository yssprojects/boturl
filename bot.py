import requests
from pyrogram import Client, filters,

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_URL = environ.get('API_URl')

bot = Client('gplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm Url Shorten bot. Just send me link and get short link\n @yssprojects")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        links = 'https://url-shorten-api.vercel.app/create?u='+link
        shotlink = requests.get(links).json()
        ide = shotlink['unique_id']
        linka = "https://ysslinkbot.herokuapp.com/"+ide
        await message.reply('Here is your \n '+linka'\n @yssprojects', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


bot.run()
