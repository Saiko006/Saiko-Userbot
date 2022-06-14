from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot




async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/928dafe0e365472cac933.jpg",
                caption="🌹 **Saiko UserBot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 5.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @yodhiyah ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/SaikoSupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
