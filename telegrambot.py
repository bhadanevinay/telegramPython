from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Define the start command handler
async def start(update: Update, context: CallbackContext):
    welcome_message = (
        "🎉 Welcome to OmegaOfTS - Your Gateway to Free Premium Courses! 🚀\n\n"
        "✨ We're excited to help you level up your skills with our amazing course collection.\n "
        "Simply click on 'Free Courses' below to explore all the incredible learning opportunities we have for you! 😍"
    )
    await update.message.reply_text(welcome_message)

# Main function to run the bot
def main():
    # Replace 'YOUR_TOKEN' with your bot's token
    application = Application.builder().token("7602061598:AAGJzotMH5aln8WqwMT2Ag4MJqitnyVq204").build()

    # Add handler for the /start command
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
