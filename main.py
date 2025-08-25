import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = "8214956306:AAFM1k0QD4J4clTOXPSJRGdWNEOAL7MRA0U"
OPENAI_KEY = "c8OXR9tWFwD8qc1cE62dX1TcSRbahyld6udSd_xbc0xBwNg1jFC35HITNbFEU8CRRUniVSg3VkT3BlbkFJUXLFYwwqxweiI4cqBHlpxvOVCcaj8dNH0vRz2WQCWUykjf_Gf1JBJ-7IPXGaY6In9vMbgLYx4A
"

openai.api_key = OPENAI_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Olá! Eu sou o AJETA EduBot, seu assistente para educação e carreira.\n"
        "Digite sua dúvida sobre bolsas, cursos ou carreiras!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente educacional angolano, ajude com bolsas, carreiras, estudos, universidades e CV."},
            {"role": "user", "content": user_msg}
        ]
    )

    answer = response.choices[0].message.content
    await update.message.reply_text(answer)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
app.run_polling()
