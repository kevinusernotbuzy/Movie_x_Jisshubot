from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from info import ADMINS, LOG_CHANNEL, USERNAME, ADDGRP_PIC
from database.users_chats_db import db
from database.ia_filterdb import Media, get_files_db_size
from utils import get_size, temp
from Script import script
from datetime import datetime
import psutil
import time
import random

@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    check = [u.id for u in message.new_chat_members]
    if temp.ME in check:  # Check if the bot is one of the new members
        if str(message.chat.id).startswith("-100") and not await db.get_chat(message.chat.id):
            total = await bot.get_chat_members_count(message.chat.id)
            user = message.from_user.mention if message.from_user else "Dear"
            
            # Try to export invite link; handle permission issues
            try:
                group_link = await message.chat.export_invite_link()
            except Exception as e:
                group_link = "No Invite Link"  # Default text for permission issues

            # Format the message for the log channel
            log_message = script.NEW_GROUP_TXT.format(
                temp.B_LINK,
                message.chat.title,
                message.chat.id,
                message.chat.username or "No Username",
                group_link,
                total,
                user
            )
            
            # Send the log message to the log channel
            try:
                await bot.send_message(LOG_CHANNEL, log_message, disable_web_page_preview=True)
            except Exception as e:
                print(f"Error sending message to log channel: {e}")

            # Save group info in the database
            try:
                await db.add_chat(message.chat.id, message.chat.title)
            except Exception as e:
                print(f"Error saving group to the database: {e}")

            # Select a random image from the list in ADD_GROUP_PIC
            random_pic = random.choice(ADDGRP_PIC)

            # Notify the group with a welcome message and a random picture
            btn = [[
                InlineKeyboardButton('• Support •', url=USERNAME),
                InlineKeyboardButton('• Update •', url="https://t.me/noob_marcus")
            ]]
            reply_markup = InlineKeyboardMarkup(btn)
            welcome_message = (
                f"<b>ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ᴛᴏ {message.chat.title} ♥️🥀</b>\n\n"
                f"⚠️ <i>ᴘʟᴇᴀsᴇ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ᴡɪᴛʜ 'ᴅᴇʟᴇᴛᴇ' & 'ɪɴᴠɪᴛᴇ' ᴘᴇʀᴍɪssɪᴏɴs ғᴏʀ ᴏᴘᴛɪᴍᴀʟ ᴘᴇʀғᴏʀᴍᴀɴᴄᴇ.</i>\n\n"
                f"<b>ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs? ᴜsᴇ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴs ᴏʀ ʀᴇᴀᴄʜ ᴏᴜᴛ ᴛᴏ sᴜᴘᴘᴏʀᴛ.</b>\n\n"
                f"✨ <b>ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴜsɪɴɢ /settings ✨</b>"
            )
            try:
                # Send the random image along with the welcome message
                await bot.send_photo(
                    chat_id=message.chat.id,
                    photo=random_pic,  # Ensure the photo is a valid URL or file ID
                    caption=welcome_message,
                    reply_markup=reply_markup
                )
            except Exception as e:
                print(f"Error sending welcome message with picture to group: {e}")


                    


@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def leave_a_chat(bot, message):
    r = message.text.split(None)
    if len(message.command) == 1:
        return await message.reply('<b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʟɪᴋᴇ ᴛʜɪꜱ `/leave -100******`</b>')
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "ɴᴏ ʀᴇᴀꜱᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ..."
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        btn = [[
            InlineKeyboardButton('⚡️ ᴏᴡɴᴇʀ ⚡️', url=USERNAME)
        ]]
        reply_markup=InlineKeyboardMarkup(btn)
        await bot.send_message(
            chat_id=chat,
            text=f'😞 ʜᴇʟʟᴏ ᴅᴇᴀʀ,\nᴍʏ ᴏᴡɴᴇʀ ʜᴀꜱ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ɢʀᴏᴜᴘ ꜱᴏ ɪ ɢᴏ 😔\n\n🚫 ʀᴇᴀꜱᴏɴ ɪꜱ - <code>{reason}</code>\n\nɪꜰ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴀᴅᴅ ᴍᴇ ᴀɢᴀɪɴ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ 👇',
            reply_markup=reply_markup,
        )
        await bot.leave_chat(chat)
        await db.delete_chat(chat)
        await message.reply(f"<b>ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʟᴇꜰᴛ ꜰʀᴏᴍ ɢʀᴏᴜᴘ - `{chat}`</b>")
    except Exception as e:
        await message.reply(f'<b>🚫 ᴇʀʀᴏʀ - `{e}`</b>')

@Client.on_message(filters.command('groups') & filters.user(ADMINS))
async def groups_list(bot, message):
    msg = await message.reply('<b>Searching...</b>')
    chats = await db.get_all_chats()
    out = "Groups saved in the database:\n\n"
    count = 1
    async for chat in chats:
        chat_info = await bot.get_chat(chat['id'])
        members_count = chat_info.members_count if chat_info.members_count else "Unknown"
        out += f"<b>{count}. Title - `{chat['title']}`\nID - `{chat['id']}`\nMembers - `{members_count}`</b>"
        out += '\n\n'
        count += 1
    try:
        if count > 1:
            await msg.edit_text(out)
        else:
            await msg.edit_text("<b>No groups found</b>")
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="<b>List of all groups</b>")


@Client.on_message(filters.command('stats') & filters.user(ADMINS) & filters.incoming)
async def get_stats(bot, message):
    # Show a temporary "Fetching stats..." message
    fukx = await message.reply('⚡ Fetching stats...')
    
    try:
        # Fetch required stats
        users = await db.total_users_count()
        groups = await db.total_chat_count()
        size = get_size(await db.get_db_size())
        free = get_size(536870912)
        files = await Media.count_documents()
        db2_size = get_size(await get_files_db_size())
        db2_free = get_size(536870912)
        uptime_seconds = int(time.time() - psutil.boot_time())  # Correct uptime calculation
        uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(uptime_seconds))
        ram = psutil.virtual_memory().percent
        cpu = psutil.cpu_percent()

        # Edit the temporary message with the stats
        await fukx.edit(
            script.STATUS_TXT.format(
                users, groups, size, free, files, db2_size, db2_free, uptime, ram, cpu
            )
        )
    except Exception as e:
        # If any error occurs, inform the user
        await fukx.edit(f"❌ Failed to fetch stats: {e}")
