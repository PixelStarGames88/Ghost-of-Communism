#7678710156:AAEOVnSf6HGru3McFGUd7wnMqsiEn-iV7Gs
#CAACAgIAAxkBAAEO88VoeSqcO9fiOlhpUmAR6k4WCYjjugACJ0gAAro22Ele_Us2kFHCEDYE
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


MY_STICKER_ID = "CAACAgIAAxkBAAEO88VoeSqcO9fiOlhpUmAR6k4WCYjjugACJ0gAAro22Ele_Us2kFHCEDYE"

async def Attack(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    target_for_attack = update.message.chat_id
    n = 100;
    while(n>0):
        n-=1
        try:
            await context.bot.send_sticker(chat_id=target_for_attack, sticker=MY_STICKER_ID)
        except:
            break

    n = 100;
    while(n>0):
        n-=1
        try:
            await context.bot.send_sticker(chat_id=target_for_attack, sticker=MY_STICKER_ID)
        except:
            break

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}! Скажи "/a"!')

app = ApplicationBuilder().token("7678710156:AAEOVnSf6HGru3McFGUd7wnMqsiEn-iV7Gs").build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("a", Attack))

app.run_polling()