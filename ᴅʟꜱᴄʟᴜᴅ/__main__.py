from ꜰᴇᴛᴄʜ import *
AP = SNDCLUDE.APP_ID
AH = SNDCLUDE.API_HASH
AB = SNDCLUDE.BOT_TOKEN
from pyrogram import Client
from pyrogram.methods.utilities import idle
import shutil
from logging import INFO, basicConfig, getLogger
basicConfig(
format="%(levelname)s - %(message)s",
level=INFO)
LOGS = getLogger(__name__)


GLUU = dict(
    root="ʀᴜɴᴛɪᴍᴇ"
)

Client = Client(
    "ɦʏքɛʋօɨɖֆօʊʟ",
    api_id=AP,
    api_hash=AH,
    bot_token=AB,
    workers=12,
    plugins=GLUU
)
Client.start()
LOGS.info('🍁🎷一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一\nONLINE🍁🎷\n')
idle()
Client.stop()  
try:
    shutil.rmtree(K)
    shutil.rmtree(P)
    shutil.rmtree(V)
    shutil.rmtree(Y)
    shutil.rmtree(M)
except:
    pass
LOGS.info('🍁⚰️一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一\nOFFLINE ⚰️🍁\n')
