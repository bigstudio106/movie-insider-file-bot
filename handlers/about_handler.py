from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("about"))
async def about(client, message: Message):
    text = (
        "**Developer:** [@i100RBH](https://t.me/i100RBH)\n\n"
        "**Support:** [@MOVIE_INSIDER1](https://t.me/MOVIE_INSIDER1)\n\n"
        "⚡ **Powered by:** Movie Insider Channel\n\n"
        "Hey! 👋 Welcome to **Movie Insider File Bot**\n"
        "I can help you find your favorite movies and series. Just send the name, and I'll get it for you!"
    )
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support", url="https://t.me/MOVIE_INSIDER1")],
        [InlineKeyboardButton("Back to Start", callback_data="start")]
    ])
    
    await message.reply(text, reply_markup=buttons)
