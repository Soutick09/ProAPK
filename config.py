#(©)CodeXBotz
#By @Codeflix_Bots



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7679580674:AAGBYie8a_l3LuzgtSEo4zGZSB0Tn75WrU0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28450765"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "36f00f11f9d5c65e69b81fd804453a93")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002481328926"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5827289728"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ProAPK:ProAPK@cluster0.ysutu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002263899507"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002271125915"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1002092034053"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\n I am ProAPK's Links Supplier 😇.\n\n Join » @Pro_xAPK\n\n Visit Website » ProAPK.net</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "7272399911 5413708222").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Sorry {first} But You Have to Join My Channels First...\n\n So Pwase Join by clicking on “Now Click Here” button....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @Soutick_09"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "codeflixbots.txt"

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
