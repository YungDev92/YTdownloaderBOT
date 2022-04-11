
import pyrogram

from pyrogram import Client, filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support Channel", url="https://t.me/YdpBots")],
        [InlineKeyboardButton(
            "Support Group", url="https://t.me/YdpDiscussion")]
    ])
    welcomed = f"Hi! <b>{message.from_user.first_name}</b>\n/help to check Features."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
