#Телеграм-бот 
 
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
#from spy import *


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #logg(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #logg(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #logg(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #logg(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #logg(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x-y}')

async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #logg(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')

async def dev_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #logg(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} / {y} = {x/y}')



app = ApplicationBuilder().token("5479074956:AAEha7e8f8nXdqHH2hxU7cnjiz_KtxgMLV0").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("dev", dev_command))

print('server start')
app.run_polling()