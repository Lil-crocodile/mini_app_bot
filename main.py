import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Ваш URL мини-приложения (Web App)
WEB_APP_URL = "https://your-mini-app-url.com"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎁 Get a gift", web_app=WebAppInfo(url="https://lil-crocodile.github.io/Tonnel-Relayer-Bot"))]
    ])
    await update.message.reply_text(
        "Hello! Click on the button below to receive a gift:",
        reply_markup=keyboard
    )

def main():
    TOKEN = "7874681564:AAGH9Lu6M81DF6n217hICJvISuQpwuHfoaw"
    # TOKEN = os.getenv("BOT_TOKEN")  # ✅ токен теперь берётся из переменной окружения

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
