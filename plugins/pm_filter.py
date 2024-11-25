import asyncio
import re
import math
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import pyrogram
from info import * #SUBSCRIPTION, PAYPICS, START_IMG, SETTINGS, URL, STICKERS_IDS,PREMIUM_POINT,MAX_BTN, BIN_CHANNEL, USERNAME, URL, ADMINS,REACTIONS, LANGUAGES, QUALITIES, YEARS, SEASONS, AUTH_CHANNEL, SUPPORT_GROUP, IMDB, IMDB_TEMPLATE, LOG_CHANNEL, LOG_VR_CHANNEL, TUTORIAL, FILE_CAPTION, SHORTENER_WEBSITE, SHORTENER_API, SHORTENER_WEBSITE2, SHORTENER_API2, DELETE_TIME
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto, ChatPermissions, WebAppInfo, InputMediaAnimation, InputMediaPhoto
from pyrogram import Client, filters, enums
from pyrogram.errors import * #FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid, ChatAdminRequired
from utils import temp, get_settings, is_check_admin, get_status, get_size, save_group_settings, is_req_subscribed, get_poster, get_status, get_readable_time , imdb , formate_file_name
from database.users_chats_db import db
from database.ia_filterdb import Media, get_search_results, get_bad_files, get_file_details
import random
lock = asyncio.Lock()
from .Extra.checkFsub import is_user_fsub
import traceback
from fuzzywuzzy import process
BUTTONS = {}
FILES_ID = {}
CAP = {}

# zishan [
from database.jsreferdb import referdb
from database.config_db import mdb
import logging
from urllib.parse import quote_plus
from Jisshu.util.file_properties import get_name, get_hash, get_media_file_size
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
# ] codes add


@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_search(client, message):
    await mdb.update_top_messages(message.from_user.id, message.text)
    bot_id = client.me.id
    user_id = message.from_user.id    

    # Set the maximum allowed message length (e.g., 500 characters)
    max_length = 60

    # If the message starts with '/', ignore the message
    if str(message.text).startswith('/'):
        return

    # URL pattern to detect links
    url_pattern = re.compile(r"https?://[^\s]+|t\.me/[^\s]+|www\.[^\s]+")
    
    # If the message contains a URL, ignore the message
    if url_pattern.search(message.text):
        return

    # If the message is too long, ignore the message
    if len(message.text) > max_length:
        return
    
    # Check if bot is enabled for search functionality
    if await db.get_pm_search_status(bot_id):
        if 'hindi' in message.text.lower() or 'tamil' in message.text.lower() or 'telugu' in message.text.lower() or 'malayalam' in message.text.lower() or 'kannada' in message.text.lower() or 'english' in message.text.lower() or 'gujarati' in message.text.lower(): 
            return await auto_filter(client, message)
        await auto_filter(client, message)
    else:
        await message.reply_text("<b><i>ɪ ᴀᴍ ɴᴏᴛ ᴡᴏʀᴋɪɴɢ ʜᴇʀᴇ. ꜱᴇᴀʀᴄʜ ᴍᴏᴠɪᴇꜱ ɪɴ ᴏᴜʀ ᴍᴏᴠɪᴇ ꜱᴇᴀʀᴄʜ ɢʀᴏᴜᴘ.</i></b>",
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("• ᴍᴏᴠɪᴇ ꜱᴇᴀʀᴄʜ ɢʀᴏᴜᴘ •", url=f'https://t.me/request_movie2')]]))


    
@Client.on_message(filters.group & filters.text & filters.incoming)
async def group_search(client, message):
    #await message.react(emoji=random.choice(REACTIONS))
    await mdb.update_top_messages(message.from_user.id, message.text)
    user_id = message.from_user.id if message.from_user else None
    chat_id = message.chat.id
    settings = await get_settings(chat_id)
    ifJoinedFsub = await is_user_fsub(client,message)
    if ifJoinedFsub == False:
        return
    if message.chat.id == SUPPORT_GROUP :
                if message.text.startswith("/"):
                    return
                files, n_offset, total = await get_search_results(message.text, offset=0)
                if total != 0:
                    link = await db.get_set_grp_links(index=1)
                    msg = await message.reply_text(script.SUPPORT_GRP_MOVIE_TEXT.format(message.from_user.mention() , total) ,             reply_markup=InlineKeyboardMarkup([
                        [ InlineKeyboardButton('ɢᴇᴛ ғɪʟᴇs ғʀᴏᴍ ʜᴇʀᴇ' , url=link)]
                        ]))
                    await asyncio.sleep(300)
                    return await msg.delete()
                else: return     
    if settings["auto_filter"]:
        if not user_id:
            #await message.reply("<b>🚨 ɪ'ᴍ ɴᴏᴛ ᴡᴏʀᴋɪɴɢ ғᴏʀ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ!</b>")
            return
        
        if 'hindi' in message.text.lower() or 'tamil' in message.text.lower() or 'telugu' in message.text.lower() or 'malayalam' in message.text.lower() or 'kannada' in message.text.lower() or 'english' in message.text.lower() or 'gujarati' in message.text.lower(): 
            return await auto_filter(client, message)

        elif message.text.startswith("/"):
            return
		
        elif re.findall(r'https?://\S+|www\.\S+|t\.me/\S+', message.text):
            if await is_check_admin(client, message.chat.id, message.from_user.id):
                return
            await message.delete()
            warning_msg = await message.reply("⚠️ <b>ᴡᴀʀɴɪɴɢ: ᴜɴᴀᴜᴛʜᴏʀɪᴢᴇᴅ ʟɪɴᴋ ᴅᴇᴛᴇᴄᴛᴇᴅ!</b>\n\n<b><i>{message.from_user.mention} ʏᴏᴜʀ ᴍᴇꜱꜱᴀɢᴇ ʜᴀꜱ ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱ ꜱʜᴀʀɪɴɢ ᴇxᴛᴇʀɴᴀʟ ʟɪɴᴋꜱ ɪꜱ <u>ꜱᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ</u> ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.</i></b>")
            await asyncio.sleep(60)  # Wait for 1 minute (60 seconds)
            await warning_msg.delete()  # Delete the warning message after 1 minute

        elif '@admin' in message.text.lower() or '@admins' in message.text.lower():
            if await is_check_admin(client, message.chat.id, message.from_user.id):
                return
            admins = []
            async for member in client.get_chat_members(chat_id=message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
                if not member.user.is_bot:
                    admins.append(member.user.id)
                    if member.status == enums.ChatMemberStatus.OWNER:
                        if message.reply_to_message:
                            try:
                                sent_msg = await message.reply_to_message.forward(member.user.id)
                                await sent_msg.reply_text(f"#Attention\n★ User: {message.from_user.mention}\n★ Group: {message.chat.title}\n\n★ <a href={message.reply_to_message.link}>Go to message</a>", disable_web_page_preview=True)
                            except:
                                pass
                        else:
                            try:
                                sent_msg = await message.forward(member.user.id)
                                await sent_msg.reply_text(f"#Attention\n★ User: {message.from_user.mention}\n★ Group: {message.chat.title}\n\n★ <a href={message.link}>Go to message</a>", disable_web_page_preview=True)
                            except:
                                pass
            hidden_mentions = (f'[\u2064](tg://user?id={user_id})' for user_id in admins)
            await message.reply_text('<code>Report sent</code>' + ''.join(hidden_mentions))
            return               
        else:
            try: 
                await auto_filter(client, message)
            except Exception as e:
                traceback.print_exc()
                print('found err in grp search  :',e)

    else:
        k=await message.reply_text('<b>⚠️ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ᴍᴏᴅᴇ ɪꜱ ᴏғғ...</b>')
        await asyncio.sleep(10)
        await k.delete()
        try:
            await message.delete()
        except:
            pass

@Client.on_callback_query(filters.regex(r"^reffff"))
async def refercall(bot, query):
    btn = [[
        InlineKeyboardButton('• sʜᴀʀᴇ ʟɪɴᴋ •', url=f'https://telegram.me/share/url?url=https://t.me/{bot.me.username}?start=reff_{query.from_user.id}&text=Hello%21%20Experience%20a%20bot%20that%20offers%20a%20vast%20library%20of%20unlimited%20movies%20and%20series.%20%F0%9F%98%83'),
        InlineKeyboardButton(f'⏳ {referdb.get_refer_points(query.from_user.id)}', callback_data='ref_point'),
        InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close_data')
    ]]
    reply_markup = InlineKeyboardMarkup(btn)
    await bot.send_photo(
        chat_id=query.message.chat.id,
        photo="https://graph.org/file/1a2e64aee3d4d10edd930.jpg",
        caption=f'» ʏᴏᴜʀ ʀᴇғᴇʀ ʟɪɴᴋ:\n\nhttps://t.me/{bot.me.username}?start=reff_{query.from_user.id}\n\nsʜᴀʀᴇ ᴛʜɪs ʟɪɴᴋ ᴡɪᴛʜ ʏᴏᴜʀ ғʀɪᴇɴᴅs, ᴇᴀᴄʜ ᴛɪᴍᴇ ᴛʜᴇʏ ᴊᴏɪɴ,  ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ 𝟷𝟶 ʀᴇғғᴇʀᴀʟ ᴘᴏɪɴᴛs ᴀɴᴅ ᴀғᴛᴇʀ 𝟷𝟶𝟶 ᴘᴏɪɴᴛs ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ 𝟷 ᴍᴏɴᴛʜ ᴘʀᴇᴍɪᴜᴍ sᴜʙsᴄʀɪᴘᴛɪᴏɴ.</b>',
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )
    await query.answer()
	


@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query):
    ident, req, key, offset = query.data.split("_")
    if int(req) not in [query.from_user.id, 0]:
        return await query.answer(script.ALRT_TXT.format(query.from_user.first_name), show_alert=True)
    try:
        offset = int(offset)
    except:
        offset = 0
    search = BUTTONS.get(key)
    cap = CAP.get(key)
    if not search:
        await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name),show_alert=True)
        return
    files, n_offset, total = await get_search_results(search, offset=offset)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0
    if not files:
        return
    temp.FILES_ID[key] = files
    batch_ids = files
    temp.FILES_ID[f"{query.message.chat.id}-{query.id}"] = batch_ids
    batch_link = f"batchfiles#{query.message.chat.id}#{query.id}#{query.from_user.id}"
    ads, ads_name, _ = await mdb.get_advirtisment()
    ads_text = ""
    if ads is not None and ads_name is not None:
        ads_url = f"https://t.me/{temp.U_NAME}?start=ads"
        ads_text = f"<a href={ads_url}>{ads_name}</a>"
    js_ads = f"\n━━━━━━━━━━━━━━━━━━\n <b>{ads_text}</b> \n━━━━━━━━━━━━━━━━━━" if ads_text else ""
    settings = await get_settings(query.message.chat.id)
    reqnxt  = query.from_user.id if query.from_user else 0
    temp.CHAT[query.from_user.id] = query.message.chat.id
    #del_msg = f"\n\n<b>⚠️ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀꜰᴛᴇʀ <code>{get_readable_time(DELETE_TIME)}</code> ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs</b>" if settings["auto_delete"] else ''
    links = ""
    if settings["link"]:
        btn = []
        for file_num, file in enumerate(files, start=offset+1):
            links += f"""<b>\n\n{file_num}. <a href=https://t.me/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}>[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}</a></b>"""
    else:
        btn = [[InlineKeyboardButton(text=f"📁 {get_size(file.file_size)} ✦ {formate_file_name(file.file_name)}", url=f'https://telegram.dog/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}'),]
                for file in files
              ]
    btn.insert(0,[
	InlineKeyboardButton("sᴇɴᴅ ᴀʟʟ ғɪʟᴇs", callback_data=batch_link),
        ])
    btn.insert(1, [
	InlineKeyboardButton("ꜱᴇᴀꜱᴏɴ", callback_data=f"seasons#{key}#{offset}#{req}"),
        InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ ", callback_data=f"languages#{key}#{offset}#{req}")
    ])    

    if 0 < offset <= int(MAX_BTN):
        off_set = 0
    elif offset == 0:
        off_set = None
    else:
        off_set = offset - int(MAX_BTN)
    if n_offset == 0:

        btn.append(
            [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}"),
             InlineKeyboardButton(f"ᴘᴀɢᴇ {math.ceil(int(offset) / int(MAX_BTN)) + 1} / {math.ceil(total / int(MAX_BTN))}", callback_data="pages")]
        )
    elif off_set is None:
        btn.append(
            [InlineKeyboardButton(f"{math.ceil(int(offset) / int(MAX_BTN)) + 1} / {math.ceil(total / int(MAX_BTN))}", callback_data="pages"),
             InlineKeyboardButton("ɴᴇxᴛ ›", callback_data=f"next_{req}_{key}_{n_offset}")])
    else:
        btn.append(
            [
                InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}"),
                InlineKeyboardButton(f"{math.ceil(int(offset) / int(MAX_BTN)) + 1} / {math.ceil(total / int(MAX_BTN))}", callback_data="pages"),
                InlineKeyboardButton("ɴᴇxᴛ ›", callback_data=f"next_{req}_{key}_{n_offset}")
            ],
        )
    if settings["link"]:
        links = ""
        for file_num, file in enumerate(files, start=offset+1):
            links += f"""<b>\n\n{file_num}. <a href=https://t.me/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}>[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}</a></b>"""
        await query.message.edit_text(cap + links + js_ads, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn))
        return        
    try:
        await query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(btn)
        )
    except MessageNotModified:
        pass
    await query.answer()
    
@Client.on_callback_query(filters.regex(r"^seasons#"))
async def seasons_cb_handler(client: Client, query: CallbackQuery):
    _, key, offset, req = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer(script.ALRT_TXT, show_alert=True) 
    btn= []
    for i in range(0, len(SEASONS)-1, 2):
        btn.append([
            InlineKeyboardButton(
                text=SEASONS[i].title(),
                callback_data=f"season_search#{SEASONS[i].lower()}#{key}#0#{offset}#{req}"
            ),
            InlineKeyboardButton(
                text=SEASONS[i+1].title(),
                callback_data=f"season_search#{SEASONS[i+1].lower()}#{key}#0#{offset}#{req}"
            ),     
        ])

    btn.append([InlineKeyboardButton(text="‹ ʙᴀᴄᴋ ᴛᴏ ᴍᴀɪɴ ᴘᴀɢᴇ", callback_data=f"next_{req}_{key}_{offset}")])
    await query.message.edit_text("<b>ɪɴ ᴡʜɪᴄʜ sᴇᴀsᴏɴ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ, ᴄʜᴏᴏsᴇ ғʀᴏᴍ ʜᴇʀᴇ ↓↓</b>", reply_markup=InlineKeyboardMarkup(btn))
    return

@Client.on_callback_query(filters.regex(r"^season_search#"))
async def season_search(client: Client, query: CallbackQuery):
    _, season, key, offset, orginal_offset, req = query.data.split("#")
    seas = int(season.split(' ' , 1)[1])
    if seas < 10:
        seas = f'S0{seas}'
    else:
        seas = f'S{seas}'
    
    if int(req) != query.from_user.id:
        return await query.answer(script.ALRT_TXT, show_alert=True)	
    offset = int(offset)
    search = BUTTONS.get(key)
    cap = CAP.get(key)
    if not search:
        await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name),show_alert=True)
        return 
    search = search.replace("_", " ")
    files, n_offset, total = await get_search_results(f"{search} {seas}", max_results=int(MAX_BTN), offset=offset)
    files2, n_offset2, total2 = await get_search_results(f"{search} {season}", max_results=int(MAX_BTN), offset=offset)
    total += total2
    try:
        n_offset = int(n_offset)
    except:
        try: 
            n_offset = int(n_offset2)
        except : 
            n_offset = 0
    files = [file for file in files if re.search(seas, file.file_name, re.IGNORECASE)]
    
    if not files:
        files = [file for file in files2 if re.search(season, file.file_name, re.IGNORECASE)]
        if not files:
            await query.answer(f"sᴏʀʀʏ {season.title()} ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ {search}", show_alert=1)
            return

    batch_ids = files
    temp.FILES_ID[f"{query.message.chat.id}-{query.id}"] = batch_ids
    batch_link = f"batchfiles#{query.message.chat.id}#{query.id}#{query.from_user.id}"
    reqnxt = query.from_user.id if query.from_user else 0
    settings = await get_settings(query.message.chat.id)
    temp.CHAT[query.from_user.id] = query.message.chat.id
    ads, ads_name, _ = await mdb.get_advirtisment()
    ads_text = ""
    if ads is not None and ads_name is not None:
        ads_url = f"https://t.me/{temp.U_NAME}?start=ads"
        ads_text = f"<a href={ads_url}>{ads_name}</a>"
    js_ads = f"\n━━━━━━━━━━━━━━━━━━\n <b>{ads_text}</b> \n━━━━━━━━━━━━━━━━━━" if ads_text else ""
  #  del_msg = f"\n\n<b>⚠️ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀꜰᴛᴇʀ <code>{get_readable_time(DELETE_TIME)}</code> ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs</b>" if settings["auto_delete"] else ''
    links = ""
    if settings["link"]:
        btn = []
        for file_num, file in enumerate(files, start=offset+1):
            links += f"""<b>\n\n{file_num}. <a href=https://t.me/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}>[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}</a></b>"""
    else:
        btn = [[
                InlineKeyboardButton(text=f"📁 {get_size(file.file_size)} ✦ {formate_file_name(file.file_name)}", callback_data=f'files#{reqnxt}#{file.file_id}'),]
                   for file in files
              ]
   
    btn.insert(0,[
	InlineKeyboardButton("sᴇɴᴅ ᴀʟʟ ғɪʟᴇs", callback_data=batch_link),
        ])
    btn.insert(1, [
	InlineKeyboardButton("ꜱᴇᴀꜱᴏɴ", callback_data=f"seasons#{key}#{offset}#{req}"),
        InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ ", callback_data=f"languages#{key}#{offset}#{req}")
    ])    
    
    if n_offset== '':
        btn.append(
            [InlineKeyboardButton(text="🥲 ɴᴏ ᴍᴏʀᴇ ᴘᴀɢᴇs 🥲", callback_data="buttons")]
        )
    elif n_offset == 0:
        btn.append(
            [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data=f"season_search#{season}#{key}#{offset- int(MAX_BTN)}#{orginal_offset}#{req}"),
             InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}", callback_data="pages",),
            ])
    elif offset==0:
        btn.append(
            [InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}",callback_data="pages",),
             InlineKeyboardButton("ɴᴇxᴛ ›", callback_data=f"season_search#{season}#{key}#{n_offset}#{orginal_offset}#{req}"),])
    else:
        btn.append(
            [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data=f"season_search#{season}#{key}#{offset- int(MAX_BTN)}#{orginal_offset}#{req}"),
             InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}", callback_data="pages",),
             InlineKeyboardButton("ɴᴇxᴛ ›", callback_data=f"season_search#{season}#{key}#{n_offset}#{orginal_offset}#{req}"),])

    btn.append([
        InlineKeyboardButton(text="‹ ʙᴀᴄᴋ ᴛᴏ ᴍᴀɪɴ ᴘᴀɢᴇ", callback_data=f"next_{req}_{key}_{orginal_offset}"),])
    await query.message.edit_text(cap + links + js_ads, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn))
    return

@Client.on_callback_query(filters.regex(r"^years#"))
async def years_cb_handler(client: Client, query: CallbackQuery):
    _, key, offset, req = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer(script.ALRT_TXT, show_alert=True)
    btn  = []
    for i in range(0, len(YEARS)-1, 3):
        btn.append([
            InlineKeyboardButton(
                text=YEARS[i].title(),
                callback_data=f"years_search#{YEARS[i].lower()}#{key}#0#{offset}#{req}"
            ),
            InlineKeyboardButton(
                text=YEARS[i+1].title(),
                callback_data=f"years_search#{YEARS[i+1].lower()}#{key}#0#{offset}#{req}"
            ),
            InlineKeyboardButton(
                text=YEARS[i+2].title(),
                callback_data=f"years_search#{YEARS[i+2].lower()}#{key}#0#{offset}#{req}"
            ),
        ])
    
    btn.append([InlineKeyboardButton(text="‹ ʙᴀᴄᴋ ᴛᴏ ᴍᴀɪɴ ᴘᴀɢᴇ", callback_data=f"next_{req}_{key}_{offset}")])
    await query.message.edit_text("<b>ɪɴ ᴡʜɪᴄʜ ʏᴇᴀʀ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ, ᴄʜᴏᴏsᴇ ғʀᴏᴍ ʜᴇʀᴇ!</b>", reply_markup=InlineKeyboardMarkup(btn))
    return

@Client.on_callback_query(filters.regex(r"^years_search#"))
async def year_search(client: Client, query: CallbackQuery):
    _, year, key, offset, orginal_offset, req = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer(script.ALRT_TXT, show_alert=True)	
    offset = int(offset)
    search = BUTTONS.get(key)
    cap = CAP.get(key)
    if not search:
        await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name),show_alert=True)
        return 
    search = search.replace("_", " ")
    files, n_offset, total = await get_search_results(f"{search} {year}", max_results=int(MAX_BTN), offset=offset)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0
    files = [file for file in files if re.search(year, file.file_name, re.IGNORECASE)]
    if not files:
        await query.answer(f"sᴏʀʀʏ ʏᴇᴀʀ {year.title()} ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ {search}", show_alert=1)
        return

    batch_ids = files
    temp.FILES_ID[f"{query.message.chat.id}-{query.id}"] = batch_ids
    batch_link = f"batchfiles#{query.message.chat.id}#{query.id}#{query.from_user.id}"

    reqnxt = query.from_user.id if query.from_user else 0
    settings = await get_settings(query.message.chat.id)
    temp.CHAT[query.from_user.id] = query.message.chat.id
    ads, ads_name, _ = await mdb.get_advirtisment()
    ads_text = ""
    if ads is not None and ads_name is not None:
        ads_url = f"https://t.me/{temp.U_NAME}?start=ads"
        ads_text = f"<a href={ads_url}>{ads_name}</a>"
    js_ads = f"\n━━━━━━━━━━━━━━━━━━\n <b>{ads_text}</b> \n━━━━━━━━━━━━━━━━━━" if ads_text else ""
    #del_msg = f"\n\n<b>⚠️ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀꜰᴛᴇʀ <code>{get_readable_time(DELETE_TIME)}</code> ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs</b>" if settings["auto_delete"] else ''
    links = ""
    if settings["link"]:
        btn = []
        for file_num, file in enumerate(files, start=offset+1):
            links += f"""<b>\n\n{file_num}. <a href=https://t.me/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}>[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}</a></b>"""
    else:
        btn = [[
                InlineKeyboardButton(text=f"📁 {get_size(file.file_size)} ✦ {formate_file_name(file.file_name)}", callback_data=f'files#{reqnxt}#{file.file_id}'),]
                   for file in files
              ]
        
   
    btn.insert(0,[
	InlineKeyboardButton("sᴇɴᴅ ᴀʟʟ ғɪʟᴇs", callback_data=batch_link),
        ])
    btn.insert(1, [
	InlineKeyboardButton("ꜱᴇᴀꜱᴏɴ", callback_data=f"seasons#{key}#{offset}#{req}"),
        InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ ", callback_data=f"languages#{key}#{offset}#{req}")
    ])    
    
    if n_offset== '':
        btn.append(
            [InlineKeyboardButton(text="🥲 ɴᴏ ᴍᴏʀᴇ ᴘᴀɢᴇs 🥲", callback_data="buttons")]
        )
    elif n_offset == 0:
        btn.append(
            [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data=f"years_search#{year}#{key}#{offset- int(MAX_BTN)}#{orginal_offset}#{req}"),
             InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}", callback_data="pages",),
            ])
    elif offset==0:
        btn.append(
            [InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}",callback_data="pages",),
             InlineKeyboardButton("ɴᴇxᴛ ›", callback_data=f"years_search#{year}#{key}#{n_offset}#{orginal_offset}#{req}"),])
    else:
        btn.append(
            [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data=f"years_search#{year}#{key}#{offset- int(MAX_BTN)}#{orginal_offset}#{req}"),
             InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}", callback_data="pages",),
             InlineKeyboardButton("ɴᴇxᴛ ›", callback_data=f"years_search#{year}#{key}#{n_offset}#{orginal_offset}#{req}"),])

    btn.append([
        InlineKeyboardButton(text="‹ ʙᴀᴄᴋ ᴛᴏ ᴍᴀɪɴ ᴘᴀɢᴇ", callback_data=f"next_{req}_{key}_{orginal_offset}"),])
    await query.message.edit_text(cap + links + js_ads, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn))
    return

@Client.on_callback_query(filters.regex(r"^qualities#"))
async def quality_cb_handler(client: Client, query: CallbackQuery):
    _, key, offset, req = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer(script.ALRT_TXT, show_alert=True)
    btn= []
    for i in range(0, len(QUALITIES)-1, 3):
        btn.append([
            InlineKeyboardButton(
                text=QUALITIES[i].title(),
                callback_data=f"quality_search#{QUALITIES[i].lower()}#{key}#0#{offset}#{req}"
            ),
            InlineKeyboardButton(
                text=QUALITIES[i+1].title(),
                callback_data=f"quality_search#{QUALITIES[i+1].lower()}#{key}#0#{offset}#{req}"
            ),
            InlineKeyboardButton(
                text=QUALITIES[i+2].title(),
                callback_data=f"quality_search#{QUALITIES[i+2].lower()}#{key}#0#{offset}#{req}"
            ),
        ])
    btn.append([InlineKeyboardButton(text="‹ ʙᴀᴄᴋ ᴛᴏ ᴍᴀɪɴ ᴘᴀɢᴇ", callback_data=f"next_{req}_{key}_{offset}")])
    await query.message.edit_text("<b>ɪɴ ᴡʜɪᴄʜ ǫᴜᴀʟɪᴛʏ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ, ᴄʜᴏᴏsᴇ ғʀᴏᴍ ʜᴇʀᴇ!</b>", reply_markup=InlineKeyboardMarkup(btn))
    return

@Client.on_callback_query(filters.regex(r"^quality_search#"))
async def quality_search(client: Client, query: CallbackQuery):
    _, qul, key, offset, orginal_offset, req = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer(script.ALRT_TXT, show_alert=True)	
    offset = int(offset)
    search = BUTTONS.get(key)
    cap = CAP.get(key)
    if not search:
        await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name),show_alert=True)
        return 
    search = search.replace("_", " ")
    files, n_offset, total = await get_search_results(f"{search} {qul}", max_results=int(MAX_BTN), offset=offset)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0
    files = [file for file in files if re.search(qul, file.file_name, re.IGNORECASE)]
    if not files:
        await query.answer(f"sᴏʀʀʏ ǫᴜᴀʟɪᴛʏ {qul.title()} ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ {search}", show_alert=1)
        return

    batch_ids = files
    temp.FILES_ID[f"{query.message.chat.id}-{query.id}"] = batch_ids
    batch_link = f"batchfiles#{query.message.chat.id}#{query.id}#{query.from_user.id}"

    reqnxt = query.from_user.id if query.from_user else 0
    settings = await get_settings(query.message.chat.id)
    temp.CHAT[query.from_user.id] = query.message.chat.id
    ads, ads_name, _ = await mdb.get_advirtisment()
    ads_text = ""
    if ads is not None and ads_name is not None:
        ads_url = f"https://t.me/{temp.U_NAME}?start=ads"
        ads_text = f"<a href={ads_url}>{ads_name}</a>"
    js_ads = f"\n━━━━━━━━━━━━━━━━━━\n <b>{ads_text}</b> \n━━━━━━━━━━━━━━━━━━" if ads_text else ""
  #  del_msg = f"\n\n<b>⚠️ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀꜰᴛᴇʀ <code>{get_readable_time(DELETE_TIME)}</code> ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs</b>" if settings["auto_delete"] else ''
    links = ""
    if settings["link"]:
        btn = []
        for file_num, file in enumerate(files, start=offset+1):
            links += f"""<b>\n\n{file_num}. <a href=https://t.me/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}>[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}</a></b>"""
    else:
        btn = [[
                InlineKeyboardButton(text=f"📁 {get_size(file.file_size)} ✦ {formate_file_name(file.file_name)}", callback_data=f'files#{reqnxt}#{file.file_id}'),]
                   for file in files
              ]
        
 
    btn.insert(0,[
	InlineKeyboardButton("sᴇɴᴅ ᴀʟʟ ғɪʟᴇs", callback_data=batch_link),
        ])
    btn.insert(1, [
	InlineKeyboardButton("ꜱᴇᴀꜱᴏɴ", callback_data=f"seasons#{key}#{offset}#{req}"),
        InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ", callback_data=f"languages#{key}#{offset}#{req}"),
    ])    
    if n_offset== '':
        btn.append(
            [InlineKeyboardButton(text="🥲 ɴᴏ ᴍᴏʀᴇ ᴘᴀɢᴇs 🥲", callback_data="buttons")]
        )
    elif n_offset == 0:
        btn.append(
            [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data=f"quality_search#{qul}#{key}#{offset- int(MAX_BTN)}#{orginal_offset}#{req}"),
             InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}", callback_data="pages",),
            ])
    elif offset==0:
        btn.append(
            [InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}",callback_data="pages",),
             InlineKeyboardButton("ɴᴇxᴛ ›", callback_data=f"quality_search#{qul}#{key}#{n_offset}#{orginal_offset}#{req}"),])
    else:
        btn.append(
            [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data=f"quality_search#{qul}#{key}#{offset- int(MAX_BTN)}#{orginal_offset}#{req}"),
             InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}", callback_data="pages",),
             InlineKeyboardButton("ɴᴇxᴛ ›", callback_data=f"quality_search#{qul}#{key}#{n_offset}#{orginal_offset}#{req}"),])

    btn.append([
        InlineKeyboardButton(text="‹ ʙᴀᴄᴋ ᴛᴏ ᴍᴀɪɴ ᴘᴀɢᴇ", callback_data=f"next_{req}_{key}_{orginal_offset}"),])
    await query.message.edit_text(cap + links + js_ads, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn))
    return
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(btn))

@Client.on_callback_query(filters.regex(r"^languages#"))
async def languages_cb_handler(client: Client, query: CallbackQuery):
    _, key, offset, req = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer(script.ALRT_TXT, show_alert=True)
    btn  = []
    for i in range(0, len(LANGUAGES)-1, 2):
        btn.append([
            InlineKeyboardButton(
                text=LANGUAGES[i].title(),
                callback_data=f"lang_search#{LANGUAGES[i].lower()}#{key}#0#{offset}#{req}"
            ),
            InlineKeyboardButton(
                text=LANGUAGES[i+1].title(),
                callback_data=f"lang_search#{LANGUAGES[i+1].lower()}#{key}#0#{offset}#{req}"
            ),
                    ])
    btn.append([InlineKeyboardButton(text="‹ ʙᴀᴄᴋ ᴛᴏ ᴍᴀɪɴ ᴘᴀɢᴇ", callback_data=f"next_{req}_{key}_{offset}")])
    await query.message.edit_text("<b>ɪɴ ᴡʜɪᴄʜ ʟᴀɴɢᴜᴀɢᴇ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ, ᴄʜᴏᴏsᴇ ғʀᴏᴍ ʜᴇʀᴇ!</b>", reply_markup=InlineKeyboardMarkup(btn))
    return

@Client.on_callback_query(filters.regex(r"^lang_search#"))
async def lang_search(client: Client, query: CallbackQuery):
    _, lang, key, offset, orginal_offset, req = query.data.split("#")
    lang2 = lang[:3]
    if int(req) != query.from_user.id:
        return await query.answer(script.ALRT_TXT, show_alert=True)	
    offset = int(offset)
    search = BUTTONS.get(key)
    cap = CAP.get(key)
    if not search:
        await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name),show_alert=True)
        return 
    search = search.replace("_", " ")
    files, n_offset, total = await get_search_results(f"{search} {lang}", max_results=int(MAX_BTN), offset=offset)
    files2, n_offset2, total2 = await get_search_results(f"{search} {lang2}", max_results=int(MAX_BTN), offset=offset)
    total += total2
    try:
        n_offset = int(n_offset)
    except:
        try: 
            n_offset = int(n_offset2)
        except : 
            n_offset = 0
    files = [file for file in files if re.search(lang, file.file_name, re.IGNORECASE)]
    if not files:
        files = [file for file in files2 if re.search(lang2, file.file_name, re.IGNORECASE)]
        if not files:
            return await query.answer(f"sᴏʀʀʏ ʟᴀɴɢᴜᴀɢᴇ {lang.title()} ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ {search}", show_alert=1)

    batch_ids = files
    temp.FILES_ID[f"{query.message.chat.id}-{query.id}"] = batch_ids
    batch_link = f"batchfiles#{query.message.chat.id}#{query.id}#{query.from_user.id}"

    reqnxt = query.from_user.id if query.from_user else 0
    settings = await get_settings(query.message.chat.id)
    group_id = query.message.chat.id
    temp.CHAT[query.from_user.id] = query.message.chat.id
    ads, ads_name, _ = await mdb.get_advirtisment()
    ads_text = ""
    if ads is not None and ads_name is not None:
        ads_url = f"https://t.me/{temp.U_NAME}?start=ads"
        ads_text = f"<a href={ads_url}>{ads_name}</a>"

    js_ads = f"\n━━━━━━━━━━━━━━━━━━\n <b>{ads_text}</b> \n━━━━━━━━━━━━━━━━━━" if ads_text else ""
    #del_msg = f"\n\n<b>⚠️ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀꜰᴛᴇʀ <code>{get_readable_time(DELETE_TIME)}</code> ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs</b>" if settings["auto_delete"] else ''
    links = ""
    if settings["link"]:
        btn = []
        for file_num, file in enumerate(files, start=offset+1):
            links += f"""<b>\n\n{file_num}. <a href=https://t.me/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}>[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}</a></b>"""
    else:
        btn = [[
                InlineKeyboardButton(text=f"📁 {get_size(file.file_size)} ✦ {formate_file_name(file.file_name)}", callback_data=f'files#{reqnxt}#{file.file_id}'),]
                   for file in files
              ]
        

    btn.insert(0,[
	InlineKeyboardButton("sᴇɴᴅ ᴀʟʟ ғɪʟᴇs", callback_data=batch_link),
        ])
    btn.insert(1, [
	InlineKeyboardButton("ꜱᴇᴀꜱᴏɴ", callback_data=f"seasons#{key}#{offset}#{req}"),
        InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ", callback_data=f"languages#{key}#{offset}#{req}")
    ])    
    if n_offset== '':
        btn.append(
            [InlineKeyboardButton(text="🥲 ɴᴏ ᴍᴏʀᴇ ᴘᴀɢᴇs 🥲", callback_data="buttons")]
        )
    elif n_offset == 0:
        btn.append(
            [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data=f"lang_search#{lang}#{key}#{offset- int(MAX_BTN)}#{orginal_offset}#{req}"),
             InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}", callback_data="pages",),
            ])
    elif offset==0:
        btn.append(
            [InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}",callback_data="pages",),
             InlineKeyboardButton("ɴᴇxᴛ ›", callback_data=f"lang_search#{lang}#{key}#{n_offset}#{orginal_offset}#{req}"),])
    else:
        btn.append(
            [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data=f"lang_search#{lang}#{key}#{offset- int(MAX_BTN)}#{orginal_offset}#{req}"),
             InlineKeyboardButton(f"{math.ceil(offset / int(MAX_BTN)) + 1}/{math.ceil(total / int(MAX_BTN))}", callback_data="pages",),
             InlineKeyboardButton("ɴᴇxᴛ ›", callback_data=f"lang_search#{lang}#{key}#{n_offset}#{orginal_offset}#{req}"),])

    btn.append([
        InlineKeyboardButton(text="‹ ʙᴀᴄᴋ ᴛᴏ ᴍᴀɪɴ ᴘᴀɢᴇ", callback_data=f"next_{req}_{key}_{orginal_offset}"),])
    await query.message.edit_text(cap + links + js_ads, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn))
    return
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(btn))

@Client.on_callback_query(filters.regex(r"^spol"))
async def advantage_spoll_choker(bot, query):
    _, id, user = query.data.split('#')
    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer(script.ALRT_TXT, show_alert=True)
    movie = await get_poster(id, id=True)
    search = movie.get('title')
    await query.answer('ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ 🥶')
    files, offset, total_results = await get_search_results(search)
    if files:
        k = (search, files, offset, total_results)
        await auto_filter(bot, query, k)
    else:
        k = await query.message.edit(script.NO_RESULT_TXT)
        await asyncio.sleep(60)
        await k.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        try:
            user = query.message.reply_to_message.from_user.id
        except:
            user = query.from_user.id
        if int(user) != 0 and query.from_user.id != int(user):
            return await query.answer(script.ALRT_TXT, show_alert=True)
        await query.answer("ᴄʟᴏsɪɴɢ ʙᴀʙʏ")
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif query.data == "delallcancel":
        userid = query.from_user.id
        chat_type = query.message.chat.type
        if chat_type == enums.ChatType.PRIVATE:
            await query.message.reply_to_message.delete()
            await query.message.delete()
        elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            grp_id = query.message.chat.id
            st = await client.get_chat_member(grp_id, userid)
            if (st.status == enums.ChatMemberStatus.OWNER) or (str(userid) in ADMINS):
                await query.message.delete()
                try:
                    await query.message.reply_to_message.delete()
                except:
                    pass
            else:
                await query.answer(script.ALRT_TXT.format(query.from_user.first_name), show_alert=True)    

    elif query.data.startswith("checksub"):
        ident, file_id , grp_id = query.data.split("#")
        if grp_id != 'None' or grp_id != '':
            chat_id = grp_id
        else:
            chat_id = query.message.chat.id
        if AUTH_CHANNEL and not await is_req_subscribed(client, query):
            await query.answer("ɪ ʟɪᴋᴇ ʏᴏᴜʀ sᴍᴀʀᴛɴᴇss ʙᴜᴛ ᴅᴏɴ'ᴛ ʙᴇ ᴏᴠᴇʀsᴍᴀʀᴛ 😒\nꜰɪʀsᴛ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ 😒", show_alert=True)
            return         
        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('ɴᴏ sᴜᴄʜ ꜰɪʟᴇ ᴇxɪsᴛs 🚫')
        files = files_[0]
        btn = [[
            InlineKeyboardButton('• ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇ •', url=f'https://t.me/{temp.U_NAME}?start=file_{chat_id}_{file_id}')
        ]]
        reply_markup = InlineKeyboardMarkup(btn)
        return await query.message.edit(text=f'<b>ᴛʜᴀɴᴋs ғᴏʀ ᴊᴏɪɴɪɴɢ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ 🔥😗\nɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇ : {files.file_name[:20]}.. ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ⚡</b>',reply_markup=reply_markup)

    elif query.data == "give_trial":
        user_id = query.from_user.id
        has_free_trial = await db.check_trial_status(user_id)
        if has_free_trial:
            await query.answer(" ʏᴏᴜ'ᴠᴇ ᴀʟʀᴇᴀᴅʏ ᴄʟᴀɪᴍᴇᴅ ʏᴏᴜʀ ꜰʀᴇᴇ ᴛʀɪᴀʟ ᴏɴᴄᴇ !\n\n📌 ᴄʜᴇᴄᴋᴏᴜᴛ ᴏᴜʀ ᴘʟᴀɴꜱ ʙʏ : /plan", show_alert=True)
            return
        else:            
            await db.give_free_trial(user_id)
            await query.message.edit_text(
                text="ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴꜱ🎉 ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ꜰʀᴇᴇ ᴛʀᴀɪʟ ꜰᴏʀ <u>5 ᴍɪɴᴜᴛᴇs</u> ꜰʀᴏᴍ ɴᴏᴡ !\n\nɴᴏᴡ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ꜱᴇʀᴠɪᴄᴇ ꜰᴏʀ 5 ᴍɪɴᴜᴛᴇꜱ. ᴛᴏ ʙᴜʏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ꜱᴇʀᴠɪᴄᴇ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.",
                disable_web_page_preview=True,                  
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💸 ᴄʜᴇᴄᴋᴏᴜᴛ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ 💸", callback_data='seeplans')]]))
            await client.send_message(LOG_CHANNEL, text=f"#FREE_TRAIL_CLAIMED\n\n👤 ᴜꜱᴇʀ ɴᴀᴍᴇ - {query.from_user.mention}\n⚡ ᴜꜱᴇʀ ɪᴅ - {user_id}", disable_web_page_preview=True)
            return   
	
    elif query.data.startswith("stream"):
        user_id = query.from_user.id
        file_id = query.data.split('#', 1)[1]
        log_msg = await client.send_cached_media(
        chat_id=LOG_CHANNEL,
        file_id=file_id
        )
        fileName = quote_plus(get_name(log_msg))
        online = f"{URL}watch/{log_msg.id}/{fileName}?hash={get_hash(log_msg)}"
        download = f"{URL}{log_msg.id}/{fileName}?hash={get_hash(log_msg)}"
        btn = [[
            InlineKeyboardButton("• ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ •", url=online),
            InlineKeyboardButton("• ꜰᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ •", url=download)
        ],[
            InlineKeyboardButton('↺ ᴄʟᴏsᴇ', callback_data='close_data')
	]]
        await query.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(btn)
	)
        username = query.from_user.username
        await log_msg.reply_text(
            text=f"#LinkGenrated\n\nIᴅ : <code>{user_id}</code>\nUꜱᴇʀɴᴀᴍᴇ : {username}\n\nNᴀᴍᴇ : {fileName}",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("🚀 ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᴀᴅ", url=download),
                    InlineKeyboardButton('ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 🧿', url=online)
                ]
            ])
	)
	
    elif query.data == "buttons":
        await query.answer("ɴᴏ ᴍᴏʀᴇ ᴘᴀɢᴇs! 💀", show_alert=True)

    elif query.data == "pages":
        await query.answer("ᴛʜɪs ɪs ᴘᴀɢᴇs ʙᴜᴛᴛᴏɴ! 👀")

    elif query.data.startswith("lang_art"):
        _, lang = query.data.split("#")
        await query.answer(f"ʏᴏᴜ sᴇʟᴇᴄᴛᴇᴅ {lang.title()} ʟᴀɴɢᴜᴀɢᴇ ⚡️", show_alert=True)


    elif query.data == "start":
        buttons = [[
                InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴀʙʏ ➕', url=f'http://t.me/{temp.U_NAME}?startgroup=start')
                ],[
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", callback_data='support'),
                InlineKeyboardButton('✧ ᴀʙᴏᴜᴛ ᴍᴇ ✧', callback_data=f'about')
                ],[
                InlineKeyboardButton('ᴘʀᴇᴍɪᴜᴍ', callback_data='seeplans'),
                InlineKeyboardButton('✘ ʜᴇʟᴘ & ᴄᴍᴅ ✘', callback_data="features")
                ],[
                InlineKeyboardButton('💰 ᴇᴀʀɴ ᴍᴏɴᴇʏ ᴡɪᴛʜ ʙᴏᴛ 💸', callback_data="earn")
                ]] 
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, get_status(), query.from_user.id),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )      
    elif query.data == "seeplans":
        btn = [[
            InlineKeyboardButton('• ᴀʟʟ ᴘʟᴀɴs ғᴏʀ ᴘʀᴇᴍɪᴜᴍ •', callback_data='free')
	],[
	    InlineKeyboardButton('• ɢᴇᴛ ғʀᴇᴇ ᴘʀᴇᴍɪᴜᴍ •', callback_data='reffff')	
        ],[
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(btn)
        m=await query.message.reply_sticker("CAACAgQAAxkBAAEiLZ9l7VMuTY7QHn4edR6ouHUosQQ9gwACFxIAArzT-FOmYU0gLeJu7x4E") 
        await m.delete()
        await query.message.reply_photo(
            photo=random.choice(PREMIUM_PIC),
            caption=script.PREPLANS_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)
    elif query.data == "free":
        buttons = [[
            InlineKeyboardButton('📸 sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ʜᴇʀᴇ •', url=f'https://t.me/vampirexgirl')
        ],[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='broze'),
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)             
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PAYPICS))
        )
        await query.message.edit_text(
            text=script.FREE_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )   
    #jisshu
    elif query.data == "broze":
       buttons = [[
           InlineKeyboardButton('• ᴀʟʟ ᴘʟᴀɴs ғᴏʀ ᴘʀᴇᴍɪᴜᴍ •', callback_data='free')
       ],[
	   InlineKeyboardButton('• ɢᴇᴛ ғʀᴇᴇ ᴘʀᴇᴍɪᴜᴍ •', callback_data='reffff')	      
       ],[
           InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
       ]]
       reply_markup = InlineKeyboardMarkup(buttons)
  
       await query.message.edit_media(
         media=InputMediaPhoto(
            media=random.choice(PREMIUM_PIC),
            caption=script.PREPLANSS_TXT.format(query.from_user.mention()),
            parse_mode=enums.ParseMode.HTML
         ),
         reply_markup=reply_markup
       )
        

    elif query.data == "ref_point":
        await query.answer(f'You Have: {referdb.get_refer_points(query.from_user.id)} Refferal points.', show_alert=True)

    elif query.data == "verifyon":
        await query.answer(f'Only the bot admin can ᴏɴ ✓ or ᴏғғ ✗ this feature.', show_alert=True)
    
    elif query.data == "features":
        buttons = [[
              InlineKeyboardButton('• sᴇᴛᴛɪɴɢs •', callback_data='settings_lol'),
              InlineKeyboardButton('• ɢʀᴏᴜᴘ sᴇᴛᴜᴘs •', callback_data='helpx'),
              ], [
              InlineKeyboardButton('• ᴏᴡɴᴇʀ ᴄᴍᴅs •', callback_data='admincmd'),
              InlineKeyboardButton('• ᴇxᴛʀᴀ ᴄᴍᴅs •', callback_data='extra_cmds')
              ], [
              InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='start')
              ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
    
        await query.message.edit_media(
            media=InputMediaPhoto(
            media=random.choice(PICS),
            caption=script.HELP_TXT.format(query.from_user.mention),
            parse_mode=enums.ParseMode.HTML 
            ),
            reply_markup=reply_markup
	)
      #  await query.message.edit_text(
      #      text=script.HELP_TXT,
      #      reply_markup=reply_markup,
       #     parse_mode=enums.ParseMode.HTML
       # )   
        
    elif query.data == "admincmd":
    # If the user isn't an admin, return
      if query.from_user.id not in ADMINS:
        return await query.answer('ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙʀᴏ!', show_alert=True)
    
      buttons = [[
	      InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='features'),
	      InlineKeyboardButton('ɴᴇxᴛ ›', callback_data='admincmd2'),
      ]]
      reply_markup = InlineKeyboardMarkup(buttons)
    
      await client.edit_message_media(
          chat_id=query.message.chat.id,
          message_id=query.message.id,
          media=InputMediaAnimation(
            media="https://cdn.jsdelivr.net/gh/Jisshubot/JISSHU_BOTS/Video.mp4/Welcome_video_20240921_184741_0001.gif",
            caption=script.ADMIN_CMD_TXT,
            parse_mode=enums.ParseMode.HTML
          ),
          reply_markup=reply_markup
          )

    elif query.data == "admincmd2":
       buttons = [[
	      InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='admincmd')]]
       reply_markup = InlineKeyboardMarkup(buttons)
    
       await client.edit_message_media(
          chat_id=query.message.chat.id,
          message_id=query.message.id,
          media=InputMediaAnimation(
            media="https://cdn.jsdelivr.net/gh/Jisshubot/JISSHU_BOTS/Video.mp4/Welcome_video_20240921_184741_0001.gif",
            caption=script.ADMIN_CMD_TXT2,
            parse_mode=enums.ParseMode.HTML
          ),
          reply_markup=reply_markup
      )
	    

    elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('• sᴜᴘᴘᴏʀᴛ •', callback_data='support'),
            InlineKeyboardButton('• ʏᴏᴜᴛᴜʙᴇ •', callback_data='youtube')
        ],[
            InlineKeyboardButton('✘ ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅ ✘', callback_data='features')
        ],[
            InlineKeyboardButton('© ᴅɪsᴄʟᴀɪᴍᴇʀ ©', callback_data='disclaimer')
        ],[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='start'),
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)    
        	
    
    elif query.data == "mydevelopers":
        await query.answer("Meet the minds behind this bot:\n\n👨‍💻 @JISSHU_BOTS\n👨‍💻 @IM_JISSHU\n👨‍💻 @JOYBOY_ZORO\n👨‍💻 @TG_Anonymous_Official\n\n\n❤️ A big thank you for making this bot awesome!", show_alert=True)
 
    

    elif query.data == "youtube":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(YT_PIC))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.YT_TEXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)
	
    elif query.data == "disclaimer":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.DISCLAIMER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)
    

    elif query.data == "earn":
            btn = [[
                     InlineKeyboardButton('• ᴀʟʟ ᴅᴇᴛᴀɪʟs ᴄᴏᴍᴍᴀɴᴅs •', callback_data='helpx')
                 ],[ 
                     InlineKeyboardButton('• ᴄᴏɴᴛᴀᴄᴛ sᴜᴘᴘᴏʀᴛ •', url=f'http://t.me/Vampirexgirl')
                 ],[
		     InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data="start"),
	             InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
                  ]]
            await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto(random.choice(PICS))
            )
            reply_markup = InlineKeyboardMarkup(btn)
            await query.message.edit_text(
                text=script.GROUP_TEXT,
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
	    )
	    
    
    elif query.data == "extra_cmds":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='features')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)  
        await query.message.edit_text(
            text=script.EXTRA_CMDS_TEXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    
	
    elif query.data == "support":
        buttons = [[
            InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ', url=f'https://t.me/top10ner_0'),
            InlineKeyboardButton('ɢʀᴏᴜᴘ', url=f'https://t.me/request_movie2')
        ],[
            InlineKeyboardButton('ʀᴇᴘᴏʀᴛ ʙᴜɢs ᴀɴᴅ ғᴇᴇᴅʙᴀᴄᴋ', url=f'https://t.me/noob_marcus'),
        ],[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='start'),
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=f"<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ, ɢʀᴏᴜᴘ, ʙᴏᴛ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ.\n\n» sᴜᴘᴘᴏʀᴛ ᴍᴇ ɢᴜʏs 💜</b>",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)

	
    elif query.data == "helpx":
        buttons = [[
            InlineKeyboardButton('• sᴇᴛ ᴠᴇʀɪғʏ •', callback_data='set_verifyx'),
	    InlineKeyboardButton('• sᴇᴛ ᴛᴜᴛᴏʀɪᴀʟ •', callback_data='set_tutorialx')
	],[ 	
	    InlineKeyboardButton('• sᴇᴛ ғᴏʀᴄᴇ ᴄʜᴀɴɴᴇʟ •', callback_data='fsub'),
            InlineKeyboardButton('• sᴇᴛ ᴄᴀᴘᴛɪᴏɴ •', callback_data='set_captionx')
	],[ 	
            InlineKeyboardButton('•sᴇᴛ ᴛᴇᴍᴘʟᴀᴛᴇ •', callback_data='set_templatex'),
            InlineKeyboardButton('• sᴇᴛ ʟᴏɢ ᴄʜᴀɴɴᴇʟ •', callback_data='set_log_channelx')
	],[      
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='features'),
	    InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.GENERAL_INFO_TEXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)

    elif query.data == "set_verifyx":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='helpx'),
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SET_VERIFY_TEXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)    
        

    elif query.data == "set_captionx":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='helpx'),
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SET_CAPTION_TEXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)    
        

    elif query.data == "set_templatex":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='helpx'),
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SET_TEMPLATE_TEXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)    
        

    elif query.data == "set_tutorialx":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='helpx'),
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SET_TUTORIAL_TEXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)    
        

    elif query.data == "set_log_channelx":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='helpx'),
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SET_LOG_CHANNEL_TEXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)    

    elif query.data == "fsub":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='helpx'),
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.FSUB_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)
	    
    elif query.data == "settings_lol":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='features')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SETTINGS_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
	    
    elif query.data == "rule":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ', callback_data='helpx')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(RULES_PIC))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.RULES_TEXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)
	    
    elif query.data == "rules":
        buttons = [[
            InlineKeyboardButton('× ᴄʟᴏsᴇ ×', callback_data='close_data')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(RULES_PIC))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.RULES_TEXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
	)
	
    elif query.data == "all_files_delete":
        files = await Media.count_documents()
        await query.answer('Deleting...')
        await Media.collection.drop()
        await query.message.edit_text(f"Successfully deleted {files} files")
        
    elif query.data.startswith("killfilesak"):
        ident, keyword = query.data.split("#")
        await query.message.edit_text(f"<b>ꜰᴇᴛᴄʜɪɴɢ ꜰɪʟᴇs ꜰᴏʀ ʏᴏᴜʀ ǫᴜᴇʀʏ {keyword} ᴏɴ ᴅʙ...\n\nᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...</b>")
        files, total = await get_bad_files(keyword)
        await query.message.edit_text(f"<b>ꜰᴏᴜɴᴅ {total} ꜰɪʟᴇs ꜰᴏʀ ʏᴏᴜʀ ǫᴜᴇʀʏ {keyword}!!</b>")
        deleted = 0
        async with lock:
            try:
                for file in files:
                    file_ids = file.file_id
                    file_name = file.file_name
                    result = await Media.collection.delete_one({
                        '_id': file_ids,
                    })
                    if result.deleted_count:
                        print(f'Successfully deleted {file_name} from database.')
                    deleted += 1
                    if deleted % 20 == 0:
                        await query.message.edit_text(f"<b>Process started for deleting files from DB. Successfully deleted {str(deleted)} files from DB for your query {keyword} !\n\nPlease wait...</b>")
            except Exception as e:
                print(e)
                await query.message.edit_text(f'Error: {e}')
            else:
                await query.message.edit_text(f"<b>Process Completed for file deletion !\n\nSuccessfully deleted {str(deleted)} files from database for your query {keyword}.</b>")
          
    elif query.data.startswith("reset_grp_data"):
        grp_id = query.message.chat.id
        btn = [[
            InlineKeyboardButton('× ᴄʟᴏsᴇ ×', callback_data='close_data')
        ]]           
        reply_markup=InlineKeyboardMarkup(btn)
        await save_group_settings(grp_id, 'shortner', SHORTENER_WEBSITE)
        await save_group_settings(grp_id, 'api', SHORTENER_API)
        await save_group_settings(grp_id, 'shortner_two', SHORTENER_WEBSITE2)
        await save_group_settings(grp_id, 'api_two', SHORTENER_API2)
        await save_group_settings(grp_id, 'shortner_three', SHORTENER_WEBSITE3)
        await save_group_settings(grp_id, 'api_three', SHORTENER_API3)
        await save_group_settings(grp_id, 'verify_time', TWO_VERIFY_GAP)
        await save_group_settings(grp_id, 'third_verify_time', THREE_VERIFY_GAP)
        await save_group_settings(grp_id, 'tutorial', TUTORIAL)
        await save_group_settings(grp_id, 'tutorial_2', TUTORIAL_2)
        await save_group_settings(grp_id, 'tutorial_3', TUTORIAL_3)
        await save_group_settings(grp_id, 'template', IMDB_TEMPLATE)
        await save_group_settings(grp_id, 'caption', FILE_CAPTION)
        await save_group_settings(grp_id, 'log', LOG_VR_CHANNEL)
        await query.answer('ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ ʀᴇꜱᴇᴛ...')
        await query.message.edit_text("<b>ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ ʀᴇꜱᴇᴛ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ...\n\nɴᴏᴡ ꜱᴇɴᴅ /details ᴀɢᴀɪɴ</b>", reply_markup=reply_markup)

    elif query.data.startswith("setgs"):
        ident, set_type, status, grp_id = query.data.split("#")
        userid = query.from_user.id if query.from_user else None
        if not await is_check_admin(client, int(grp_id), userid):
            await query.answer(script.ALRT_TXT, show_alert=True)
            return
        if status == "True":
            await save_group_settings(int(grp_id), set_type, False)
            await query.answer("ᴏғғ ❌")
        else:
            await save_group_settings(int(grp_id), set_type, True)
            await query.answer("ᴏɴ ✅")
        settings = await get_settings(int(grp_id))      
        if settings is not None:
            buttons = [[
                InlineKeyboardButton('ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ', callback_data=f'setgs#auto_filter#{settings["auto_filter"]}#{grp_id}'),
                InlineKeyboardButton('ᴏɴ ✓' if settings["auto_filter"] else 'ᴏғғ ✗', callback_data=f'setgs#auto_filter#{settings["auto_filter"]}#{grp_id}')
            ],[
                InlineKeyboardButton('ɪᴍᴅʙ', callback_data=f'setgs#imdb#{settings["imdb"]}#{grp_id}'),
                InlineKeyboardButton('ᴏɴ ✓' if settings["imdb"] else 'ᴏғғ ✗', callback_data=f'setgs#imdb#{settings["imdb"]}#{grp_id}')
            ],[
                InlineKeyboardButton('sᴘᴇʟʟ ᴄʜᴇᴄᴋ', callback_data=f'setgs#spell_check#{settings["spell_check"]}#{grp_id}'),
                InlineKeyboardButton('ᴏɴ ✓' if settings["spell_check"] else 'ᴏғғ ✗', callback_data=f'setgs#spell_check#{settings["spell_check"]}#{grp_id}')
            ],[
                InlineKeyboardButton('ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ', callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{grp_id}'),
                InlineKeyboardButton(f'{get_readable_time(DELETE_TIME)}' if settings["auto_delete"] else 'ᴏғғ ✗', callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{grp_id}')
            ],[
                InlineKeyboardButton('ʀᴇsᴜʟᴛ ᴍᴏᴅᴇ', callback_data=f'setgs#link#{settings["link"]}#{str(grp_id)}'),
                InlineKeyboardButton('⛓ ʟɪɴᴋ' if settings["link"] else '🧲 ʙᴜᴛᴛᴏɴ', callback_data=f'setgs#link#{settings["link"]}#{str(grp_id)}')
            ],[
                InlineKeyboardButton('× ᴄʟᴏsᴇ ×', callback_data='close_data')
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            d = await query.message.edit_reply_markup(reply_markup)
            await asyncio.sleep(300)
            await d.delete()
        else:
            await query.message.edit_text("<b>ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ</b>")
            
    elif query.data.startswith("show_options"):
        ident, user_id, msg_id = query.data.split("#")
        chnl_id = query.message.chat.id
        userid = query.from_user.id
        buttons = [[
            InlineKeyboardButton("✅️ ᴀᴄᴄᴇᴘᴛ ᴛʜɪꜱ ʀᴇǫᴜᴇꜱᴛ ✅️", callback_data=f"accept#{user_id}#{msg_id}")
        ],[
            InlineKeyboardButton("🚫 ʀᴇᴊᴇᴄᴛ ᴛʜɪꜱ ʀᴇǫᴜᴇꜱᴛ 🚫", callback_data=f"reject#{user_id}#{msg_id}")
        ]]
        try:
            st = await client.get_chat_member(chnl_id, userid)
            if (st.status == enums.ChatMemberStatus.ADMINISTRATOR) or (st.status == enums.ChatMemberStatus.OWNER):
                await query.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
            elif st.status == enums.ChatMemberStatus.MEMBER:
                await query.answer(script.ALRT_TXT, show_alert=True)
        except pyrogram.errors.exceptions.bad_request_400.UserNotParticipant:
            await query.answer("⚠️ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀ ᴍᴇᴍʙᴇʀ ᴏꜰ ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ, ꜰɪʀꜱᴛ ᴊᴏɪɴ", show_alert=True)

    elif query.data.startswith("reject"):
        ident, user_id, msg_id = query.data.split("#")
        chnl_id = query.message.chat.id
        userid = query.from_user.id
        buttons = [[
            InlineKeyboardButton("✗ ʀᴇᴊᴇᴄᴛ ✗", callback_data=f"rj_alert#{user_id}")
        ]]
        btn = [[
            InlineKeyboardButton("♻️ ᴠɪᴇᴡ sᴛᴀᴛᴜs ♻️", url=f"{query.message.link}")
        ]]
        st = await client.get_chat_member(chnl_id, userid)
        if (st.status == enums.ChatMemberStatus.ADMINISTRATOR) or (st.status == enums.ChatMemberStatus.OWNER):
            user = await client.get_users(user_id)
            request = query.message.text
            await query.answer("Message sent to requester")
            await query.message.edit_text(f"<s>{request}</s>")
            await query.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
            try:
                await client.send_message(chat_id=user_id, text="<b>sᴏʀʀʏ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ʀᴇᴊᴇᴄᴛᴇᴅ 😶</b>", reply_markup=InlineKeyboardMarkup(btn))
            except UserIsBlocked:
                await client.send_message(SUPPORT_GROUP, text=f"<b>💥 ʜᴇʟʟᴏ {user.mention},\n\nsᴏʀʀʏ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ʀᴇᴊᴇᴄᴛᴇᴅ 😶</b>", reply_markup=InlineKeyboardMarkup(btn), reply_to_message_id=int(msg_id))
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("accept"):
        ident, user_id, msg_id = query.data.split("#")
        chnl_id = query.message.chat.id
        userid = query.from_user.id
        buttons = [[
            InlineKeyboardButton("😊 ᴀʟʀᴇᴀᴅʏ ᴀᴠᴀɪʟᴀʙʟᴇ 😊", callback_data=f"already_available#{user_id}#{msg_id}")
        ],[
            InlineKeyboardButton("‼️ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ‼️", callback_data=f"not_available#{user_id}#{msg_id}")
        ],[
            InlineKeyboardButton("🥵 ᴛᴇʟʟ ᴍᴇ ʏᴇᴀʀ/ʟᴀɴɢᴜᴀɢᴇ 🥵", callback_data=f"year#{user_id}#{msg_id}")
        ],[
            InlineKeyboardButton("🙃 ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ 1 ʜᴏᴜʀ 🙃", callback_data=f"upload_in#{user_id}#{msg_id}")
        ],[
            InlineKeyboardButton("☇ ᴜᴘʟᴏᴀᴅᴇᴅ ☇", callback_data=f"uploaded#{user_id}#{msg_id}")
        ]]
        try:
            st = await client.get_chat_member(chnl_id, userid)
            if (st.status == enums.ChatMemberStatus.ADMINISTRATOR) or (st.status == enums.ChatMemberStatus.OWNER):
                await query.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
            elif st.status == enums.ChatMemberStatus.MEMBER:
                await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name),show_alert=True)
        except pyrogram.errors.exceptions.bad_request_400.UserNotParticipant:
            await query.answer("⚠️ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀ ᴍᴇᴍʙᴇʀ ᴏꜰ ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ, ꜰɪʀꜱᴛ ᴊᴏɪɴ", show_alert=True)

    elif query.data.startswith("not_available"):
        ident, user_id, msg_id = query.data.split("#")
        chnl_id = query.message.chat.id
        userid = query.from_user.id
        buttons = [[
            InlineKeyboardButton("🚫 ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ 🚫", callback_data=f"na_alert#{user_id}")
        ]]
        btn = [[
            InlineKeyboardButton("♻️ ᴠɪᴇᴡ sᴛᴀᴛᴜs ♻️", url=f"{query.message.link}")
        ]]
        st = await client.get_chat_member(chnl_id, userid)
        if (st.status == enums.ChatMemberStatus.ADMINISTRATOR) or (st.status == enums.ChatMemberStatus.OWNER):
            user = await client.get_users(user_id)
            request = query.message.text
            await query.answer("Message sent to requester")
            await query.message.edit_text(f"<s>{request}</s>")
            await query.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
            try:
                await client.send_message(chat_id=user_id, text="<b>sᴏʀʀʏ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ 😢</b>", reply_markup=InlineKeyboardMarkup(btn))
            except UserIsBlocked:
                await client.send_message(SUPPORT_GROUP, text=f"<b>💥 ʜᴇʟʟᴏ {user.mention},\n\nsᴏʀʀʏ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ 😢</b>", reply_markup=InlineKeyboardMarkup(btn), reply_to_message_id=int(msg_id))
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("uploaded"):
        ident, user_id, msg_id = query.data.split("#")
        chnl_id = query.message.chat.id
        userid = query.from_user.id
        buttons = [[
            InlineKeyboardButton("🙂 ᴜᴘʟᴏᴀᴅᴇᴅ 🙂", callback_data=f"ul_alert#{user_id}")
        ]]
        btn = [[
            InlineKeyboardButton("♻️ ᴠɪᴇᴡ sᴛᴀᴛᴜs ♻️", url=f"{query.message.link}")
        ]]
        st = await client.get_chat_member(chnl_id, userid)
        if (st.status == enums.ChatMemberStatus.ADMINISTRATOR) or (st.status == enums.ChatMemberStatus.OWNER):
            user = await client.get_users(user_id)
            request = query.message.text
            await query.answer("Message sent to requester")
            await query.message.edit_text(f"<s>{request}</s>")
            await query.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
            try:
                await client.send_message(chat_id=user_id, text="<b>ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ᴜᴘʟᴏᴀᴅᴇᴅ ☺️</b>", reply_markup=InlineKeyboardMarkup(btn))
            except UserIsBlocked:
                await client.send_message(SUPPORT_GROUP, text=f"<b>💥 ʜᴇʟʟᴏ {user.mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ᴜᴘʟᴏᴀᴅᴇᴅ ☺️</b>", reply_markup=InlineKeyboardMarkup(btn), reply_to_message_id=int(msg_id))
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("already_available"):
        ident, user_id, msg_id = query.data.split("#")
        chnl_id = query.message.chat.id
        userid = query.from_user.id
        buttons = [[
            InlineKeyboardButton("🫤 ᴀʟʀᴇᴀᴅʏ ᴀᴠᴀɪʟᴀʙʟᴇ 🫤", callback_data=f"aa_alert#{user_id}")
        ]]
        btn = [[
            InlineKeyboardButton("♻️ ᴠɪᴇᴡ sᴛᴀᴛᴜs ♻️", url=f"{query.message.link}")
        ]]
        st = await client.get_chat_member(chnl_id, userid)
        if (st.status == enums.ChatMemberStatus.ADMINISTRATOR) or (st.status == enums.ChatMemberStatus.OWNER):
            user = await client.get_users(user_id)
            request = query.message.text
            await query.answer("Message sent to requester")
            await query.message.edit_text(f"<s>{request}</s>")
            await query.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
            try:
                await client.send_message(chat_id=user_id, text="<b>ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴠᴀɪʟᴀʙʟᴇ 😋</b>", reply_markup=InlineKeyboardMarkup(btn))
            except UserIsBlocked:
                await client.send_message(SUPPORT_GROUP, text=f"<b>💥 ʜᴇʟʟᴏ {user.mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴠᴀɪʟᴀʙʟᴇ 😋</b>", reply_markup=InlineKeyboardMarkup(btn), reply_to_message_id=int(msg_id))
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("upload_in"):
        ident, user_id, msg_id = query.data.split("#")
        chnl_id = query.message.chat.id
        userid = query.from_user.id
        buttons = [[
            InlineKeyboardButton("😌 ᴜᴘʟᴏᴀᴅ ɪɴ 1 ʜᴏᴜʀꜱ 😌", callback_data=f"upload_alert#{user_id}")
        ]]
        btn = [[
            InlineKeyboardButton("♻️ ᴠɪᴇᴡ sᴛᴀᴛᴜs ♻️", url=f"{query.message.link}")
        ]]
        st = await client.get_chat_member(chnl_id, userid)
        if (st.status == enums.ChatMemberStatus.ADMINISTRATOR) or (st.status == enums.ChatMemberStatus.OWNER):
            user = await client.get_users(user_id)
            request = query.message.text
            await query.answer("Message sent to requester")
            await query.message.edit_text(f"<s>{request}</s>")
            await query.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
            try:
                await client.send_message(chat_id=user_id, text="<b>ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ᴡɪᴛʜɪɴ 1 ʜᴏᴜʀ 😁</b>", reply_markup=InlineKeyboardMarkup(btn))
            except UserIsBlocked:
                await client.send_message(SUPPORT_GROUP, text=f"<b>💥 ʜᴇʟʟᴏ {user.mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ᴡɪᴛʜɪɴ 1 ʜᴏᴜʀ 😁</b>", reply_markup=InlineKeyboardMarkup(btn), reply_to_message_id=int(msg_id))
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("year"):
        ident, user_id, msg_id = query.data.split("#")
        chnl_id = query.message.chat.id
        userid = query.from_user.id
        buttons = [[
            InlineKeyboardButton("⚠️ ᴛᴇʟʟ ᴍᴇ ʏᴇᴀʀꜱ & ʟᴀɴɢᴜᴀɢᴇ ⚠️", callback_data=f"yrs_alert#{user_id}")
        ]]
        btn = [[
            InlineKeyboardButton("♻️ ᴠɪᴇᴡ sᴛᴀᴛᴜs ♻️", url=f"{query.message.link}")
        ]]
        st = await client.get_chat_member(chnl_id, userid)
        if (st.status == enums.ChatMemberStatus.ADMINISTRATOR) or (st.status == enums.ChatMemberStatus.OWNER):
            user = await client.get_users(user_id)
            request = query.message.text
            await query.answer("Message sent to requester")
            await query.message.edit_text(f"<s>{request}</s>")
            await query.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
            try:
                await client.send_message(chat_id=user_id, text="<b>ʙʀᴏ ᴘʟᴇᴀꜱᴇ ᴛᴇʟʟ ᴍᴇ ʏᴇᴀʀꜱ ᴀɴᴅ ʟᴀɴɢᴜᴀɢᴇ, ᴛʜᴇɴ ɪ ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ 😬</b>", reply_markup=InlineKeyboardMarkup(btn))
            except UserIsBlocked:
                await client.send_message(SUPPORT_GROUP, text=f"<b>💥 ʜᴇʟʟᴏ {user.mention},\n\nʙʀᴏ ᴘʟᴇᴀꜱᴇ ᴛᴇʟʟ ᴍᴇ ʏᴇᴀʀꜱ ᴀɴᴅ ʟᴀɴɢᴜᴀɢᴇ, ᴛʜᴇɴ ɪ ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ 😬</b>", reply_markup=InlineKeyboardMarkup(btn), reply_to_message_id=int(msg_id))
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("rj_alert"):
        ident, user_id = query.data.split("#")
        userid = query.from_user.id
        if str(userid) in user_id:
            await query.answer("sᴏʀʀʏ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ʀᴇᴊᴇᴄᴛ", show_alert=True)
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("na_alert"):
        ident, user_id = query.data.split("#")
        userid = query.from_user.id
        if str(userid) in user_id:
            await query.answer("sᴏʀʀʏ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ", show_alert=True)
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("ul_alert"):
        ident, user_id = query.data.split("#")
        userid = query.from_user.id
        if str(userid) in user_id:
            await query.answer("ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ᴜᴘʟᴏᴀᴅᴇᴅ", show_alert=True)
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("aa_alert"):
        ident, user_id = query.data.split("#")
        userid = query.from_user.id
        if str(userid) in user_id:
            await query.answer("ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴠᴀɪʟᴀʙʟᴇ", show_alert=True)
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("upload_alert"):
        ident, user_id = query.data.split("#")
        userid = query.from_user.id
        if str(userid) in user_id:
            await query.answer("ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ᴡɪᴛʜɪɴ 1 ʜᴏᴜʀ 😁", show_alert=True)
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("yrs_alert"):
        ident, user_id = query.data.split("#")
        userid = query.from_user.id
        if str(userid) in user_id:
            await query.answer("ʙʀᴏ ᴘʟᴇᴀꜱᴇ ᴛᴇʟʟ ᴍᴇ ʏᴇᴀʀꜱ ᴀɴᴅ ʟᴀɴɢᴜᴀɢᴇ, ᴛʜᴇɴ ɪ ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ 😬", show_alert=True)
        else:
            await query.answer(script.ALRT_TXT, show_alert=True)

    elif query.data.startswith("batchfiles"):
        ident, group_id, message_id, user = query.data.split("#")
        group_id = int(group_id)
        message_id = int(message_id)
        user = int(user)
        if user != query.from_user.id:
            await query.answer(script.ALRT_TXT, show_alert=True)
            return
        link = f"https://telegram.me/{temp.U_NAME}?start=allfiles_{group_id}-{message_id}"
        await query.answer(url=link)
        return
async def ai_spell_check(wrong_name):
    async def search_movie(wrong_name):
        search_results = imdb.search_movie(wrong_name)
        movie_list = [movie['title'] for movie in search_results]
        return movie_list
    movie_list = await search_movie(wrong_name)
    if not movie_list:
        return
    for _ in range(5):
        closest_match = process.extractOne(wrong_name, movie_list)
        if not closest_match or closest_match[1] <= 80:
            return 
        movie = closest_match[0]
        files, offset, total_results = await get_search_results(movie)
        if files:
            return movie
        movie_list.remove(movie)
    return
	
async def auto_filter(client, msg, spoll=False, pm_mode=False):
    if not spoll:
        message = msg
        search = message.text
        chat_id = message.chat.id
        settings = await get_settings(chat_id, pm_mode=pm_mode)
        
        searching_msg = await msg.reply_text(f'<i>🔎 sᴇᴀʀᴄʜɪɴɢ...</i> {search}')   
        files, offset, total_results = await get_search_results(search)
        # Introduce a slight delay before deleting the searching messages
        await searching_msg.delete()            
        
        if not files:
            if settings["spell_check"]:
                ai_sts = await msg.reply_text('<code><b>ᴀɴᴀʟʏᴢɪɴɢ ᴀɴᴅ ⚡ ᴏᴘᴛɪᴍɪᴢɪɴɢ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ...</b></code>')
                    
                is_misspelled = await ai_spell_check(search)
                
                if is_misspelled:
                    await ai_sts.edit(f'<b>🐬 ᴏᴘᴛɪᴍɪᴢᴇᴅ ᴄᴏʀʀᴇᴄᴛɪᴏɴ:</b> <code>{is_misspelled}</code>\n<i> Now ʀᴇғɪɴɪɴɢ sᴇᴀʀᴄʜ wɪᴛʜ ᴛʜɪs ᴜᴘᴅᴀᴛᴇᴅ qᴜᴇʀʏ...</i>')
                    await asyncio.sleep(1)
                    msg.text = is_misspelled
                    await ai_sts.delete()
                    return await auto_filter(client, msg)
                
                await ai_sts.delete()
                return await advantage_spell_chok(msg)
            return
	
    else:
        settings = await get_settings(msg.message.chat.id , pm_mode=pm_mode)
        message = msg.message.reply_to_message  # msg will be callback query
        search, files, offset, total_results = spoll
    req = message.from_user.id if message.from_user else 0
    key = f"{message.chat.id}-{message.id}"
    batch_ids = files
    temp.FILES_ID[f"{message.chat.id}-{message.id}"] = batch_ids
    batch_link = f"batchfiles#{message.chat.id}#{message.id}#{message.from_user.id}"
    temp.CHAT[message.from_user.id] = message.chat.id
    settings = await get_settings(message.chat.id , pm_mode=pm_mode)
    del_msg = f"\n\n<b>⚠️ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀꜰᴛᴇʀ <code>{get_readable_time(DELETE_TIME)}</code> ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs</b>" if settings["auto_delete"] else ''
    links = ""
    if settings["link"]:
        btn = []
        for file_num, file in enumerate(files, start=1):
            links += f"""<b>\n\n{file_num}. <a href=https://t.me/{temp.U_NAME}?start={"pm_mode_" if pm_mode else ''}file_{ADMINS[0] if pm_mode else message.chat.id}_{file.file_id}>[{get_size(file.file_size)}] {formate_file_name(file.file_name)}</a></b>"""
    else:
        btn = [[InlineKeyboardButton(text=f"📁 {get_size(file.file_size)} ✦ {formate_file_name(file.file_name)}", url=f'https://telegram.dog/{temp.U_NAME}?start=file_{message.chat.id}_{file.file_id}'),]
               for file in files
              ]	
    if offset != "":
        if total_results >= MAX_BTN:
            btn.insert(0,[
                InlineKeyboardButton("sᴇɴᴅ ᴀʟʟ ғɪʟᴇs", callback_data=batch_link),
            ])
            btn.insert(1, [
                InlineKeyboardButton("ꜱᴇᴀꜱᴏɴ", callback_data=f"seasons#{key}#{offset}#{req}"),
                InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ ", callback_data=f"languages#{key}#{offset}#{req}")
            ])            
        else:
            btn.insert(0,[
                InlineKeyboardButton("sᴇɴᴅ ᴀʟʟ ғɪʟᴇs", callback_data=batch_link),
                InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ", callback_data=f"languages#{key}#{offset}#{req}")
            ])
            btn.append([
                InlineKeyboardButton("🥲 ɴᴏ ᴍᴏʀᴇ ᴘᴀɢᴇs 🥲", user_id=ADMINS[0])
            ])
    else:
        btn.insert(0,[
            InlineKeyboardButton("sᴇɴᴅ ᴀʟʟ ғɪʟᴇs", callback_data=batch_link),
            ])

        btn.append([
            InlineKeyboardButton("🥲 ɴᴏ ᴍᴏʀᴇ ᴘᴀɢᴇs 🥲", user_id=ADMINS[0])
        ])
                             
    if spoll:
        m = await msg.message.edit(f"<b><code>{search}</code> ɪs ꜰᴏᴜɴᴅ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ꜰᴏʀ ꜰɪʟᴇs 📫</b>")
        await asyncio.sleep(1.2)
        await m.delete()
    if offset != "":
        BUTTONS[key] = search
        req = message.from_user.id if message.from_user else 0
        btn.append(
            [InlineKeyboardButton(text=f"1/{math.ceil(int(total_results) / int(MAX_BTN))}", callback_data="pages"),
             InlineKeyboardButton(text="ɴᴇxᴛ ›", callback_data=f"next_{req}_{key}_{offset}")]
        )
        key = f"{message.chat.id}-{message.id}"
        BUTTONS[key] = search
        req = message.from_user.id if message.from_user else 0
        try:
            offset = int(offset) 
        except:
            offset = int(MAX_BTN)
        
    imdb = await get_poster(search, file=(files[0]).file_name) if settings["imdb"] else None
    TEMPLATE = settings['template']
    if imdb:
        cap = TEMPLATE.format(
            query=search,
            title=imdb['title'],
            votes=imdb['votes'],
            aka=imdb["aka"],
            seasons=imdb["seasons"],
            box_office=imdb['box_office'],
            localized_title=imdb['localized_title'],
            kind=imdb['kind'],
            imdb_id=imdb["imdb_id"],
            cast=imdb["cast"],
            runtime=imdb["runtime"],
            countries=imdb["countries"],
            certificates=imdb["certificates"],
            languages=imdb["languages"],
            director=imdb["director"],
            writer=imdb["writer"],
            producer=imdb["producer"],
            composer=imdb["composer"],
            cinematographer=imdb["cinematographer"],
            music_team=imdb["music_team"],
            distributors=imdb["distributors"],
            release_date=imdb['release_date'],
            year=imdb['year'],
            genres=imdb['genres'],
            poster=imdb['poster'],
            plot=imdb['plot'],
            rating=imdb['rating'],
            url=imdb['url'],
            **locals()
        )
    else:
        cap =  f"<b>ʜᴇʏ {message.from_user.mention}</b> ♥️\n\n<b>📁 ғᴏᴜɴᴅ ✨ ғɪʟᴇs ғᴏʀ ʏᴏᴜʀ ǫᴜᴇʀʏ : {search} 👇🏼</b>"

    ads, ads_name, _ = await mdb.get_advirtisment()
    ads_text = ""
    if ads is not None and ads_name is not None:
        ads_url = f"https://t.me/{temp.U_NAME}?start=ads"
        ads_text = f"<a href={ads_url}>{ads_name}</a>"

    js_ads = f"\n━━━━━━━━━━━━━━━━━━\n <b>{ads_text}</b> \n━━━━━━━━━━━━━━━━━━" if ads_text else ""
  #  del_msg = f"\n\n<b>⚠️ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀꜰᴛᴇʀ <code>{get_readable_time(DELETE_TIME)}</code> ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs</b>" if settings["auto_delete"] else ''
    CAP[key] = cap
    if imdb and imdb.get('poster'):
        try:
            if settings['auto_delete']:
                k = await message.reply_photo(photo=imdb.get('poster'), caption=cap[:1024] + links + del_msg, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn))
              #  await delSticker(st)
                await asyncio.sleep(DELETE_TIME)
                await k.delete()
                try:
                    await message.delete()
                except:
                    pass
            else:
                await message.reply_photo(photo=imdb.get('poster'), caption=cap[:1024] + links + js_ads, reply_markup=InlineKeyboardMarkup(btn))                    
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            if settings["auto_delete"]:
                k = await message.reply_photo(photo=poster, caption=cap[:1024] + links + js_ads, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn))
                #await delSticker(st)
                await asyncio.sleep(DELETE_TIME)
                await k.delete()
                try:
                    await message.delete()
                except:
                    pass
            else:
                await message.reply_photo(photo=poster, caption=cap[:1024] + links + js_ads, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn))
        except Exception as e:
            print(e)
            if settings["auto_delete"]:
                #await delSticker(st)
                try:
                    k = await message.reply_text(cap + links + js_ads, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
                except Exception as e:
                    print("error", e)
                await asyncio.sleep(DELETE_TIME)
                await k.delete()
                try:
                    await message.delete()
                except:
                    pass
            else:
                await message.reply_text(cap + links + js_ads, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
    else:
        k = await message.reply_text(text=cap + links + js_ads, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(btn), parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)
       # await delSticker(st)
        if settings['auto_delete']:
          #  await delSticker(st)
            await asyncio.sleep(DELETE_TIME)
            await k.delete()
            try:
                await message.delete()
            except:
                pass
    return            
async def advantage_spell_chok(message):
    mv_id = message.id
    search = message.text
    chat_id = message.chat.id
    settings = await get_settings(chat_id)
    query = re.sub(
        r"\b(pl(i|e)*?(s|z+|ease|se|ese|(e+)s(e)?)|((send|snd|giv(e)?|gib)(\sme)?)|movie(s)?|new|latest|br((o|u)h?)*|^h(e|a)?(l)*(o)*|mal(ayalam)?|t(h)?amil|file|that|find|und(o)*|kit(t(i|y)?)?o(w)?|thar(u)?(o)*w?|kittum(o)*|aya(k)*(um(o)*)?|full\smovie|any(one)|with\ssubtitle(s)?)",
        "", message.text, flags=re.IGNORECASE)
    query = query.strip() + " movie"
    try:
        movies = await get_poster(search, bulk=True)
    except:
        k = await message.reply(CUDNT_FND.I_CUDNT.format(message.from_user.mention))
        await asyncio.sleep(60)
        await k.delete()
        try:
            await message.delete()
        except:
            pass
        return
    if not movies:
        google = search.replace(" ", "+")
        button = [[
            InlineKeyboardButton("• ᴄʜᴇᴄᴋ ᴏɴ ɢᴏᴏɢʟᴇ •", url=f"https://www.google.com/search?q={google}")
        ]]
        k = await message.reply_photo(photo=random.choice(SPELL_IMG), caption=script.I_CUDNT.format(search), reply_markup=InlineKeyboardMarkup(button))
        await asyncio.sleep(120)
        await k.delete()
        try:
            await message.delete()
        except:
            pass
        return
    user = message.from_user.id if message.from_user else 0
    buttons = [[
        InlineKeyboardButton(text=movie.get('title'), callback_data=f"spol#{movie.movieID}#{user}")
    ]
        for movie in movies
    ]
    buttons.append(
        [InlineKeyboardButton(text="🚫 ᴄʟᴏsᴇ 🚫", callback_data='close_data')]
    )
    d = await message.reply_photo(photo=random.choice(SPELL_IMG), caption=script.CUDNT_FND.format(search), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=message.id)
    await asyncio.sleep(120)
    await d.delete()
    try:
        await message.delete()
    except:
        pass
