from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("help"))
async def help(client, message: Message):
    text = (
        "Hey! 👋 You're using **Movie Insider File Bot**\n\n"
        "I can search for **Movies** & **Series** for you!\n"
        "Just send me any movie or series name, and I will get it for you!\n\n"
        "✨ **Make sure the spelling is correct** for better results!\n"
        "⚡ **Powered by:** Movie Insider Channel\n"
        "🙆🏻‍♂️ **Developer:** [@i100RBH](https://t.me/i100RBH)\n"
        "📢 **Support:** [@MOVIE_INSIDER1](https://t.me/MOVIE_INSIDER1)"
    )
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support", url="https://t.me/MOVIE_INSIDER1")],
        [InlineKeyboardButton("About Developer", callback_data="about_dev")]
    ])

    await message.reply(text, reply_markup=buttons)
