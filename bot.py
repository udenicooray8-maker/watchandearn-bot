from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        data = context.args[0]

        if data.startswith("balance_"):
            points = data.split("_")[1]
            await update.message.reply_text(f"Your balance is {points} points.")

        elif data.startswith("withdraw_"):
            points = int(data.split("_")[1])

            if points < 1000:
                await update.message.reply_text(
                    f"Minimum withdrawal is 1000 points.\nYou need {1000 - points} more points."
                )
            else:
                await update.message.reply_text("Enter your BTC address:")
    else:
        await update.message.reply_text("Welcome to Watch & Earn Bot!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
