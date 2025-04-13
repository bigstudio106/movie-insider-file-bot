from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start(client, message: Message):
    first_name = message.from_user.first_name
    text = (
        "**Welcome to Movie Insider File Bot**\n\n"
        "🙊𝙸 𝙲𝙰𝙽 𝚂𝙴𝙰𝚁𝙲𝙷 𝙼𝙾𝚅𝙸𝙴𝚂 & 𝚂𝙴𝚁𝙸𝙴𝚂 𝙵𝙾𝚁 𝚈𝙾𝚄\n"
        "😘𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝙼𝙾𝚅𝙸𝙴 & 𝚂𝙴𝚁𝙸𝙴𝚂 𝙽𝙰𝙼𝙴.\n"
        "😉𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚃𝙷𝙴 𝚂𝙿𝙴𝙻𝙻𝙸𝙽𝙶 𝙰𝚁𝙴 𝙲𝙾𝚁𝚁𝙴𝙲𝚃\n"
        "✨𝙰𝙽𝙳 𝚆𝙰𝙸𝚃 𝙵𝙾𝚁 𝙼𝙴 𝚃𝙾 𝙳𝙾 𝙼𝙰𝙶𝙸𝙲\n\n"
        "⚡**Powered by:** Movie Insider Channel\n"
        "🙆🏻‍♂️**Developer:** [@i100RBH](https://t.me/i100RBH)\n"
        "📢**Support:** [@MOVIE_INSIDER1](https://t.me/MOVIE_INSIDER1)"
    )

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support", url="https://t.me/MOVIE_INSIDER1")],
        [InlineKeyboardButton("About Developer", callback_data="about_dev")]
    ])
    
    await message.reply(text, reply_markup=buttons)
