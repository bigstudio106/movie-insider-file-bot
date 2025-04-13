from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    first_name = update.effective_user.first_name
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

    update.message.reply_text(
        text,
        reply_markup=buttons,
        parse_mode="Markdown"
    )

start_handler = CommandHandler("start", start)
