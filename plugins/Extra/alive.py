import time
import random
from info import HELP_PIC
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

CMD = ["/", "."]


@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("<b>ɪ ᴀᴍ ᴀʟᴡᴀʏꜱ ᴀʟɪᴠᴇ ꜰᴏʀ ʏᴏᴜ 🥵\n\nᴄʜᴇᴄᴋᴏᴜᴛ /start ꜰᴏʀ ᴍᴏʀᴇ...🥀✨</b>")


@Client.on_message(filters.command("rules", CMD))
async def help(_, message):
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("✦ 𝗧𝗵𝗲 𝗥𝘂𝗹𝗲𝘀 ✦", callback_data="rules")]])
    await message.reply_photo(
        photo=random.choice(HELP_PIC),
        caption="<b>Cʟɪᴄᴋ THᴇ Bᴜᴛᴛᴏɴ Fᴏʀ Sᴇᴇ Tʜᴇ Rᴜʟᴇs</b>", 
        reply_markup=reply_markup
    )


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"𝖯𝗂𝗇𝗀!\n{time_taken_s:.3f} ms")
