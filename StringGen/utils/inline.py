from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message

from config import SUPPORT_CHAT,OWNER_ID


keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="بدا استخراج الجلسة 🖥️", callback_data="gensession")
                    ],
                    [
                    InlineKeyboardButton("سـورس الزعيم - ", url="t.me/rr_r_v")
                    ],
                    [
                    InlineKeyboardButton("مـعـلـومات الـمـطـور", url="t.me/T_5_G"),
                ],
                [
                    InlineKeyboardButton("الـمـطـور👷", user_id=OWNER_ID),
                    InlineKeyboardButton("اوامـر الـبـوت", url="rr_r_v")
                ]
            ]
        )

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="بايروجورام v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="بايروجورام v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="تليثون", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="استخرج مجدداً", callback_data="gensession")]]
)
