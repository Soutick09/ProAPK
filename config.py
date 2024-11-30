import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7679580674:AAEnb_jCZZD_g0_UYHpB5B28n1hbOVY47Wo")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28450765"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "36f00f11f9d5c65e69b81fd804453a93")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002481328926"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Soutick_09")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5827289728"))

#Port
PORT = os.environ.get("PORT", "8030")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ProAPK:ProAPK@cluster0.ysutu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002263899507"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002271125915"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds

#start message
START_PIC = os.environ.get("START_PIC", "https://envs.sh/pme.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/pme.jpg")

HELP_TXT = "<b>If you can't use me or don't get any files, it's mean you don't join either <a href=https://t.me/Pro_xAPK>Pro APK</a>. First Join These Channels Then retry.</b>"
ABOUT_TXT = "<b>• Creators: <a href=https://t.me/Soutick_09>Soutick</a> | <a href=https://t.me/ProAPK_Owner>ProAPK Owner</a>\n• Main Channel: <a href=https://t.me/Pro_xAPK>Pro APK</a>\n• Best Friend: <a href=tg://settings>This Person</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello!! {mention} 👋! I'm Pro APK's Links Supplier 😇.\n\n© @Pro_xAPK</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5413708222").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\nᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Bakka ! You're not my Senpai!!"

ADMINS.append(OWNER_ID)
ADMINS.append(5827289728)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
