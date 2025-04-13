from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackContext

# Help command handler
async def help(update: Update, context: CallbackContext):
    text = (
        "Hey! 👋 You're using **Movie Insider File Bot**\n\n"
        "I can search for **Movies** & **Series** for you!\n"
        "Just send me any movie or series name, and I will get it for you!\n\n"
        "✨ **Make sure the spelling is correct** for better results!\n"
        "⚡ **Powered by:** Movie Insider Channel\n"
        "🙆🏻‍♂️ **Developer:** [@i100RBH](https://t.me/i100RBH)\n"
        "📢 **Support:** [@MOVIE_INSIDER1](https://t.me/MOVIE_INSIDER1)"
    )
    
    buttons = [
        [InlineKeyboardButton("Support", url="https://t.me/MOVIE_INSIDER1")],
        [InlineKeyboardButton("About Developer", callback_data="about_dev")]
    ]
    
    # Send the help message with buttons
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))

# Register the handler
help_handler = CommandHandler("help", help)
