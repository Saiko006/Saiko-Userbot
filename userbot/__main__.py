""" Userbot start point """

import sys
from importlib import import_module

import requests

from userbot import (
    BOT_TOKEN,
    BOT_USERNAME,
    BOT_VER,
    BOTLOG_CHATID,
    DEVS, 
    LOGS,
    bot,
    call_py,
    blacklistuser,
    CMD_HANDLER as cmd,
)
from userbot.modules import ALL_MODULES
from userbot.utils import autobot, autopilot

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    blacklistuser = requests.get(
        "https://raw.githubusercontent.com/Saiko006/blacklist/master/saikoblacklist.json"
    ).json()
    if user.id in blacklistuser:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH NGTD, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE BOCAH HINA KEK LU.\nCredits: @teleudahhina"
        )
        sys.exit(1)
    if not DEVS:
        LOGS.warning(
            f"EOL\nSaiko-UserBot v{BOT_VER}, Copyright © 2021-2022 Saiko-Userbot• <https://github.com/Saiko006>"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)
    
if not BOTLOG_CHATID:
    LOGS.info(
        "BOTLOG_CHATID Vars tidak terisi, Memulai Membuat Grup Otomatis..."
    )
    bot.loop.run_until_complete(autopilot())

LOGS.info(
    f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/SaikoSupport"
)

LOGS.info(f"Saiko-Userbot ⚙️ V{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")

async def check_alive():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(BOTLOG_CHATID, f"✨ **Saiko Userbot Berhasil Diaktifkan**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 3.1.0@Saiko-Userbot\n➠ **Ketik** `{cmd}ping` **Untuk Mengecheck Bot**\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @SaikoSupport ")
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass


bot.loop.run_until_complete(check_alive())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars tidak terisi, Memulai Membuat BOT Otomatis di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())
    

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
