import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

    
@Client.on_message(commandpro(["/start", "/alive", "pavan"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a0ceebfb97ce2f711ab37.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ʜᴇʀᴇ ɪꜱ ᴀ ꜱᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/CreatorPavanSupport")
                ],[
                    InlineKeyboardButton(
                        "• ʜᴇʀᴇ ɪꜱ ᴀ ᴜᴘᴅᴀᴛᴇꜱ •", url=f"https://t.me/TheCreatorPavan")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["pavan"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c71a064fd6ba982578641.jpg",
        caption=f"""**ᴛʜɪꜱ ᴏᴘ ʙᴏᴛ ɪꜱ ꜱᴘᴇᴄɪᴀʟʟʏ ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ. ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴏʀ ᴀ Qᴜᴇꜱᴛɪᴏɴ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ •", url=f"https://t.me/PavanxD")
                ]
            ]
        ),
    )

@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c71a064fd6ba982578641.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ꜰᴏʀ ʀᴇᴘᴏ ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ •", url=f"https://t.me/PavanxD")
                ]
            ]
        ),
    )
