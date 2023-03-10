from pyrogram.types import InlineKeyboardButton

# Project Settings

START = """Hey {user}, welcome to {bot}!

I can convert GIFs and videos to video stickers and create their Sticker Packs specific to you!"""

ABOUT = """
**About This Bot** 

I can convert GIFs and videos to video stickers and create their Sticker Packs specific to you!

Library : [Justin's Video Sticker Bot](https://github.com/JustinWritesCode/VideoStickerBot2)

Language : [Python](www.python.org) (unfortunately)

Developer : @StarkProgrammer
Patcher: [@JustinWritesCode](https://github.com/JustinWritesCode)
"""

REPO = "VideoStickerBot2"

STARKBOTS = True

CUSTOM_USERS_TABLE = True

# REMOVE_ADDONS = ["must_join"]



HELP = """
✨ **Available Commands** ✨

{commands}
"""

HOME_BUTTON = [
    [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
]

MAIN_BUTTONS = [
    [
        InlineKeyboardButton("How to Use ❔", callback_data="help"),
        InlineKeyboardButton("🎪 About 🎪", callback_data="about")
    ],
    [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/BackroomBots")],
]
