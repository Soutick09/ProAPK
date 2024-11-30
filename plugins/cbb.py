#(©)Codeflix-Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀs : <a href='https://t.me/ProAPK_Owner'>ProAPK Owner</a> | <a href='https://t.me/Soutick_09'>Soutick</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/+UbKgjcJOEkg2NGZl'>ProAPK PRIVATE</a>\n○ ᴀɴɪᴍᴇ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/+YtbcMJRsXM5hNjY9'>AniTown4U</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ Close", callback_data = "close"),
                    InlineKeyboardButton('🍁 Website', url='https://proapk.net')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
