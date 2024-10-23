import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#---------------------------------------------------------------
#---------------------------------------------------------------         ,
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
#---------------------------------------------------------------
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5672857559').split()]
USERNAME = environ.get('USERNAME', "https://t.me/IM_JISSHU") # ADMIN USERNAME
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/JisshuMovieZone')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
#---------------------------------------------------------------
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
#---------------------------------------------------------------
#---------------------------------------------------------------
#----------- There will be channel id add in all these ---------
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '0'))  # set shortner log channel
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','0')) # The movie you upload in it will be deleted from the bot.
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '0'))
auth_channel = environ.get('AUTH_CHANNEL', '')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '0'))
request_channel = environ.get('REQUEST_CHANNEL', '0') # If anyone sends a request message to your bot, you will get it in this channel.
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '0')) # 
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/') #Support group link ( make sure bot is admin )
#---------------------------------------------------------------
#---------------------------------------------------------------
IS_VERIFY = is_enabled('IS_VERIFY', True)
#---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'omegalinks.in')
SHORTENER_API2 = environ.get("SHORTENER_API2", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'omegalinks.in')
SHORTENER_API3 = environ.get("SHORTENER_API3", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'omegalinks.in')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))
#---------------------------------------------------------------
#---------------------------------------------------------------
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
#---------------------------------------------------------------
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
#---------------------------------------------------------------
#---------------------------------------------------------------
PREMIUM_PIC = (environ.get('PREMIUM_PIC', 'https://envs.sh/pVp.jpg https://envs.sh/pVT.jpg https://envs.sh/pVn.jpg https://envs.sh/pVI.jpg https://envs.sh/pVB.jpg https://envs.sh/pVW.jpg https://envs.sh/pVS.jpg')).split()
EARNMONEY_PIC = (environ.get('EARNMONEY_PIC', 'https://graph.org/file/5197a7eef9ff83262e6ad.jpg https://graph.org/file/831f3a58f1eb8362827d5.jpg https://graph.org/file/bf8f0d9edf14829e2eb06.jpg https://graph.org/file/7914023396c3e6d6b0ab4.jpg https://graph.org/file/518531963faadd2c0c20f.jpg https://graph.org/file/9e433f29684134f0dceb3.jpg https://graph.org/file/aed0ccf00ff8acc1afee4.jpg')).split()
SPELL_IMG = (environ.get('SPELL_IMG', 'https://graph.org/file/ee0b06fbf1e0f79122532.jpg https://graph.org/file/4cd26f2e3599ddf7b346b.jpg https://graph.org/file/a31e2169da3210e7f4ce6.jpg https://graph.org/file/9b4f26839abb96432bfb1.jpg https://graph.org/file/9436f9cbbad83ba552f2e.jpg https://graph.org/file/e99a245a20f1892fbc92a.jpg https://graph.org/file/458ff80ce537b50fad45e.jpg')).split()
YT_PIC = (environ.get('YT_PIC', 'https://graph.org/file/ccdcebbdb2d9e99f57aa1.jpg https://graph.org/file/7aae08fd87fa189d94481.jpg')).split()
HELP_PIC = (environ.get('HELP_PIC', 'https://graph.org/file/6762b66b7d0ebbd06ae27.jpg https://graph.org/file/4d822099a264d8783cc64.jpg https://graph.org/file/605193b8f4b91bd1d93d9.jpg https://graph.org/file/6bd8b1f681840d219f9f1.jpg https://graph.org/file/f1eb31c75ef43f3e983eb.jpg https://graph.org/file/d98f7f46960479ee35274.jpg https://graph.org/file/99dceaaab24ad5e92bba5.jpg https://graph.org/file/c7302333cebe82d29d08e.jpg')).split()
RULES_PIC = (environ.get('RULES_PIC', 'https://graph.org/file/b94aa904ec73efa7bb938.jpg https://graph.org/file/d6b06e2bb155935adcc5e.jpg https://graph.org/file/f3ee69d5e36ebd6b120b6.jpg')).split()
VERIFY_PIC = (environ.get('VERIFY_PIC', 'https://graph.org/file/523dd9d97677254eeb5a5.jpg https://graph.org/file/50409d1edf26caaea6278.jpg https://graph.org/file/f981682eefbe8c5e0c6ad.jpg https://graph.org/file/e63425ee7104d5b741a08.jpg https://graph.org/file/4d4f1fe45849773751f9a.jpg https://graph.org/file/433bacbbf507a8ddf0486.jpg https://graph.org/file/46a3259fc0f76b91178d0.jpg')).split()
PICS2 = (environ.get('PICS2', 'https://graph.org/file/bed440a9bdcf1d9b62a5d.jpg https://graph.org/file/74879d6ab32e4b067d7aa.jpg https://graph.org/file/c387e7a27af66fde7a86d.jpg https://graph.org/file/0b975358e5f72b16c252c.jpg https://graph.org/file/512c6004240a35d7a42ce.jpg https://graph.org/file/809a007a45d06f09621d5.jpg')).split()
START_IMG = (environ.get('START_IMG', 'https://telegra.ph/file/6a0726f79acd8300e9a04.jpg https://telegra.ph/file/68289fefb76dbc43b766d.jpg https://telegra.ph/file/0caad29c0cf91c23fb1b6.jpg https://telegra.ph/file/8c34c755dd16581c1c6b5.jpg https://telegra.ph/file/365e35b554e5a3ea83857.jpg https://telegra.ph/file/07f185825c5b7bfd6fbfb.jpg https://telegra.ph/file/85f95494565a762edb3e7.jpg https://telegra.ph/file/708a1d6ce805fcc6a46d0.jpg https://telegra.ph/file/d799c1a964f211028cc97.jpg https://telegra.ph/file/b987425b80bca0cf45c7e.jpg https://telegra.ph/file/2a8b3779760289b76de24.jpg https://telegra.ph/file/47961be968719b3e24cf0.jpg https://telegra.ph/file/2e127b0f6b1810d733c09.jpg https://telegra.ph/file/281b18770a43a29120252.jpg https://telegra.ph/file/2086dd2aa8382e758a599.jpg https://telegra.ph/file/fcc849db4bf5c517f0f8d.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/46443096bc6895c74a716.jpg")
MELCOW_PIC = (environ.get('MELCOW_PIC', 'https://graph.org/file/0c527b681ee3d024d81e9.jpg https://graph.org/file/ad13ab5a18320ed6a33d1.jpg https://graph.org/file/6e86ac350fc34f61f10c9.jpg https://graph.org/file/0e7b82cd5503139495d17.jpg https://graph.org/file/7c7b2654c1f41b7107861.jpg https://graph.org/file/e6cd46ee1e6c2db5ff4e5.jpg https://graph.org/file/dc2c11a33ca85a1f322ee.jpg https://graph.org/file/019251312dd6f424cef7b.jpg')).split()
ADDGRP_PIC = environ.get("ADDGRP_PIC", "https://graph.org/file/0b975358e5f72b16c252c.jpg")
#---------------------------------------------------------------
PICS = (environ.get('PICS', 'https://envs.sh/pfy.jpg https://envs.sh/pf6.jpg https://envs.sh/pfV.jpg https://envs.sh/pfx.jpg https://envs.sh/pf-.jpg https://envs.sh/paD.jpg https://envs.sh/paE.jpg https://envs.sh/paQ.jpg https://envs.sh/pah.jpg https://envs.sh/pad.jpg https://envs.sh/pa2.jpg https://envs.sh/pau.jpg https://envs.sh/pat.jpg https://envs.sh/pae.jpg https://envs.sh/pai.jpg')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://envs.sh/p-t.jpg')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/9f3f47c690bbcc67633c2.jpg'))
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
#---------------------------------------------------------------
#---------------------------------------------------------------
#------------.---------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
IS_SEND_MOVIE_UPDATE = is_enabled('IS_SEND_MOVIE_UPDATE', False) # Don't Change It ( If You Want To Turn It On Then Turn It On By Commands) We Suggest You To Make It Turn Off If You Are Indexing Files First Time.
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTIgON}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_ThXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "")

#---------------------------------------------------------------
#---------------------------------------------------------------
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'tutorial_2': TUTORIAL_2,
            'tutorial_3': TUTORIAL_3,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}
