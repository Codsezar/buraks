import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "28467973"))
API_HASH = getenv("API_HASH", "a7b8ebc9c60db6f3b763d32aebb51873")
BOT_PRIVACY = getenv("BOT_PRIVACY", None)
BOT_TOKEN = getenv("BOT_TOKEN", "7958792956:AAFfY7Fj39Tu1rK7QA705TqDZvCS9SK040Y")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Sezar:alp@cluster0.gp7vh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002361838198))

OWNER_ID = int(getenv("OWNER_ID", 7921877964))

OWNER = int(getenv("OWNER", 7921877964))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HK543fklqxgt66hvxf")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AbhiModszYT/AnieXEricaMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Lattedestek")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/LATTEDESTEKTR")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION", "BAGyYwUAxaKnDuBbd-qPhol8kJ2wMYuunZbDMEMCNluRXDPs3v-rDSW5CYG9_qDzH_qpkpoyA7Lcq7zpV7693TLIm0dH0j6DPKa-DGvnF58ltzStWZYeK5-FhqvAGMUuaLcXI_67OkXNXIgm6MN4iQX1xqokax9x_UMI9lEwjVaTFmlogg7UPUeDb15LLPcSE3g7g8UhHyD48fLnjiW7owI09MQlcnJ6_7wBSsZVwVw7WBfjJPIavYaGQ4ZD6azrtB9Pg0YPGjPpC6qbZ8L8y__f0ufEC8QxTQD9CN9lEYmRBkWqEkvvmWGR8HIbr0_h4sQutsZfoMx3p6wVVjt7nuGwOO5urAAAAAHHcSgVAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://t.me/Lattedestek/3")
PING_IMG_URL = getenv("PING_IMG_URL", "https://t.me/Lattedestek/3")
PLAYLIST_IMG_URL = "https://t.me/Lattedestek/3"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://t.me/Lattedestek/3")
TELEGRAM_AUDIO_URL = "https://t.me/Lattedestek/3"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
