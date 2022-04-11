import pyrogram
from pyrogram import Client, filters


@Client.on_message(filters.command(["help"]))
async def start(client, message):
    helptxt = f"Bot Can Download Mp3/Mp4 from youtube Powered by @yung92"
    await message.reply_text(helptxt)
