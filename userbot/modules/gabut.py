from platform import uname
from time import sleep

from userbot import (
    CMD_HANDLER as cmd,
    ALIVE_NAME, 
    CMD_HELP,
    WEATHER_DEFCITY,
)
from userbot.utils import toni_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@toni_cmd(pattern="g(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG LAH GOBLOKK!!!**")


# Pantun


@toni_cmd(pattern="p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam Dulu Biar Sopan...`")
    sleep(2)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Salam


@toni_cmd(pattern="l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kalo Orang Salam Itu Dijawab...`")
    sleep(2)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Menjawab Salam


@toni_cmd(pattern="kenalin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `putra wibu`")
    sleep(2)
    await typew.edit("✅ `putra wibu`")
    sleep(1)
    await typew.edit("☑️ `duta stres`")
    sleep(2)
    await typew.edit("✅ `duta stres`")
    sleep(1)
    await typew.edit("☑️ `fajar Gajelas`")
    sleep(2)
    await typew.edit("✅ `fajar Gajelas`")
    sleep(1)
    await typew.edit("☑️ `ken Wibu Sangean`")
    sleep(2)
    await typew.edit("✅ `ken Wibu Sangean`")
    sleep(1)
    await typew.edit("☑️ `askar Autis`")
    sleep(2)
    await typew.edit("✅ `askar Autis`")
    sleep(1)
    await typew.edit(
        "`⚡ Cuma Tonic Yang Paling Waras, Baik Hati, Dan Tidak Sombong :v`"
    )


# King Userbot Support


@toni_cmd(pattern="istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")


# Istigfar


@toni_cmd(pattern="alay(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Halo kak**")
    sleep(1)
    await typew.edit("**Gua liat-liat lu main bot mulu**")
    sleep(2)
    await typew.edit("**Alay banget sumpah**")
    sleep(2)
    await typew.edit("**Baru pasang ucelbot ya?**")
    sleep(2)
    await typew.edit("**Pantesan norak yahaha**")
    sleep(2)
    await typew.edit("**Kalo mau coba coba command di gc pribadi aja**")
    sleep(2)
    await typew.edit("**Jangan di publik, jijik liatnya anjg:v**")
    sleep(2)
    await typew.edit("**Intinya lo alay maen bot mulu**")
    sleep(2)
    await typew.edit("**Lawriiiiiiieeeee:v**")


# Alay maen bot mulu ngentot!


@toni_cmd(pattern=r"virtual(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**OOOO**")
    sleep(1.5)
    await typew.edit("**INI YANG VIRTUAL**")
    sleep(1.5)
    await typew.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await typew.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await typew.edit("**NI INGET**")
    sleep(1.5)
    await typew.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await typew.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await typew.edit("**BHAHAHAHA**")
    sleep(1.5)
    await typew.edit("**KASIAN MANA MASIH MUDA**")


@toni_cmd(pattern="perkenalkan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")


# Perkenalan


@toni_cmd(pattern="Tonic(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Ehh Lu Mau Tau Gak?**")
    sleep(1)
    await typew.edit("**Sih Tonic mukanya mirip babi😂**")
    sleep(1)
    await typew.edit("**Ehh Gak Bercanda Deh😁**")
    sleep(1)
    await typew.edit("**Emang Bener Sih Tonic Mukanya Kaya Babi🙈**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh, Tonic Kan Ganteng Kaya Artis Korea😄**")
    sleep(1)
    await typew.edit("**Tapi Boong😂**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Tonic Nangis Minta Balon😂**")
    sleep(1)
    await typew.edit("**Maaf Ya Tonic Ganteng Bercanda😁**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")


# Create by myself @localheart


CMD_HELP.update(
    {
        "gabut": f"**Modules** - `Gabut`\
        \n\n Cmd : `{cmd}l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `{cmd}perkenalkan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `{cmd}alay`\
        \nUsage : ngeledek orang baru pasang bot\
        \n\n Cmd : `{cmd}virtual`\
        \nUsage : ngeledek orang yang virtual\
        \n\n Cmd : `{cmd}g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `{cmd}kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `Tonic`\
        \nUsage : buat ngeledek Tonic\
        \n\n Cmd : `{cmd}p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
