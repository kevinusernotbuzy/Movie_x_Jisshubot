import os
class script(object):
    START_TXT =  """<b>{} ✨, {}

✦ ɪ ᴀᴍ ⚡️ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ-ғɪʟᴛᴇʀ ʙᴏᴛ.
✦ ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴀʟʟ ᴍᴏᴠɪᴇs ᴀɴᴅ ᴡᴇʙ sᴇʀɪᴇs ɪɴ sᴏᴍᴇ ʟᴀɴɢᴜᴀɢᴇs. 
✦ ɪᴛs ᴇᴀsʏ ᴛᴏ ᴜsᴇ ᴍᴇ. ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ.

✦ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ᴄʜᴇᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ʙᴀʙʏ 💜</b>"""

    HELP_TXT = """<b>Hᴇʏ {}\n
★ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.</b>"""
    
    
    FORCESUB_TEXT = """
⚠️ <b><u>ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ</u> ⚠️

✘ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴏᴜʀ ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ sᴏ ʏᴏᴜ ᴅᴏɴ'ᴛ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ғɪʟᴇ.

✘ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ғɪʟᴇ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴊᴏɪɴ ʙᴜᴜᴛᴏɴ ᴀɴᴅ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ,\nᴛʜᴇɴ ᴄʟɪᴄᴋ 🔄 ᴛʀʏ ᴀɢᴀɪɴ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ!</b>
"""
    
    EXTRA_CMDS_TEXT = """<b>
    <u>ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs</u>
• /ban - ʙᴀɴ ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.
• /unban - uɴʙᴀɴ ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.

<u>ᴏᴛʜᴇʀ ᴜsᴇғᴜʟ ᴄᴏᴍᴍᴀɴᴅs</u>
• /telegraph - sᴇɴᴅ ᴍᴇ ᴀ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ (ᴜᴘ ᴛᴏ 5ᴍʙ).
• /stream - sᴇɴᴅ ᴍᴏᴠɪᴇ ᴏʀ sᴇʀɪᴇs ғɪʟᴇs ғᴏʀ ᴏɴʟɪɴᴇ sᴛʀᴇᴀᴍɪɴɢ ᴏʀ ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ.
• /font - cʜᴀɴɢᴇ ᴛᴇxᴛ ᴛᴏ sᴛʏʟɪsʜ ғᴏʀᴍᴀᴛs.
• /link - sʜᴀʀᴇ ᴀɴʏ ᴛᴇxᴛ wɪᴛʜ ᴀ ᴄʟɪᴄkᴀʙʟᴇ ʟɪɴᴋ.
• /id - ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ.
</b>"""
    
    DISCLAIMER_TXT = """<pre>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.\n
ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ᴏʀ ʙʏ ᴀɴʏ ᴍᴇᴀɴꜱ, ꜱʜᴀʀᴇ, ᴏʀ ᴄᴏɴꜱᴜᴍᴇ, ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.\n</pre>
<b>~ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ ›› <a href=https://t.me/vampirexgirl><b></b>ѵαмριяɛ ɢιяℓ</a></b>"""

    ABOUT_TXT = """<b><i>🤖 ᴍʏ ɴᴀᴍᴇ : {}
👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : ᴍᴀʀᴄᴜs
📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏʀᴏɢʀᴀᴍ
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3
📡 ʜᴏsᴛᴇᴅ ᴏɴ : ᴠᴘs
🌟 ᴠᴇʀsɪᴏɴ : ᴠ 13.0 [ ʙᴇᴛᴀ ]\n
~ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href=https://t.me/Vampirexgirl></b>ѵαмριяɛ ɢιяℓ</a></b>"""
    
    
    SUPPORT_GRP_MOVIE_TEXT = '''<b>ʜᴇʏ {}

ɪ ғᴏᴜɴᴅ {} ʀᴇsᴜʟᴛs 🎁,
ʙᴜᴛ ɪ ᴄᴀɴ'ᴛ sᴇɴᴅ ʜᴇʀᴇ 🤞🏻
ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ᴛᴏ ɢᴇᴛ ✨</b>'''

    CHANNELS = """
<u>ᴏᴜʀ ᴀʟʟ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ᴄʜᴀɴɴᴇʟꜱ</u> 

▫ ᴀʟʟ ʟᴀᴛᴇꜱᴛ ᴀɴᴅ ᴏʟᴅ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ.
▫ ᴀʟʟ ʟᴀɴɢᴜᴀɢᴇꜱ ᴍᴏᴠɪᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ.
▫ ᴀʟᴡᴀʏꜱ ᴀᴅᴍɪɴ ꜱᴜᴘᴘᴏʀᴛ.
▫ 𝟸𝟺x𝟽 ꜱᴇʀᴠɪᴄᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ."""

    LOGO = """

BOT Started 💋🐬"""
    
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v4.2 [ Sᴛᴀʙʟᴇ ]</code>

Bʏ @Noob_X_Marcus</b>"""
        
    
    STATUS_TXT = """<b><u>🗃 ᴅᴀᴛᴀʙᴀsᴇ 1 🗃</u>

» ᴛᴏᴛᴀʟ ᴜsᴇʀs - <code>{}</code>
» ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🗳 ᴅᴀᴛᴀʙᴀsᴇ 2 🗳</u></b>

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖</u>

» ᴜᴘᴛɪᴍᴇ - <code>{}</code>
» ʀᴀᴍ - <code>{}%</code>
» ᴄᴘᴜ - <code>{}%</code></b>"""

    NEW_USER_TXT = """<b>#New_User {}

≈ ɪᴅ:- <code>{}</code>
≈ ɴᴀᴍᴇ:- {}</b>"""

    NEW_GROUP_TXT = """#New_Group {}

Group name - {}
Id - <code>{}</code>
Group username - @{}
Group link - {}
Total members - <code>{}</code>
User - {}"""

    REQUEST_TXT = """<b>📜 ᴜꜱᴇʀ - {}
📇 ɪᴅ - <code>{}</code>

🎁 ʀᴇǫᴜᴇꜱᴛ ᴍꜱɢ - <code>{}</code></b>"""  

    IMDB_TEMPLATE_TXT = """
📟 ᴛɪᴛʟᴇ : <a href={url}><b>{title}</b></a>
🛸 ɪɴғᴏ : <b>{runtime} min</b> | <a href={url}/releaseinfo><b>{year}</b></a>
🎭 ɢᴇɴʀᴇ : <b>{genres}</b>
🌟 ʀᴀᴛɪɴɢ : <b><a href={url}/ratings>{rating}</a> / 10</b>
🔊 ʟᴀɴɢᴜᴀɢᴇ : <b>#{languages}</b>
👩🏻‍💻 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : <b>{message.from_user.mention}</b>
"""
    
    FILE_CAPTION = """<b><i>{file_name} » {file_size} › [Top10ner movie](https://t.me/top10ner_0)</i></b>"""

    RULES_TEXT = """<b>♨️ 𝗚𝗥𝗢𝗨𝗣 𝗥𝗨𝗟𝗘𝗦 ♨️\n\n🔹 Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ :\n› ᴀᴠᴀᴛᴀʀ 2009 ✅\n› ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ✅\n› ᴀᴠᴀᴛᴀʀ ᴍᴏᴠɪᴇ ❌\n› ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ..❌\n\n🔹Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇs Iɴ ᴛʜɪs Fᴏʀᴍᴀᴛᴇ : \n› ᴠɪᴋɪɴɢs S01 ✅\n› ᴠɪᴋɪɴɢs S01E01 ✅\n› ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ✅\n› ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ᴅᴜʙʙ. ❌\n› ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 1 ❌\n› ᴠɪᴋɪɴɢs ᴡᴇʙ sᴇʀɪᴇs ❌\n\n🔹 ᴅᴏɴ'ᴛ ᴅᴏ ᴀɴʏ sᴇʟғ ᴘʀᴏᴍᴏᴛɪᴏɴ.\n\n🔹 ᴅᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ ᴅᴏᴄᴜᴍᴇɴᴛs, ᴜʀʟ ᴇᴛᴄ..\n\n🔹 ᴅᴏɴ'ᴛ ʀᴇǫᴜᴇsᴛ ᴀɴʏ ᴛʜɪɴɢs ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇ sᴇʀɪᴇs ᴀɴɪᴍᴇs..\n\n⚙️ 𝖭ᴏᴛᴇ :- 𝖠ʟʟ ᴍᴇ𝗌𝗌ᴀɢᴇ𝗌 ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀғᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇ𝗌 ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪ𝗌𝗌ᴜᴇ𝗌.</b>"""
    
    EARN_TEXT = """
<b>──────「 <a href='t.me/Vampirexgirl'>ᴇᴀʀɴ ᴍᴏɴᴇʏ</a> 」─────

<b>Now You can start earning 💸 money today with our Simple and easy-to-use bot!\n\n›› Step 1: Add This bot to your group as an admin..\n\n›› Step 2: If you don't Using any shortner website then make account first on <a href='https://mdiskshortner.link/ref/Kimxd'>mdiskshortner.link</a> (You can also use other link shortner website).\n\n›› Step 3: Copy your API from website and then, simply set your website and API Using the\n/set_shortner command\n\n› Like this :  <pre>/set_shortner shorturllink.in 7eddb02ee3a9e5ad7c207aab9cce5b34fadfe22f</pre>\n\n\n★ This bot will automatically converts links with Your Api and will provide your links.\n\n★ Don't wait any longer to start earning money from your telegram group. Add our bot today and start making money 💰!</b>\n"""


    EARN_CMD_TEXT = """
<b>Earn money related my all command</b>

/set_shortner - Set your own api with shortner website.
/set_tutorial - Set your tutorial video link.
/del_tutorial - Delete your tutorial video link"""

    START2 = """<b>ʜᴇʏ 💜 {}

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs.\nᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ ʙᴀʙʏ 💞</b>"""
    
    YT_TEXT = """
<b>• ɴᴀᴍᴇ ›› ᴛᴏᴘ10ɴᴇʀ</b>
<b>• ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ ›› <a href='https://youtube.com/@Top10ner'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>

<pre>ᴘʟᴇᴀsᴇ ʟɪᴋᴇ - sʜᴀʀᴇ - sᴜʙsᴄʀɪʙᴇ</pre>"""

    ALRT_TXT = """Hᴇʏ 🙄, Iᴛ's Nᴏᴛ Fᴏʀ Yᴏᴜ ❗"""

    OLD_ALRT_TXT = """ʏᴏᴜ ᴀʀᴇ ᴜsɪɴɢ ᴍʏ ᴏʟᴅ ᴍᴇssᴀɢᴇs..sᴇɴᴅ ᴀ ɴᴇᴡ ʀᴇǫᴜᴇsᴛ.."""

    NO_RESULT_TXT = """<b>ᴛʜɪs ᴍᴇssᴀɢᴇ ɪs ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ ᴏʀ ᴀᴅᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ 🙄</b>"""
    
    I_CUDNT = """<b>ʏᴏᴜʀ ᴡᴏʀᴅ 👉🏻 <s>{}</s> 👈🏻 ɪs ɴᴏᴛ ᴍᴀᴄᴛʜ ᴀɴʏ ᴍᴏᴠɪᴇs ᴏʀ ᴡᴇʙsᴇʀɪᴇs 🤯.

✦ ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ 🤧

➻ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʜɪᴛ  /rules</b>
"""

    I_CUD_NT = """<b>ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
\nᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ...</b>"""
    
    CUDNT_FND = """<b>ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ <u>{}</u>
\n<pre>ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ 👇🏻?</pre>"""


    FONT_TXT= """<b>ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛs sᴛʏʟᴇ, ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ʟɪᴋᴇ ᴛʜɪs ꜰᴏʀᴍᴀᴛ

<code>/font hi how are you</code></b>"""
    
    PLAN_TEXT = """<b>ᴡᴇ ᴀʀᴇ ᴘʀᴏᴠɪᴅɪɴɢ ᴘʀᴇᴍɪᴜᴍ ᴀᴛ ᴛʜᴇ ʟᴏᴡᴇsᴛ ᴘʀɪᴄᴇs:
    
25 ʀᴜᴘᴇᴇ ғᴏʀ ᴏɴᴇ ᴍᴏɴᴛʜs
45 ʀᴜᴘᴇᴇs ғᴏʀ ᴛᴡᴏ  ᴍᴏɴᴛʜs
99 ʀᴜᴘᴇᴇs ғᴏʀ sɪx ᴍᴏɴᴛʜs

ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ʙᴜʏɪɴɢ ↡↡↡
</b>"""
    
    VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {} {},

📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ ᴛᴏᴅᴀʏ, ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ғᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 1/3 ✓

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ʙᴏᴛ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😊

💶 sᴇɴᴅ /plan ᴛᴏ ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ</b>"""

    VERIFY_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 1st ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ <code>{}</code></b>"""

    SECOND_VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {} {},

📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 2/3

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ʙᴏᴛ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😊

💶 sᴇɴᴅ /plan ᴛᴏ ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ</b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 2nd ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ <code>{}</code></b>"""

    THIRDT_VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {},
    
📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 3/3

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b>👋 ʜᴇʏ {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 3rd ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ </b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ ᴜsᴇʀ ᴠᴇʀɪꜰɪᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ ☄</u>

⚡️ ɴᴀᴍᴇ:- {} [ <code>{}</code> ] 
📆 ᴅᴀᴛᴇ:- <code>{} </code></b>

#verified_{}_completed"""

    SETTINGS_TXT = """<u>\nѕeттιngѕ</u>
~ sᴇᴛᴛɪɴɢs ɪs ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇs ɪɴ ᴛʜɪs ʙᴏᴛ.\n~ ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<u>noтe</u>
1. ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʜᴀɴɢᴇs sᴇᴛᴛɪɴɢs.
2. ɪᴛ ᴡᴏʀᴋs ᴏɴʟʏ ᴡʜᴇɴ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<u>coммand and υѕeѕ</u>
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ"""
    
    MOVIES_UPDATE_TXT = """<b>#𝑵𝒆𝒘_𝑭𝒊𝒍𝒆_𝑨𝒅𝒅𝒆𝒅 ✅
**🍿 Title:** {title}
**🎃 Genres:** {genres}
**📆 Year:** {year}
**⭐ Rating:** {rating} / 10
</b>"""

    PREPLANS_TXT = """<b>ʜᴇʏ {},
    
🎁 <u>ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs</u> :

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs                                                                        
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan
</b>"""


    PREPLANSS_TXT = """<b>ʜᴇʏ {},
    
🎁 <u>ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs</u> :

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs                                                                        
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan
</b>"""


    
    FREE_TXT = """<b>ʜᴇʏ {}
    
<b><u>ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴs</u>
1. 25₹ = 1ᴍᴏɴᴛʜ
2. 45₹ = 2ᴍᴏɴᴛʜ
3. 59₹ = 3ᴍᴏɴᴛʜ
4. 99₹ = 6ᴍᴏɴᴛʜ

• <u>ᴜᴘɪ ɪᴅ</u> - <code>userx750@ibl</code>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ</b>"""


    REFFER_TXT = """
<b>ʀᴇғᴇʀʀᴇ ʏᴏᴜʀ ғʀɪᴇɴᴅs ᴀɴᴅ ғᴀᴍɪʟʏ, ᴀɴᴅ ᴄᴏʟʟᴇᴄᴛ 100 ᴘᴏɪɴᴛ.

Note: = ᴘᴇʀ ʀᴇғғᴇʀ 10 ᴘᴏɪɴᴛ

ʏᴏᴜʀ ʀᴇғᴇʀᴀʟ ʟɪɴᴋ - https://telegram.me/{}?start=reff_{}

ɪғ ʏᴏᴜ ᴄᴏʟʟᴇᴄᴛ 50 ᴘᴏɪɴᴛs, ʏᴏᴜ ᴡɪʟʟ ʙᴇ ɢɪᴠᴇɴ 1 ᴍᴏɴᴛʜ ᴘʀᴇᴍɪᴜᴍ.
============================
 <u>💫ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs💫</u> :
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs                                                                        
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]        
____________________________
ʙᴜʏ ᴘᴀɪᴅ ᴘʟᴀɴ ʙʏ - /plan</b>"""
    
    ADMIN_CMD_TXT = """<b><blockquote>
-------------User Premium------------
➩ /add_premium {user ID} {Times} - Add a premium user
➩ /remove_premium {user ID} - Remove a premium user
➩ /add_redeem - Generate a redeem code
➩ /premium_users - List all premium users
➩ /refresh - Refresh free trial for users
-------------Update Channel----------
➩ /set_muc {channel ID} - Set the movies update channel
--------------PM Search--------------
➩ /pm_search_on - Enable PM search
➩ /pm_search_off - Disable PM search
--------------Verify ID--------------
➩ /verify_id - Generate a verification ID for group use only
--------------Set Ads----------------
➩ /set_ads {ads name}}#{Times}#{photo URL} - <a href="https://t.me/Jisshu_developer/11">Explain</a>
➩ /del_ads - Delete ads
-------------Top Trending------------
➩ /setlist {Mirzapur, Money Heist} - <a href=https://t.me/Jisshu_developer/10>Explain</a>
➩ /clearlist - Clear all lists
</blockquote></b>"""

    ADMIN_CMD_TXT2 = """<b><blockquote>
--------------Index File--------------
➩ /index - Index all files
--------------Leave Link--------------
➩ /leave {group ID} - Leave the specified group
-------------Send Message-------------
➩ /send {user-name} - Use this command as a reply to any message
----------------Ban User---------------
➩ /ban {user-name} - Ban user 
➩ /unban {user-name} - Unban user
--------------Broadcast--------------
➩ /broadcast - Broadcast a message to all users
➩ /grp_broadcast - Broadcast a message to all connected groups

</blockquote></b>"""
    
    
    FSUB_TXT = """
<u>noтe</u>
1. ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ.
2. ᴀꜱꜱɪɢɴ ᴍᴇ ᴀꜱ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ.

<u>coммand and υѕeѕ</u>
<b>• /fsub your_target_chat_id</b>
ᴇxᴀᴍᴘʟᴇ: <code>/fsub -100xxxxxx</code>

• /del_fsub - ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴛʜᴇ ꜰꜱᴜʙ ꜰᴇᴀᴛᴜʀᴇ.
• /show_fsub - ᴛᴏ ᴄʜᴇᴄᴋ ɪꜰ ꜰꜱᴜʙ ɪꜱ ᴀᴄᴛɪᴠᴇ.

<b>ᴛʜᴀᴛ'ꜱ ɪᴛ! ɪ ᴡɪʟʟ ᴇɴᴄᴏᴜʀᴀɢᴇ ʏᴏᴜʀ ᴜꜱᴇʀꜱ ᴛᴏ ᴊᴏɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ. 
ғɪʟᴇꜱ ᴡɪʟʟ ᴏɴʟʏ ʙᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴏɴᴄᴇ ᴜꜱᴇʀꜱ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟ.</b>
"""

# Command explanations for Set Verify
    SET_VERIFY_TEXT = """<b><u>Sᥱt Shortnᥱr Wᥱbsιtᥱ API</u></b>

• /Set_Shortner - ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ꜱᴇᴛꜱ ᴜᴘ ᴜꜱᴇʀ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴛʜʀᴏᴜɢʜ ᴀ ᴡᴇʙꜱɪᴛᴇ ʟɪɴᴋ ᴀɴᴅ ɪᴛꜱ ᴀᴘɪ.
<b>ᴇxᴀᴍᴘʟᴇ:</b> <code>/set_shortner publicearn.com 73864ab32816f09a175150af803b888652d28dbd</code>

• /Set_Shortner2 - ᴜꜱᴇ ᴛʜɪꜱ ꜰᴏʀ ᴀɴ ꜱᴇᴄᴏɴᴅ sʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ.
<b>ᴇxᴀᴍᴘʟᴇ:</b> <code>/set_shortner2 publicearn.com 73864ab32816f09a175150af803b888652d28dbd</code>

• /Set_Shortner3 - ᴜꜱᴇ ᴛʜɪꜱ ꜰᴏʀ ᴀ ᴛʜɪʀᴅ sʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ ᴏᴘᴛɪᴏɴ.
<b>ᴇxᴀᴍᴘʟᴇ:</b> <code>/set_shortner3 publicearn.com 73864ab32816f09a175150af803b888652d28dbd</code>


<b><u>Sᥱt Vᥱrιfιᥴᥲtιon Tιmᥱ Gᥲρ</u></b>

<u>noтe</u>
1. ɪғ ʏᴏᴜ ᴡᴀɴᴛ 1 ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ɪɴ ᴀ ᴅᴀʏ ᴛʜᴇɴ /set_time2 - 40000 ᴏʀ ᴀʙᴏᴠᴇ ɪɴ sᴇᴄᴏɴᴅ
2. ɪғ ʏᴏᴜ ᴡᴀɴᴛ 2 ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ɪɴ ᴀ ᴅᴀʏ ᴛʜᴇɴ /set_time3 - 20000 ᴏʀ ᴀʙᴏᴠᴇ ɪɴ sᴇᴄᴏɴᴅ 
3. ɪғ ʏᴏᴜ ᴡᴀɴᴛ 1 ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ɪɴ ᴀ ᴅᴀʏ ᴛʜᴇɴ ʙᴏᴛʜ ᴏғ ᴇǫᴜᴀʟ /set_time3 & /set_time2 - 14000

<u>coммand and υѕeѕ</u>
• /set_time2 - {seconds} sᴇᴛꜱ ᴛʜᴇ ᴅᴇʟᴀʏ ꜰᴏʀ ᴛʜᴇ ꜱᴇᴄᴏɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴘʀᴏᴄᴇꜱꜱ ɪɴ ꜱᴇᴄᴏɴᴅꜱ.
<b>ᴇxᴀᴍᴘʟᴇ:</b> <code>/set_time2 20000</code>

• /set_time3 - {seconds} sᴇᴛꜱ ᴛʜᴇ ᴅᴇʟᴀʏ ꜰᴏʀ ᴛʜᴇ ᴛʜɪʀᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴘʀᴏᴄᴇꜱꜱ.
<b>ᴇxᴀᴍᴘʟᴇ:</b> <code>/set_time3 16000</code>"""


    VERIFY_ON_OFF_TEXT = """<b><u>Verify On/Off</u></b>

• /verifyoff - {verify.off code}</b> Turns off the verification process. Contact the admin for this code.</i> (<a href="https://t.me/vampirexgirl">Contact Admin</a>

• /verifyon - Reactivates the verification process."""

# Command explanations for setting file captions
    SET_CAPTION_TEXT = """<b><u>Sᥱt Cᥙstom Fιᥣᥱ Cᥲρtιon</u></b>

• /set_caption - ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜᴇ ᴄᴀᴘᴛɪᴏɴ ғᴏʀ ғɪʟᴇs sᴇɴᴛ ʙʏ ᴛʜᴇ ʙᴏᴛ.

<b>ᴇxᴀᴍᴘʟᴇ:</b> <code>/set_caption <b><i>{file_name} » {file_size} › [Top10ner movie](https://t.me/top10ner_0)</i></b></code>"""

# Command explanations for setting IMDb templates
    SET_TEMPLATE_TEXT = """<b><u>Sᥱt IMDb Tᥱmρᥣᥲtᥱ</u></b>

• /set_template - sᴇᴛs ᴀ ᴄᴏᴜsᴛᴏᴍ ᴛᴇᴍᴘʟᴀᴛᴇ ғᴏʀ ɪᴍᴅʙ ɪɴғᴏ.

ᴇxᴀᴍᴘʟᴇ ᴛᴇᴍᴘʟᴀᴛᴇ: <a href="https://telegra.ph/Set-IMDb-Template-Caption-10-22">ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>"""

# Command explanations for setting tutorials
    SET_TUTORIAL_TEXT = """<b><u>Sᥱt Vᥱrιfιᥴᥲtιon Tᥙtorιᥲᥣ</u></b>

• /set_tutorial - sᴇᴛ ʏᴏᴜʀ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs.
• /set_tutorial2 - sᴇᴛ ʏᴏᴜʀ 2nd ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ.
• /set_tutorial3 - sᴇᴛ ʏᴏᴜʀ 3rd ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ.

<b>ᴇxᴀᴍᴘʟᴇ:</b> <code>/set_tutorial https://t.me/how_to_download_movi/5</code>"""

# Command explanations for setting a log channel
    SET_LOG_CHANNEL_TEXT = """<b><u>Log Chᥲnnᥱᥣ Sᥱtᥙρ</u></b>

• /set_log - {log channel id} sᴇᴛ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴜsᴇʀs ᴀᴄᴛɪᴠɪᴛɪᴇs. ᴇɴsᴜʀᴇ ᴛʜᴇ ʙᴏᴛ ɪs ᴀɴ ᴀᴅᴍɪɴ.

<b>ᴇxᴀᴍᴘʟᴇ:</b> <code>/set_log -1878998680</code>"""
    

# General info and additional details command
    GENERAL_INFO_TEXT = """<b><u>ᴄᴏᴜᴛɪᴍɪᴢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ</u></b>

<i>ᴄʜᴇᴄᴋ ᴀʟʟ ʏᴏᴜʀ ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs ᴅᴇᴛᴀɪʟs ᴜsɪɴɢ ᴛʜᴇ /details ᴄᴏᴍᴍᴀɴᴅ.</i>

<b>ᴀᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀɴᴅ ᴀᴅᴍɪɴ ᴛᴏ ᴀᴄᴄᴇss ᴀʟʟ ғᴇᴀᴛᴜʀᴇs.</b>"""

    GROUP_C_TEXT = """
<u>Sᥱt Shortnᥱr Wᥱbsιtᥱ API</u>:
  • /set_Shortner - {website link} {website API}
  • /set_Shortner2 - {website link} {website API}
  • /set_Shortner3 - {website link} {website API}

<u>Sᥱt Vᥱrιfιᥴᥲtιon Tᥙtorιᥲᥣ</u>:
  • /set_tutorial – sᴇᴛ ʏᴏᴜʀ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ ғᴏʀ sʜᴏʀᴛɴᴇʀ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.

<u>Sᥱt Vᥱrιfιᥴᥲtιon Tιmᥱ Gᥲρ</u>:
  • /set_time2 {seconds} – sᴇᴛ ᴛɪᴍᴇ ғᴏʀ ᴛʜᴇ sᴇᴄᴏɴᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.
  • /set_time3 {seconds} – sᴇᴛ ᴛɪᴍᴇ ғᴏʀ ᴛʜᴇ ᴛʜɪʀᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.

<u>Sᥱt Cᥙstom Fιᥣᥱ Cᥲρtιon</u>:
  • /set_caption – sᴇᴛ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ғᴏʀ ғɪʟᴇs.

<u>Sᥱt IMDb Tᥱmρᥣᥲtᥱ</ᥙ></u>:
  • /set_template – sᴇᴛ ᴛʜᴇ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ.

<u>Log Chᥲnnᥱᥣ Sᥱtᥙρ</u>:
  • /set_log – {log channel ID} ᴀᴅᴅ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.(ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ʜᴀs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ)

<u>Chᥱᥴk Groᥙρ Dᥱtᥲιᥣs</u>:
  • /details – ᴠɪᴇᴡ ᴀʟʟ ʏᴏᴜʀ ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs ᴅᴇᴛᴀɪʟs.

<i>◍ ᴀᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀᴅᴍɪɴ ᴛᴏ ᴇɴʙʟᴇᴀʟʟ ᴛʜᴇsᴇ ғᴇᴀᴛᴜʀᴇs.</i>
"""
    
    GROUP_TEXT = """
<u>Sᥱt Shortnᥱr Wᥱbsιtᥱ API</u>:
  • /set_Shortner - {website link} {website API}
  • /set_Shortner2 - {website link} {website API}
  • /set_Shortner3 - {website link} {website API}

<u>Sᥱt Vᥱrιfιᥴᥲtιon Tᥙtorιᥲᥣ</u>:
  • /set_tutorial – sᴇᴛ ʏᴏᴜʀ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ ғᴏʀ sʜᴏʀᴛɴᴇʀ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.

<u>Sᥱt Vᥱrιfιᥴᥲtιon Tιmᥱ Gᥲρ</u>:
  • /set_time2 {seconds} – sᴇᴛ ᴛɪᴍᴇ ғᴏʀ ᴛʜᴇ sᴇᴄᴏɴᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.
  • /set_time3 {seconds} – sᴇᴛ ᴛɪᴍᴇ ғᴏʀ ᴛʜᴇ ᴛʜɪʀᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.

<u>Sᥱt Cᥙstom Fιᥣᥱ Cᥲρtιon</u>:
  • /set_caption – sᴇᴛ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ғᴏʀ ғɪʟᴇs.

<u>Sᥱt IMDb Tᥱmρᥣᥲtᥱ</ᥙ></u>:
  • /set_template – sᴇᴛ ᴛʜᴇ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ.

<u>Log Chᥲnnᥱᥣ Sᥱtᥙρ</u>:
  • /set_log – {log channel ID} ᴀᴅᴅ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.(ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ʜᴀs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ)

<u>Chᥱᥴk Groᥙρ Dᥱtᥲιᥣs</u>:
  • /details – ᴠɪᴇᴡ ᴀʟʟ ʏᴏᴜʀ ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs ᴅᴇᴛᴀɪʟs.

<i>◍ ᴀᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀᴅᴍɪɴ ᴛᴏ ᴇɴʙʟᴇᴀʟʟ ᴛʜᴇsᴇ ғᴇᴀᴛᴜʀᴇs.</i>
"""
