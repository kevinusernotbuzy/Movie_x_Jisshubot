import time
import random
from info import EARNMONEY_PIC
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

CMD = ["/", "."]

@Client.on_message(filters.command("earn_money", CMD))
async def show_money(_, message):
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("× ᴄʟᴏsᴇ ×", callback_data="close_data")]])
    await message.reply_photo(
        photo=random.choice(EARNMONEY_PIC),
        caption="<b>──────「 <a href='t.me/Vampirexgirl'>ᴇᴀʀɴ ᴍᴏɴᴇʏ</a> 」─────\n\n<b>Now You can start earning 💸 money today with our Simple and easy-to-use bot!\n\n›› Step 1: Add This bot to your group as an admin..\n\n›› Step 2: If you don't Using any shortner website then make account first on <a href=https://mdiskshortner.link/ref/Kimxd'>mdiskshortner.link</a> (You can also use other link shortner website).\n\n›› Step 3: Copy your API from website and then, simply set your website and API Using the\n/set_shortner command\n\n› Like this : <pre>/set_shortner shorturllink.in 7eddb02ee3a9e5ad7c207aab9cce5b34fadfe22f</pre>\n\n\nNow you Can add your tutorial link in \"How to download\" button\n/set_tutorial - Your tutorial video link\n/del_tutorial - Delete your tutorial video link\n\n★ This bot will automatically converts links with Your Api and will provide your links.\n\n★ Don't wait any longer to start earning money from your telegram group. Add our bot today and start making money 💰!</b>\n", 
        reply_markup=reply_markup
    )
